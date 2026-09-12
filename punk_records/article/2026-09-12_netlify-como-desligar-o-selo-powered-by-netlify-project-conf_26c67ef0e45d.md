---
item_id: "9f0a8925-e664-4a81-a18d-b101170b210b"
platform: article
external_id: "26c67ef0e45d"
canonical_url: "https://docs.netlify.com/manage/projects/powered-by-netlify-badge"
channel: "Netlify Docs"
captured_at: 2026-09-12
status: enriched
triage: null
tags: ["netlify", "powered-by-netlify", "marca-de-terceiro", "site-de-cliente", "plano-free", "script-injetado-na-borda", "white-label"]
applicability:
  saas_pessoal: media
  projeto_cliente: alta
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Netlify — como desligar o selo 'Powered by Netlify' (Project configuration > General)

🔗 https://docs.netlify.com/manage/projects/powered-by-netlify-badge

## Resumo

Documentação oficial do selo Powered by Netlify, que aparece no canto inferior direito de todas as páginas de projetos públicos criados em plano Free. Ao clicar nele, o visitante abre um cartão que o convida a construir o próprio projeto no Netlify. A regra de ativação é por data: projetos criados a partir de 19 de agosto de 2026 em plano Free (legado ou Credit-based) nascem com o selo ligado, os anteriores não, e o lançamento é gradual; nos planos Personal e Pro o padrão é desligado e nos Enterprise o recurso não existe. O documento reconhece explicitamente o caso de trabalho para cliente como motivo legítimo para desligar, e o caminho é Project configuration > General > Powered by Netlify badge, alternar e salvar — a mudança vale na requisição seguinte, sem precisar de novo deploy, e o ajuste é por projeto, não por time. O visitante também pode esconder o selo para si em Hide this badge, mas isso fica só no local storage daquele navegador e daquele domínio exato, não vale para www contra domínio raiz e, no Safari e em qualquer navegador de iOS, some depois de 7 dias sem visita. Sobre o script: ele é injetado pelos servidores de borda do Netlify, sem tocar no código-fonte, no build nem nas dependências, não faz requisição de rede, não usa cookie nem analytics, e renderiza num frame isolado para não interferir no CSS da página. O mesmo script desenha a pre-launch toolbar de projetos privados. A seção de troubleshooting lista por que o selo pode não aparecer: rollout ainda não alcançou o projeto, projeto privado, configuração desligada, dispensa local no navegador, plano sem o recurso ou Content Security Policy bloqueando.

## Tópicos

- **Quando o selo vem ligado** — Projetos públicos criados a partir de 19/08/2026 em plano Free nascem com ele; Personal e Pro vêm desligados; Enterprise não tem o recurso.
- **Como desligar** — Project configuration > General > Powered by Netlify badge, alternar e salvar; vale na requisição seguinte, sem redeploy, e é por projeto.
- **Esconder não é desligar** — Hide this badge guarda a escolha no local storage daquele navegador e daquele domínio exato; no Safari e no iOS expira em 7 dias e outros visitantes continuam vendo.
- **O que o script faz na página** — É injetado na borda do Netlify sem tocar no código-fonte, não faz requisição de rede nem usa cookie, e roda em frame isolado. O mesmo script desenha a pre-launch toolbar de projeto privado.
- **Por que o selo pode não aparecer** — Rollout gradual, projeto privado, configuração desligada, dispensa local no navegador, plano sem o recurso, CSP bloqueando ou projeto atrás de login de time/SSO.

## Ferramentas citadas

- **Netlify**: hospedagem que injeta o selo na borda e oferece o interruptor por projeto

## Pontos-chave

- O caminho é Project configuration > General > Powered by Netlify badge; salvar basta, não precisa de novo deploy.
- A configuração é por projeto: desligar em um site não muda os outros do time.
- Projeto público novo em plano Free criado a partir de 19/08/2026 nasce com o selo ligado.
- A própria documentação cita trabalho para cliente como motivo legítimo para desligar.
- O script é injetado na borda: não está no código-fonte e não adianta procurar no repositório.
- Segundo o Netlify, o script não faz requisição de rede, não usa cookie nem analytics, e roda em frame isolado.
- Hide this badge é por navegador e por domínio exato, e no Safari/iOS expira em 7 dias.
- Projeto privado não mostra o selo, mas mostra a pre-launch toolbar, desenhada pelo mesmo script.

## Como aplicar

