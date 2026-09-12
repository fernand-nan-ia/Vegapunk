---
item_id: "c957d76c-f99b-4faa-95dc-04eeaf1dcfdf"
platform: article
external_id: "62f1f3b4fc7c"
canonical_url: "https://docs.netlify.com/manage/monitoring/monitor-builds"
channel: "Netlify Docs"
captured_at: 2026-09-12
status: archived
triage: archive
tags: ["netlify", "build-minutes", "fila-de-build", "builds-concorrentes", "audit-log", "custo-de-build"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Netlify — acompanhar builds do time: fila, prioridade e minutos gastos

🔗 https://docs.netlify.com/manage/monitoring/monitor-builds

## Resumo

Documentação da aba Builds do time no Netlify. A página principal lista todos os builds e seu estado (completed, building ou enqueued aguardando capacidade) e leva à página de detalhe de cada um, onde se lê o log e se cancela o deploy. O indicador de Concurrent builds mostra quanto da capacidade está em uso, e há alerta quando existe build na fila. Developers e Owners do time podem priorizar um build pendente com a ação Build next: ele passa a Enqueued: Prioritized, com o nome de quem priorizou registrado também no audit log do time, e começa assim que o build ativo terminar — para começar na hora, é preciso cancelar um build em execução. Só um build pode estar priorizado por vez. A página Usage & insights traz o histórico de minutos de build, com gráficos de minutos por dia e builds por dia e a lista dos sites que mais consumiram tempo, atualizada de hora em hora. Dados adicionais ficam em Billing > Account usage insights, e há um resumo rápido na página Projects do time.

## Tópicos

- **Estado atual dos builds** — Lista com completed, building e enqueued aguardando capacidade, mais o indicador de builds concorrentes em uso.
- **Priorizar um build** — Developers e Owners usam Build next; o build vira Enqueued: Prioritized, fica registrado no audit log e só um pode estar priorizado por vez.
- **Histórico de uso** — Usage & insights mostra minutos de build por dia, número de builds por dia e os sites que mais consumiram, com atualização de hora em hora.

## Ferramentas citadas

- **Netlify**: painel onde a fila de builds e o consumo de minutos do time são acompanhados

## Pontos-chave

- Build enfileirado é falta de capacidade concorrente, não erro.
- Build next apenas fura a fila no próximo espaço; para rodar na hora é preciso cancelar um build ativo.
- A priorização fica registrada no audit log com o nome de quem fez.
- Os dados de minutos atualizam de hora em hora e exigem recarregar a página.
- A lista Top sites aponta onde cortar tempo de build tem mais efeito.

## Como aplicar

Com um site só isto quase não importa. Passa a importar quando houver vários clientes na mesma conta: minuto de build é recurso compartilhado do time, e a página Top sites mostra qual cliente está consumindo o tempo dos outros.

## 📚 Pythagoras diz

Registro sem urgência: com um cliente só, a fila nunca vai te alcançar. Guardo pensando no terceiro ou quarto site na mesma conta, quando minuto de build vira recurso disputado e a página Top sites diz de quem é a culpa.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

For the complete Netlify documentation index, see llms.txt. Markdown versions of any documentation page are available by appending `.md` to its URL.

You can check your team’s current builds status and get insights into historical builds usage by visiting your team’s **Builds** tab.

### Current status

Section titled “Current status”
On the main **Builds** page, you’ll find a list of all of your team’s builds and their current state such as completed, building, or enqueued: awaiting capacity.

Select any build to visit its detail page where you can examine the deploy log, cancel the deploy, and more.

The **Concurrent builds** numbers show how much of your build capacity you’re currently using. If you have any builds that are enqueued awaiting capacity, there will be an alert message with details on how many builds are waiting for capacity.

#### Prioritize a build

Section titled “Prioritize a build”
If you have a build waiting in your team build queue that you would like to build sooner, team-wide Developers and Owners can prioritize the build so that it runs as soon as the next space opens in your team build capacity.

To prioritize a build, go to your team **Builds** page and select the build you want to prioritize, then select **Build next**.

After confirming your choice, the build will be marked **Enqueued: Prioritized**, along with the name of the team member who prioritized it, and the time it was prioritized. The action is also tracked in the team audit log.

Your prioritized build will begin when the next active build completes. If you would like the build to start immediately, you can cancel an active build to make room in your team build capacity.

Only one build can be prioritized at a time. If any team member selects a new build to prioritize, it will replace the currently prioritized build.

### Historical insights

Section titled “Historical insights”
Switch to the **Usage & insights** page for more information about your team’s builds usage. Here you’ll find data on how your build minutes have been used including the sites that have accrued the most build time. This data updates hourly. You will need to refresh your browser to load the updates.

You can examine the **Build minutes used per day** and **Number of builds per day** charts to explore day-level details.

In the **Top sites** chart, you can select the name of any site to visit the site’s dashboard.

### Account usage insights

Section titled “Account usage insights”
You can find additional data about your team’s builds under **Billing  Account usage insights**. Learn more about usage and insights.

### Team usage summary

Section titled “Team usage summary”
For a quick summary of your team’s usage, go to your team’s **Projects** page and check out the usage metrics above your sites list. Select a metric widget to expand its details.

On the **Builds** card, you can find a condensed list of the latest team builds and their current state.

### More resources

Section titled “More resources”
Learn more about concurrent builds and build minutes in our Billing doc.

Visit our Forums for a verified Support Guide on optimizing what and how you build to reduce build queueing and make the most of your build minutes. You can even temporarily stop builds for a site if needed. Focusing these efforts on the **Top sites** revealed on the **Usage & insights** page is likely to have the most impact since those sites are accruing the most build time.

##### Did you find this doc useful?

Your feedback helps us improve our docs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
