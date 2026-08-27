"""Temas do Punk Records: a camada por assunto por cima das pastas por origem.

Cada item tem um `theme` (escolhido pelo modelo no enriquecimento; `guess_theme` é a reserva por palavras).
`write_theme_pages` gera punk_records/temas/<tema>.md — o que outro projeto lê para aproveitar um assunto sem abrir todos os .md.
"""
import json
import re
import unicodedata
from pathlib import Path

# slug → (ícone, nome, descrição curta, palavras-gatilho para a reserva)
THEMES: dict[str, tuple[str, str, str, tuple[str, ...]]] = {
    "ia-e-agentes": ("🤖", "IA e agentes", "LLMs, Claude Code, agentes, MCP, prompts, benchmarks de modelos",
                     ("ia", "llm", "claude", "agent", "agente", "mcp", "prompt", "benchmark", "gpt", "modelo", "vibecod", "vibe-cod")),
    "desenvolvimento-e-ferramentas": ("🛠", "Desenvolvimento e ferramentas", "código, arquitetura, bibliotecas, infra, Docker, bancos, CLI",
                     ("codigo", "code", "arquitetura", "docker", "sql", "supabase", "nextjs", "fullstack", "cli", "terminal", "lib", "api", "refactor")),
    "seguranca-e-privacidade": ("🔐", "Segurança e privacidade", "LGPD, proteção de dados, vulnerabilidades, auditoria, compliance",
                     ("lgpd", "privacidade", "privacy", "seguranca", "security", "vulnerab", "rls", "xss", "idor", "compliance", "criptograf", "anpd")),
    "produto-e-saas": ("🚀", "Produto e SaaS", "micro-SaaS, validação, retenção, features, PRD, onboarding",
                     ("saas", "produto", "product", "mvp", "validacao", "retencao", "onboarding", "feature", "bootstrap")),
    "marketing-e-vendas": ("📣", "Marketing e vendas", "landing pages, SEO, tráfego, prospecção, copy, redes sociais",
                     ("marketing", "landing", "seo", "trafego", "prospec", "lead", "outreach", "copy", "vendas", "sales", "conversao", "ads")),
    "negocios-e-financas": ("💰", "Negócios e finanças", "preço, receita, custos, orçamento, contratos, gestão",
                     ("preco", "pricing", "receita", "faturar", "custo", "orcamento", "financ", "contrato", "gestao", "roi")),
    "design-e-ux": ("🎨", "Design e UX", "UI, UX, identidade visual, componentes, acessibilidade",
                    ("design", "ui", "ux", "branding", "identidade", "mockup", "figma", "acessib", "front-end-design")),
    "engenharia-civil": ("🏗", "Engenharia civil", "obras, vistoria, laudos, avaliação de imóveis, normas técnicas",
                         ("obra", "vistoria", "laudo", "construcao", "civil", "nbr", "imovel", "avaliacao", "estrutur")),
    "jogos-e-entretenimento": ("🎮", "Jogos e entretenimento", "videogames, filmes, séries, animes, cultura pop",
                               ("game", "jogo", "videogame", "anime", "filme", "serie", "one-piece", "playstation", "nintendo", "steam")),
    "carreira-e-aprendizado": ("📚", "Carreira e aprendizado", "estudo, cursos, emprego, produtividade, hábitos",
                               ("carreira", "career", "aprendiz", "estudo", "curso", "emprego", "job", "entrevista", "produtividade", "habito")),
    "outros": ("📦", "Outros", "o que ainda não tem tema próprio", ()),
}
THEME_IDS = tuple(THEMES)
DEFAULT_THEME = "outros"


def _norm(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s.lower()) if not unicodedata.combining(c))


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", _norm(text)))


def guess_theme(enrichment: dict) -> str:
    """Reserva por palavras (gatilho = prefixo de uma palavra; tags valem 2, título vale 1). Só quando o modelo não deu `theme`."""
    tags = _tokens(" ".join(enrichment.get("tags", [])))
    title = _tokens(enrichment.get("title", ""))
    hit = lambda h, toks: any(t.startswith(h) for t in toks)
    best, best_score = DEFAULT_THEME, 0
    for slug, (_, _, _, hints) in THEMES.items():
        score = sum((2 if hit(h, tags) else 0) + (1 if hit(h, title) else 0) for h in hints)
        if score > best_score:
            best, best_score = slug, score
    return best


def theme_of(enrichment: dict) -> str:
    t = enrichment.get("theme")
    return t if t in THEMES else guess_theme(enrichment)


def label(slug: str) -> str:
    icon, name, _, _ = THEMES.get(slug, THEMES[DEFAULT_THEME])
    return f"{icon} {name}"


def _one_liner(e: dict) -> str:
    text = e.get("brief") or e.get("summary") or ""
    first = re.split(r"(?<=[.!?])\s", text.strip(), maxsplit=1)[0]
    return first[:220]


def group_by_theme(items: list[dict]) -> dict[str, list[tuple[dict, dict]]]:
    """{slug: [(item, enrichment), …]} na ordem de THEMES, itens mais novos primeiro."""
    groups: dict[str, list] = {slug: [] for slug in THEMES}
    for it in items:
        e = json.loads(it["enrichment"]) if isinstance(it.get("enrichment"), str) else it["enrichment"]
        groups[theme_of(e)].append((it, e))
    return {k: v for k, v in groups.items() if v}


def write_theme_pages(items: list[dict], vault_dir: Path, rel_of) -> list[Path]:
    """Uma página por tema em <vault>/temas/. `rel_of(item)` devolve o caminho relativo do .md do item."""
    out_dir = vault_dir / "temas"
    out_dir.mkdir(parents=True, exist_ok=True)
    groups = group_by_theme(items)
    written = []
    for slug, pairs in groups.items():
        icon, name, desc, _ = THEMES[slug]
        lines = [f"# {icon} {name}", "", f"_{desc}._ Gerado automaticamente a partir do Punk Records — {len(pairs)} item(ns). "
                 "Para aproveitar este tema em outro projeto, leia esta página; abra o item só quando precisar do detalhe.", ""]
        for it, e in pairs:
            a = e["applicability"]
            rel = rel_of(it)
            link = f"../{rel}" if rel else ""
            lines += [f"## [{e['title']}]({link})",
                      f"{it['captured_at'][:10]} · {it['platform']} · SaaS {a['saas_pessoal']} · cliente {a['projeto_cliente']} · estudo {a['estudo_geral']}"
                      f" · triagem {it.get('triage_decision') or '—'} · `{'` `'.join(e['tags'][:6])}`",
                      "", _one_liner(e), ""]
        p = out_dir / f"{slug}.md"
        p.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        written.append(p)
    # páginas de temas que ficaram vazios são removidas (o vault é projeção, não acumula lixo)
    for stale in out_dir.glob("*.md"):
        if stale.stem not in groups and stale.name != "README.md":
            stale.unlink()
    return written


def theme_map_lines(groups: dict[str, list]) -> list[str]:
    return [f"- {label(slug)} — {len(pairs)} item(ns) → [temas/{slug}.md](temas/{slug}.md)" for slug, pairs in groups.items()]
