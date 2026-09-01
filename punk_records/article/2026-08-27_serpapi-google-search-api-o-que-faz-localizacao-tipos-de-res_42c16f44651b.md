---
item_id: "d448d9b2-d130-4178-bf0f-950402c53278"
platform: article
external_id: "42c16f44651b"
canonical_url: "https://serpapi.com/"
channel: "SerpApi"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["serpapi", "google-search-api", "serp", "seo-local", "google-maps", "api"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# SerpApi — Google Search API: o que faz, localização, tipos de resultado, SLA e Legal Shield

🔗 https://serpapi.com/

## Resumo

Página-produto do Google Search API da SerpApi. A proposta: usar a infraestrutura deles (IPs no mundo todo, cluster de navegadores completos, resolução de CAPTCHAs) para obter resultados do Google como um humano os vê, imediatamente, em JSON estruturado. Localização precisa por parâmetro 'location' (usa os parâmetros geolocalizados e criptografados do Google e roteia pelo proxy mais próximo; há endpoint de locations). Tipos de resultado: orgânicos, Maps, Local, Stories, Shopping, Direct Answer e Knowledge Graph, com links, endereços, preços, thumbnails, avaliações, rich snippets. Mesmas cotas da página de preços (250 grátis; 1.000; 5.000 Developer; 30.000; enterprise), contrato mês a mês. Throughput garantido de 20% do volume mensal por hora (planos com mais de 1 milhão têm outra regra). SLA de 99,95% com penalidade de 100% (créditos até o valor mensal). Reembolso em 7 dias se menos de 20% usado. U.S. Legal Shield: a SerpApi assume a responsabilidade pela coleta lícita de dados públicos de busca (não pelo uso que você faz), incluído no plano Production e acima, até US$ 2 milhões.

## Tópicos

- **Infra** — IPs globais, navegador completo, CAPTCHA resolvido; resposta imediata; resultado igual ao de um humano.
- **Localização** — Parâmetro location por cidade, proxy mais próximo, endpoint /locations.
- **Tipos de resultado** — Orgânico, Maps, Local, Stories, Shopping, Direct Answer, Knowledge Graph; dados ricos por resultado.
- **Garantias** — SLA 99,95% com penalidade de 100%; throughput 20%/h; reembolso 7 dias; Legal Shield Production+ (US$ 2 mi).

## Ferramentas citadas

- **SerpApi Google Search API**: endpoint principal de resultados do Google
- **Endpoint /locations**: resolver nomes de lugar para o parâmetro location

## Pontos-chave

- Devolve o que um usuário real veria naquela cidade — útil para SEO local e pesquisa de mercado por região.
- Além do orgânico, traz Maps/Local com endereço, telefone e avaliações — substitui scraping frágil do Google Maps.
- SLA com penalidade de 100% é raro em API barata.
- Legal Shield cobre a coleta, não o uso: LGPD e direitos autorais continuam sendo problema seu.

## Como aplicar

Substitui o scraping do Google Maps que o vault já registrou como frágil (prospecção de clientes): uma busca Local por cidade devolve nome, endereço e avaliações em JSON, com contrato mês a mês.

## 💡 Edison diz

Eureka — lembra da ideia de prospectar cliente pelo Google Maps que a Lilith afundou por ser scraping? Isso aqui é a mesma coisa com contrato, SLA e CAPTCHA resolvido por eles. Combina com o item de prospecção ativa do vault: busca Local por cidade + a API de Places oficial como reserva. Protótipo de fim de semana; a Lilith vai bater no Legal Shield que só vem no plano caro.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

##### Pricing

Choose the plan that suits you best.

Find the right data solutions tailored to your market.

Automate your projects with structured SERP data.

Start integration with your preferred language.

Dive deeper into our advanced features.

Explore company information and helpful guides.

Leverage our infrastructure (IPs across the globe, full browser cluster, and CAPTCHA solving technology), and exploit our structured SERP data in the way you want.

              Each API request runs immediately – no waiting for results.

              In addition, each API request runs in a full browser, and we'll even solve all CAPTCHAs, completely mimicking what a human would do.
              This guarantees that you get what users truly see.
            

              Get Google results from anywhere in the world with our "location" parameter.

              SerpApi uses Google’s geolocated, encrypted params and routes your request through the proxy server nearest to your desired location to ensure accuracy. Get locations at our locations endpoint.
            

              Regular organic results are available as well as Maps, Local, Stories, Shopping,
              Direct Answer, and Knowledge Graph.

Lots of structured data is available for each result,
              including links, addresses, tweets, prices, thumbnails, ratings, reviews, rich snippets, and more.
            

Our U.S. Legal Shield covers the scraping and parsing of search engine data, as long as your use of the data or service is not illegal. Such illegal use includes, by way of example and not limitation, copyright infringement, DMCA violations, other intellectual property infringement, privacy violations, fraud, harassment, cybercrime, terrorism, child exploitation, denial-of-service attacks, or war crimes. In short, we assume liability for the lawful collection of public search data, but not for how that data is ultimately used. Included with the Production Plan and above, with up to $2 million in coverage.

Month-to-month contract. Cancel anytime.

              
              1,000 searches per month
            

            
              
              200 throughput per hour
            

              
                
                U.S. Legal Shield
                
              

          
              
              5,000 searches per month
            

            
              
              1,000 throughput per hour
            

              
              
              30,000 searches per month
            

            
              
              6,000 throughput per hour
            

              Start for free, upgrade as you grow, or contact our team about an enterprise plan tailored to your volume, performance, and compliance needs.

View all plans
              
              250 searches per month
            

            
              
              50 throughput per hour
            

            
              
              ZeroTrace Mode
            

            
              
              Priority support
            

          Engineered for total data privacy, industry-leading compliance, and guaranteed global reliability.

- 
        #### ZeroTrace ModeWith ZeroTrace Mode enabled, we don't store your search parameters, files, or data. Once a search completes, it's as if it never happened.
- 
        #### Security & ComplianceWe're SOC 2 Type II, SOC 3, and ISO 27001 certified - Independently audited controls for security, availability, and confidentiality.
- 
        #### Premium supportGet help from a global team of experts, ready to guide you through any issue. Backed by uptime SLAs of up to 99.97%.

You are in good company. Join them.

How are searches counted?

          Only successful searches are counted towards your monthly searches. Cached, errored, and failed searches are not.  The number of results returned per response will not affect the number of credits used - responses with 100 results or empty result sets will both cost 1 search credit.

        What's your guaranteed throughput?

          The hourly throughput limit for plans with under 1 million searches per month is 20% of your plan volume. For example, the Developer Plan includes 5,000 searches per month, so subscribers to the Developer Plan can use up to 1,000 successful searches per hour. For plans with 1 million or more searches per month, the hourly throughput is 100,000 + 1% of your plan volume. While we have no other specific rate limit, we recommend spreading your searches evenly throughout each hour for the best performance.

        What if I need more volume?

          If you need more volume, we can offer you custom plans that fit your needs. Contact us for more information or check out our standard plans.

        Do you provide SLA guarantees?

          We provide a 99.95% SLA guarantee with all plans. The SLA guarantee comes with a 100% penalty, and we offer credits up to 100% of the monthly price of your plan on your next invoice.

        What’s your refund policy?

          We offer full refund within 7 days of the day you subscribed to a plan unless you've used more than 20% of your searches.

        What are scraper legal protections?

          
            Our U.S. Legal Shield covers the scraping and parsing of search engine data, as long as your use of the data or service is not illegal.
            Such illegal use includes, by way of example and not limitation, copyright infringement, DMCA violations, other intellectual property infringement, privacy violations, fraud, harassment, cybercrime, terrorism, child exploitation, denial-of-service attacks, or war crimes.
            In short, we assume liability for the lawful collection of public search data (scraping, parsing, and related actions), but not for how that data is ultimately used.
            U.S. Legal Shield is included with the Production Plan and above, with up to $2 million in coverage. Learn more.
          

        For more answers visit our FAQ page

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
