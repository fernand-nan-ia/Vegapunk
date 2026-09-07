---
item_id: "23f0ca48-ad3b-4898-8ac6-25c2a89c0aa3"
platform: article
external_id: "c5264a1d16b4"
canonical_url: "https://github.com/abi/screenshot-to-code"
channel: "Abi · GitHub"
captured_at: 2026-09-07
status: archived
triage: archive
tags: ["screenshot-to-code", "design-para-codigo", "self-hosted", "tailwind", "figma", "custo-de-api", "prototipagem"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: ia-e-agentes
content_type: article
---

# screenshot-to-code: aplicação self-hosted que converte print, Figma e gravação de tela em código

🔗 https://github.com/abi/screenshot-to-code

## Resumo

screenshot-to-code converte capturas de tela, mockups, designs do Figma e até gravações de tela em código funcional. É importante entender o que ele NÃO é: não é uma skill nem um plugin de agente, e sim uma aplicação web completa que se roda na própria máquina — frontend em React/Vite e backend em FastAPI, com Poetry, Playwright e Chromium para o modo de pré-visualização. As pilhas de saída suportadas são HTML+Tailwind, HTML+CSS, React+Tailwind, Vue+Tailwind, Bootstrap e Ionic+Tailwind. Ele não traz modelo próprio: exige pelo menos uma chave de API entre OpenAI, Anthropic e Gemini, e o README recomenda fortemente Gemini e Replicate — o Gemini porque extrai os ativos reais do print (logos e imagens de verdade em vez de recriados) e é obrigatório para o modo de vídeo, o Replicate porque habilita geração e edição de imagem e remoção de fundo. Com mais chaves, a aplicação escolhe automaticamente uma mistura mais forte de modelos e permite comparar variantes lado a lado. Há um recurso opcional em que o agente renderiza a própria página gerada num navegador headless e confere visualmente o próprio trabalho. Existe também um produto hospedado e pago no screenshottocode.com, do mesmo autor — o repositório é a versão que se roda por conta própria, sob licença MIT.

## Tópicos

- **O que é de fato** — Aplicação web completa rodada localmente — frontend React/Vite, backend FastAPI com Poetry, Playwright e Chromium — ou usada pelo produto hospedado pago do mesmo autor.
- **Pilhas de saída** — HTML+Tailwind, HTML+CSS, React+Tailwind, Vue+Tailwind, Bootstrap e Ionic+Tailwind — a escolha é do usuário no momento da geração.
- **Chaves de API obrigatórias** — Pelo menos uma entre OpenAI, Anthropic e Gemini. Gemini é fortemente recomendado porque extrai os ativos reais do print e é exigido no modo vídeo; Replicate habilita geração, edição e remoção de fundo.
- **Modo gravação de tela** — Aceita um vídeo do site em uso e devolve um protótipo funcional, não só a tela estática.
- **Autoconferência visual** — Recurso opcional em que o agente renderiza a página gerada num Chromium headless e verifica o próprio resultado; some silenciosamente se o Chromium não estiver instalado.
- **Modelo de negócio** — Repositório MIT self-hosted ao lado de um produto hospedado pago (screenshottocode.com) do mesmo autor; a versão livre é a que exige as chaves próprias.

## Ferramentas citadas

- **FastAPI**: backend da aplicação, servido por uvicorn na porta 7001
- **React + Vite**: frontend da aplicação, na porta 5173
- **Playwright / Chromium**: navegador headless para o recurso de pré-visualização e autoconferência da página gerada
- **Gemini**: modelo recomendado; extrai os ativos reais do print e é obrigatório para o modo de vídeo
- **Replicate**: geração e edição de imagem e remoção de fundo; sem ele, edit_images e remove_backgrounds ficam indisponíveis
- **Docker Compose**: caminho alternativo de execução, sem recarga automática ao editar arquivos

## Pontos-chave

- 78.141 estrelas, MIT, último push em 14/08/2026 — verificado na API em 07/09
- NÃO é skill de agente: é aplicação self-hosted com backend e frontend próprios
- O custo sai FORA do plano Max da Anthropic — cada geração consome chave de API própria
- Gemini é o recomendado por extrair os ativos reais do print, não por ser o mais barato
- Modo de gravação de tela transforma vídeo de site em uso em protótipo funcional
- O Claude Code já lê imagem nativamente: colar um print no chat cobre boa parte do caso de uso sem custo extra
- A lista de modelos do README está internamente inconsistente entre a seção de padrões e a tabela de chaves
- Existe produto hospedado pago do mesmo autor — o repo é a versão que você mesmo mantém

## Como aplicar

Só se justifica se a conversão de print em código virar rotina e o Claude Code se mostrar insuficiente — hoje ele já lê imagem nativamente e o plano Max cobre esse uso sem chave extra. O caso em que o repositório ganha é o modo de gravação de tela e a extração de ativos reais do print pelo Gemini, que o chat não faz. Antes de subir, medir: cada geração é gasto avulso, fora do Max.

## 💡 Edison diz

Eureka — e logo depois um 'opa'. A ideia é boa: print entra, código sai, e o modo de GRAVAÇÃO de tela é coisa que o chat não faz, isso me acendeu a orelha. Mas repara: é uma aplicação inteira para subir e manter, e cada geração come chave de API tua, fora do Max que você já paga. A gente colar um print no Claude Code custa zero. Guarda a ideia do vídeo→protótipo, deixa o resto na prateleira.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Convert screenshots, mockups, Figma designs, and screen recordings into clean, functional code using AI. The easiest way to try this is using the official, hosted product at screenshottocode.com →

#### youtube.mp4

Supported stacks:

- HTML + Tailwind
- HTML + CSS
- React + Tailwind
- Vue + Tailwind
- Bootstrap
- Ionic + Tailwind

Default AI models:

- Gemini 3 Flash Preview and Gemini 3.1 Pro Preview - the best models
- GPT-5.5 and GPT-5.4 Mini
- Claude Opus 4.6, Claude Opus 4.8
- z-image-turbo (using Replicate) for image generation

See the Examples section below for more demos.

Screenshot to Code also supports taking a screen recording of a website in action and turning that into a functional prototype.

Choose the path that fits what you want to do:

- **Run locally:** best if you want to customize, self-host, or contribute.
- **Use the hosted app:** the fastest way to try Screenshot to Code with no local setup. Open the hosted app →

Running locally requires API keys and a backend/frontend setup. The app has a React/Vite frontend and a FastAPI backend.

You need **at least one** model provider key (OpenAI, Anthropic, or Gemini).
**Gemini and Replicate are strongly recommended for the best quality of
screenshot-to-code accuracy** — Gemini powers asset extraction (reusing the
real logos/images from your screenshot) and Replicate powers image
generation, background removal, and image editing. Adding all four keys gives
the best results and lets you compare multiple models per generation.

| Key | Required? | What it unlocks | 
|---|---|---|
| `OPENAI_API_KEY` | One of these three | GPT code-gen variants (GPT-5.5, GPT-5.4 Mini) | 
| `ANTHROPIC_API_KEY` | One of these three | Claude code-gen variants (Opus 5, Opus 4.8, Fable 5, Sonnet 4.6) | 
| `GEMINI_API_KEY` | One of these three — **strongly recommended** | Gemini code-gen variants (3 Flash, 3.1 Pro); extracts real assets from the screenshot; required for video mode | 
| `REPLICATE_API_KEY` | **Strongly recommended** | Image editing, background removal, and Replicate-backed image generation — without it, `edit_images` and`remove_backgrounds` are unavailable | 

With more keys, the app automatically picks a stronger mix of models per variant; with a single key it uses that provider's models only.

If you'd like to run the app with Ollama open-source models (not recommended due to poor-quality results), follow this comment.

Run the backend (I use Poetry for package management; run `pip install --upgrade poetry` if you don't have it):

```
cd backend
echo "OPENAI_API_KEY=sk-your-key" > .env
echo "ANTHROPIC_API_KEY=your-key" >> .env
echo "GEMINI_API_KEY=your-key" >> .env
echo "REPLICATE_API_KEY=r8_your-key" >> .env
poetry install
### Install the Chromium browser used by the screenshot preview tool.
### On Linux, use `poetry run playwright install --with-deps chromium` to also
### install the required system libraries (needs sudo/apt).
poetry run playwright install chromium
poetry env activate
### run the printed command, e.g. source /path/to/venv/bin/activate
poetry run uvicorn main:app --reload --port 7001
```
You can also set up OpenAI, Anthropic, and Gemini keys using the settings dialog in the frontend (click the gear icon after loading the app). Replicate must be configured in `backend/.env` as `REPLICATE_API_KEY`. The Settings dialog also shows whether **screenshot preview** is available on your backend.

**Screenshot preview** (optional) lets the agent render its own generated page in a headless browser and visually check its work. It's enabled automatically once Chromium is installed (the `playwright install chromium` step above, or automatically in the Docker image). If Chromium is missing, the app just skips the tool — the Settings dialog shows whether it's available.


Run the frontend:

```
cd frontend
pnpm install
pnpm dev
```
Open http://localhost:5173 to use the app.

If you prefer to run the backend on a different port, update `VITE_WS_BACKEND_URL` in `frontend/.env.local`.

If you have Docker installed, run this from the root directory:

```
echo "OPENAI_API_KEY=sk-your-key" > .env
docker-compose up -d --build
```
The app will be up and running at http://localhost:5173. Note that you can't develop the application with this setup, as file changes won't trigger a rebuild.

- **I'm running into an error when setting up the backend. How can I fix it?** Try this. If that still doesn't work, open an issue.
- **How do I get an OpenAI API key?** See https://github.com/abi/screenshot-to-code/blob/main/Troubleshooting.md
- **How can I configure an OpenAI proxy?** If you're not able to access the OpenAI API directly, for example because of country restrictions, you can try a VPN or configure the OpenAI base URL to use a proxy. Set`OPENAI_BASE_URL` in`backend/.env` or directly in the UI in the settings dialog. Make sure the URL has`v1` in the path, for example:`https://xxx.xxxxx.xxx/v1` .
- **How can I update the backend host that my frontend connects to?** Configure`VITE_HTTP_BACKEND_URL` and`VITE_WS_BACKEND_URL` in`frontend/.env.local` . For example, set`VITE_HTTP_BACKEND_URL=http://124.10.20.1:7001` .
- **Seeing UTF-8 errors when running the backend?** On Windows, open the`.env` file with Notepad++, then go to Encoding and select UTF-8.
- **How can I provide feedback?** For feedback, feature requests, and bug reports, open an issue or ping me on Twitter.

**NYTimes**

| Original | Replica | 
|---|---|

**Instagram**

#### instagram.mp4

**Hacker News**

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