Desligar ANTES de mandar qualquer prévia a cliente: site de cliente com selo de terceiro no rodapé entrega que a página é demonstração em conta gratuita e rouba a autoria da entrega. Fazer disso item fixo do checklist de publicação, junto com noindex, sitemap e llms.txt. Vale lembrar que o selo não é o único enxerto: o Netlify também injeta um comentário HTML com link UTM para netlify.new e as metatags hosting-provider e netlify-deploy.

## 📚 Pythagoras diz

Aqui está a resposta que os seis links que você mandou não tinham: o selo não é status badge, é outro recurso e tem interruptor próprio. O registro diz que o script vem da borda, então procurar no código-fonte era busca perdida. Desligue antes da prévia; a própria Netlify escreveu que trabalho para cliente é motivo legítimo.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

For the complete Netlify documentation index, see llms.txt. Markdown versions of any documentation page are available by appending `.md` to its URL.

The Powered by Netlify badge appears on new public projects created on a Free plan. Every visitor sees it, and selecting it opens a card that invites them to build a project of their own. You can turn the badge on or off.

### What visitors see

Section titled “What visitors see”
The badge appears in the bottom-right corner of any page of the project:

When a visitor selects the badge, a card opens where they can describe a project they want to build and start it with an agent, or drop an existing project onto Netlify.

The badge looks the same on every project that carries it, and it says nothing about you, your team, or how much traffic you get.

### When is the badge on

Section titled “When is the badge on”
**New projects created on or after August 19, 2026 on a Free plan (either legacy or Credit-based) start with the badge on.** Projects that were created before that date have the badge off. We’re rolling this out gradually, so a brand-new Free project may not have it yet.

On the Credit-based Personal and Pro plans, the badge is off by default, and you can turn it on for any project.

### Turn the badge on or off

Section titled “Turn the badge on or off”
The badge is how visitors discover that a project is powered by Netlify. If it doesn’t suit a particular project you own, such as client work or anywhere third-party branding is out of place, you can turn it off.

The setting is per project, so turning it off on one project leaves the rest of your team’s projects unchanged. To change it:

1. In the Netlify UI, go to your project and select **Project configuration  General  Powered by Netlify badge** .
2. Turn the badge on or off.
3. Save your changes.

The change takes effect on the next request. You don’t need to redeploy the project.

### Hide the badge

Section titled “Hide the badge”
Visitors can dismiss the badge for themselves by selecting **Hide this badge** inside the card. It stays hidden for that project.

The choice is stored only in local storage on your project’s own domain. That means that:

- **Netlify does not collect any information** when the badge is hidden.
- Hiding applies to that browser on that device only. The badge still appears for other visitors.
- If you hide the badge, it will only apply to the exact domain you hid it on. For example, if your browser shows the `example.com` domain and you hide the badge, then you will still find the badge on`www.example.com` .
- Safari clears local storage after 7 days without a visit. On Safari, and any browser on an iOS device, the dismissal is thus not permanent.

To remove the badge for everyone, turn off the Powered by Netlify badge in your project configuration instead.

### What the script does on your page

Section titled “What the script does on your page”
Netlify injects the badge script on our edge servers, so it arrives with the page. Your source, build, and dependencies are untouched. The same script renders the pre-launch toolbar on private projects, so everything in this section applies to both.

- It makes no network requests: no analytics, cookies, or other data collection.
- It renders in an isolated frame, so your project’s CSS can’t affect the badge and the badge can’t affect your layout.

The badge works on any page type, including pages rendered at request time by Netlify Functions and Edge Functions.

### Troubleshooting

Section titled “Troubleshooting”
Here are potential reasons why the badge may not appear:

1. **The rollout hasn’t reached the project.** The badge is rolling out gradually, so a project that qualifies may not have it yet.
2. **The project is private.** The badge appears only on public projects. Check project visibility.
3. **The badge setting is off.** Check**Project configuration  General  Powered by Netlify badge** .
4. **You dismissed it in this browser.** Dismissals are per browser and per domain, so try another browser or a private window.
5. **The plan doesn’t include it.** The badge is available on the legacy and Credit-based Free plans, and on the Credit-based Personal and Pro plans. It is not available on Enterprise plans.
6. **A Content Security Policy is blocking it.** See the note above.

The badge also does not appear on a project protected by team login or SSO.

### More resources

Section titled “More resources”
##### Did you find this doc useful?

Your feedback helps us improve our docs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
