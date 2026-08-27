---
item_id: "db67e79b-de3d-4230-8ba9-4904fbd42561"
platform: article
external_id: "8b722ef0051f"
canonical_url: "https://developers.google.com/recaptcha/docs/v3?hl=pt-br"
channel: "Google for Developers"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["recaptcha", "recaptcha-v3", "anti-bot", "formularios", "seguranca", "javascript"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: seguranca-e-privacidade
content_type: article
---

# reCAPTCHA v3 — pontuação sem atrito: carregar o script, vincular a botão ou executar programaticamente, interpretar a pontuação

🔗 https://developers.google.com/recaptcha/docs/v3?hl=pt-br

## Resumo

Documentação do reCAPTCHA v3 (Google): devolve uma pontuação de 0,0 (bot) a 1,0 (humano) para cada requisição, sem desafio ao usuário; chaves criadas no Admin Console. Recomenda-se rodar em formulários/ações e também em segundo plano nas páginas, para dar mais contexto ao modelo; pode-se executar quantas ações quiser por página. Dois modos: automático (carregar api.js, callback que recebe o token, botão com classe g-recaptcha, data-sitekey, data-callback e data-action) ou programático (carregar api.js?render=site_key e chamar grecaptcha.execute(site_key, {action}) retornando o token, enviado imediatamente ao backend para verificação). Interpretação: definir limiar por ação (ex.: 0,5) e reagir — permitir, pedir verificação extra, bloquear; ações nomeadas melhoram a análise no console.

## Tópicos

- **Como funciona** — Pontuação por requisição, sem atrito; chaves no Admin Console.
- **Integração** — Botão g-recaptcha com data-action, ou grecaptcha.execute programático; token verificado no backend.
- **Uso da nota** — Limiar por ação; ações nomeadas para análise.

## Pontos-chave

- Sem atrito: não afeta conversão do formulário do cliente.
- O token tem que ser verificado no servidor — no front não vale nada.
- Rodar também em páginas comuns melhora a precisão.

## Como aplicar

Formulário de contato do site do cliente e cadastro do SaaS com v3 + verificação no backend (FastAPI); comparar com Turnstile da Cloudflare (item no vault), que é grátis e sem Google.

## 🔧 Atlas diz

Dois caminhos, ambos com o mesmo parafuso: o token só vale depois de verificado no servidor. E aqui a comparação de bancada: o Turnstile da Cloudflare (já no vault) faz o mesmo sem mandar seu usuário pro Google. Para o cliente, eu testaria o Turnstile primeiro.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

O reCAPTCHA v3 retorna uma pontuação para cada solicitação sem atrito do usuário. A pontuação tem como base as interações com o site e permite que você tome uma ação apropriada para ele. Registre chaves reCAPTCHA v3 no Admin Console do reCAPTCHA.

Esta página explica como ativar e personalizar o reCAPTCHA v3 na sua página da Web.

### Posicionamento no site

O reCAPTCHA v3 nunca interrompe os usuários, para que você possa executá-lo quando quiser, sem afetar e conversão em massa. O reCAPTCHA funciona melhor quando tem o máximo de contexto sobre as interações com o site, que vem de um comportamento legítimo e abusivo. Por isso, recomendamos incluindo a verificação reCAPTCHA em formulários ou ações, bem como em segundo plano em páginas para análise de dados em nuvem.

Você pode executar o reCAPTCHA em quantas ações desejar na mesma página.

### Vincular o desafio automaticamente a um botão

O método mais fácil para usar o reCAPTCHA v3 na sua página é incluir o necessário do JavaScript e adicione alguns atributos ao seu botão HTML.

1. Carregue a API JavaScript. ```
 <script src="https://www.google.com/recaptcha/api.js"></script>
```
2. Adicione uma função de callback para processar o token. ```
 <script>
   function onSubmit(token) {
     document.getElementById("demo-form").submit();
   }
 </script>
```
3. Adicione atributos ao botão HTML. ```
<button class="g-recaptcha" 
        data-sitekey="reCAPTCHA_site_key" 
        data-callback='onSubmit' 
        data-action='submit'>Submit</button>
```

### Invoque o desafio programaticamente

Se você quiser ter mais controle sobre quando o reCAPTCHA é executado, use o
Método `execute` no objeto `grecaptcha`. Para isso,
você precisa adicionar um parâmetro `render` ao carregamento do script reCAPTCHA.

1. Carregue a API JavaScript com a chave do site. ```
<script src="https://www.google.com/recaptcha/api.js?render=reCAPTCHA_site_key"></script>
```
2. Chame `grecaptcha.execute` em cada ação que você quer proteger.```
   <script>
      function onClick(e) {
        e.preventDefault();
        grecaptcha.ready(function() {
          grecaptcha.execute('reCAPTCHA_site_key', {action: 'submit'}).then(function(token) {
              // Add your logic to submit to your backend server here.
          });
        });
      }
  </script>
```
3. Enviar o token imediatamente para seu back-end com a solicitação para verificar.

### Como interpretar a pontuação

O reCAPTCHA v3 retorna uma pontuação (1,0 é muito provavelmente uma boa interação, 0,0 é muito provavelmente um bot). Com base na pontuação, você pode realizar ações variáveis no contexto do seu site. Todo site é mas abaixo estão alguns exemplos de como os sites usam a pontuação. Como nos exemplos abaixo, nos bastidores em vez de bloquear o tráfego para proteger melhor o site.

| Caso de uso | Recomendação | 
|---|---|
| homepage | Confira uma visão coesa do tráfego no Admin Console ao filtrar as raspagens de informação. | 
| login | Com pontuações baixas, exigem autenticação de dois fatores ou verificação de e-mail para evitar ataques de preenchimento de credenciais. | 
| social | Limite as solicitações de amizade não respondidas de usuários abusivos e envie comentários de risco para a moderação. | 
| E-commerce | Coloque vendas reais à frente dos bots e identifique transações arriscadas. | 

O reCAPTCHA aprende com o tráfego real no seu site. Por isso, as pontuações em um teste ou logo após a implementação pode diferir da produção. Como o reCAPTCHA v3 nunca interromper o fluxo do usuário, primeiro execute o reCAPTCHA sem tomar medidas e, em seguida, decida específicos ao analisar o tráfego no Admin Console. De padrão, é possível usar um limite de 0,5.

### Ações

O reCAPTCHA v3 introduz um novo conceito: ações. Quando você especifica um nome de ação em cada local em que o reCAPTCHA é executado, os seguintes novos recursos são ativados:

- Uma análise detalhada dos dados das dez principais ações no Admin Console
- Análise de risco adaptável com base no contexto da ação, porque anúncios abusivos podem variar.

É importante ressaltar que, ao verificar a resposta reCAPTCHA, você deve confirmar se o nome da ação é o nome esperado.

### Resposta de verificação do site

Faça a solicitação para verificar o token de resposta, assim como acontece com o reCAPTCHA v2 ou reCAPTCHA invisível.

A resposta é um objeto JSON:

```
{
  "success": true|false,      // whether this request was a valid reCAPTCHA token for your site
  "score": number             // the score for this request (0.0 - 1.0)
  "action": string            // the action name for this request (important to verify)
  "challenge_ts": timestamp,  // timestamp of the challenge load (ISO format yyyy-MM-dd'T'HH:mm:ssZZ)
  "hostname": string,         // the hostname of the site where the reCAPTCHA was solved
  "error-codes": [...]        // optional
}
```
#### Dicas

1. `grecaptcha.ready()` executa a função quando a biblioteca reCAPTCHA é carregada. Para
evitar disputas com o`api.js` , inclua o`api.js` antes do
scripts que chamam grecaptcha ou continuam a usar o
callback onload definido com a API v2.
2. Tente conectar a chamada `execute` a ações interessantes ou sensíveis, como
Registrar, redefinir senha, comprar ou jogar.
3. Use o `https://www.google.com/recaptcha/api.js?trustedtypes=true` para
carregar código compatível com os Tipos confiáveis.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
