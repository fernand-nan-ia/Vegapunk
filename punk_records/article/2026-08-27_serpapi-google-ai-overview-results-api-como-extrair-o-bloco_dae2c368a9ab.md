---
item_id: "a52788dd-f60f-479e-94e3-97de74eb791f"
platform: article
external_id: "dae2c368a9ab"
canonical_url: "https://serpapi.com/ai-overview"
channel: "SerpApi"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["serpapi", "google-ai-overview", "seo", "api", "llm", "documentacao"]
applicability:
  saas_pessoal: media
  projeto_cliente: media
  estudo_geral: alta
confidence: alta
theme: ia-e-agentes
content_type: article
---

# SerpApi — Google AI Overview Results API: como extrair o bloco de IA do Google em JSON

🔗 https://serpapi.com/ai-overview

## Resumo

Documentação da extração do bloco 'AI Overview' (o resumo gerado por IA no topo de algumas buscas do Google) pela SerpApi, no mesmo endpoint engine=google. Hoje o bloco só aparece em buscas em inglês (hl=en) e em poucos países (gl). Às vezes o Google exige uma segunda requisição para carregar o AI Overview — a doc mostra como tratar esse caso (page_token) e há um engine dedicado google_ai_overview. A resposta traz ai_overview com text_blocks tipados (paragraph, heading, list — listas com título, snippet e às vezes thumbnail), snippet_highlighted_words, reference_indexes ligando cada trecho às references (título, link, snippet, fonte, índice) e uma thumbnail. Exemplos cobrem resultado típico, lista com miniaturas e casos de requisição extra. Texto integral guardado (44k caracteres).

## Tópicos

- **Disponibilidade** — Só hl=en e alguns gl; pode exigir requisição extra (page_token) ou o engine google_ai_overview.
- **Estrutura** — ai_overview.text_blocks (paragraph/heading/list), snippet_highlighted_words, reference_indexes → references (title, link, snippet, source).
- **Uso** — Monitorar como a IA do Google resume um tema e quais fontes cita — SEO e pesquisa de mercado.

## Ferramentas citadas

- **SerpApi Google AI Overview API**: engine dedicado para o bloco de IA

## Pontos-chave

- Permite ver que fontes o Google cita no resumo de IA para uma pergunta — insumo direto para SEO de conteúdo.
- Limitação forte hoje: só inglês; em pt-BR o bloco não vem.
- Cada trecho aponta as referências que o sustentam (reference_indexes), o que facilita auditar o resumo.
- Pode custar duas buscas por consulta quando o Google exige requisição extra.

## Como aplicar

Por enquanto estudo: em pt-BR o AI Overview não é servido. Quando chegar, monitorar se o site do cliente é citado no resumo de IA para as perguntas do nicho dele.

## 💡 Edison diz

Boa ideia — a 3 é ruim, esquece a 3: só funciona em inglês, então para o cliente brasileiro ainda não acende. Fica na gaveta com etiqueta: 'quando o Google ligar o AI Overview em português, checar se o site do cliente aparece nas referências'. É uma ideia dormindo, não uma ideia morta.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Google AI Overview Results API

For some searches, Google search results includes an AI Overview block. SerpApi is able to scrape, extract and make sense of this information.

Currently, the AI Overview block is only seen for English searches (`hl=en`) with a limited range of countries (`gl`).

          The API endpoint is `https://serpapi.com/search?engine=google`
            

            Head to the playground for a live and interactive demo.
        

Google sometimes requires an additional request to retrieve AI Overview results. See the extra request example and our Google AI Overview API to understand how to handle these cases.

#### API Examples

##### Typical result

Typical result containing headings, paragraphs, lists (with and without title) and a thumbnail.

```
{
  ...
  "ai_overview": {
    "text_blocks": [
      {
        "type": "paragraph",
        "snippet": "Drop shipping is a retail model where an online store doesn't keep products in stock. When a customer buys something, the store orders it from a third-party supplier who then ships it directly to the customer. This allows businesses to operate without managing inventory or warehouse space, reducing initial investment and overhead.",
        "snippet_highlighted_words": [
          "a retail model where an online store doesn't keep products in stock"
        ],
        "reference_indexes": [
          0,
          1,
          3
        ]
      },
      {
        "type": "heading",
        "snippet": "Here's a more detailed breakdown:"
      },
      {
        "type": "list",
        "list": [
          {
            "title": "No Inventory:",
            "snippet": "Drop shippers sell products without holding any inventory themselves.",
            "reference_indexes": [
              1,
              3
            ]
          },
          {
            "title": "Third-Party Fulfillment:",
            "snippet": "They rely on a supplier (manufacturer, wholesaler, or another retailer) to handle warehousing, shipping, and fulfillment.",
            "reference_indexes": [
              2,
              3
            ]
          },
          {
            "title": "Forwarding Orders:",
            "snippet": "When a customer places an order, the drop shipper forwards it to their supplier, along with the shipping address.",
            "reference_indexes": [
              2,
              3
            ]
          },
          ...
        ]
      }
    ],
    "thumbnail": "https://serpapi.com/searches/66c53c7915afff0a2a48fc6c/images/ada462b58dfff08439da27aa82fde6c082293d76cc6e06be.png",
    "references": [
      {
        "title": "Drop shipping - Wikipedia",
        "link": "https://en.wikipedia.org/wiki/Drop_shipping",
        "snippet": "Drop shipping is a form of retail business in which the seller accepts customer orders without keeping stock on hand. Instead, in ...",
        "source": "Wikipedia",
        "index": 0
      },
      {
        "title": "Drop-Shipping: What you Need to Know Before You Buy or Sell Online",
        "link": "https://www.michigan.gov/consumerprotection/protect-yourself/consumer-alerts/shopping/before-you-buy-or-sell-online",
        "snippet": "What Is Drop-Shipping? Drop-shipping is when a person or company sells goods on their website that they do not keep in stock. When...",
        "source": "State of Michigan (.gov)",
        "index": 1
      },
      {
        "title": "What is Dropshipping: A Comprehensive Guide for ... - FedEx",
        "link": "https://www.fedex.com/en-us/small-business/articles-insights/what-is-drop-shipping.html#:~:text=Dropshipping%20is%20an%20online%20retail%20fulfillment%20method,the%20ordered%20products%20directly%20to%20the%20customer.",
        "snippet": "Dropshipping is an online retail fulfillment method where a store doesn't keep the products it sells in stock. Instead, when a sto...",
        "source": "FedEx",
        "index": 2
      },
      ...
    ]
  },
  ...
}
```
##### Example with a list containing thumbnails

```
{
  ...
  "ai_overview": {
    "text_blocks": [
      {
        "type": "heading",
        "snippet": "Here are some quotes about success:",
        "reference_indexes": [
          1
        ]
      },
      {
        "type": "list",
        "list": [
          {
            "title": "Albert Einstein",
            "thumbnail": "https://serpapi.com/searches/66c5457015afff0a2878cb08/images/4585b9266b87a391ef0f171532560347a6cfec61ff8315f797ba8afa9c0d9c8975178708294e51b8caa9fb8d67d58629.jpeg",
            "snippet": "\"Strive not to be a success, but rather to be of value\"",
            "reference_indexes": [
              1
            ]
          },
          {
            "title": "Nelson Mandela",
            "thumbnail": "https://serpapi.com/searches/66c5457015afff0a2878cb08/images/4585b9266b87a391ef0f171532560347a6cfec61ff8315f7e12a7180e6485d05cd19174a2fed3bc740822f57ec6aba42.jpeg",
            "snippet": "\"It always seems impossible until it's done\"",
            "reference_indexes": [
              1
            ]
          },
          {
            "title": "Herman Melville",
            "thumbnail": "https://serpapi.com/searches/66c5457015afff0a2878cb08/images/4585b9266b87a391ef0f171532560347a6cfec61ff8315f78333d67ec3a028c0a7884df42a0dba573a24740ee1f0fe89.jpeg",
            "snippet": "\"It is better to fail in originality than to succeed in imitation\"",
            "reference_indexes": [
              1,
              6
            ]
          },
          ...
        ]
      }
    ],
    "references": [
      {
        "title": "50 inspiring quotes about success",
        "link": "https://www.canva.com/learn/quotes-about-success/#:~:text=I%20find%20that%20the%20harder%20I%20work%2C,I%20seem%20to%20have.%20%E2%80%94%20Thomas%20Jefferson.",
        "snippet": "I find that the harder I work, the more luck I seem to have. — Thomas Jefferson.",
        "source": "Canva",
        "index": 0
      },
      {
        "title": "125 Motivational Success Quotes for Business - Team Building",
        "link": "https://teambuilding.com/blog/success-quotes",
        "snippet": "Sep 27, 2022 — What are some good success quotes for work? ... “Strive not to be a success, but rather to be of value.” – Albert Eins...",
        "source": "Team Building",
        "index": 1
      },
      {
        "title": "Life Quotes: 100+ Motivational Quotes To Inspire Your Positive ...",
        "link": "https://www.forbesindia.com/article/explainers/motivational-quotes/84853/1#:~:text=%22The%20only%20place%20where%20success%20comes%20before,and%20learning%20from%20failure.%22%20%E2%80%94%20Colin%20Powell",
        "snippet": "May 31, 2024 — \"The only place where success comes before work is in the dictionary.\" — Vince Lombardi; \"There are no secrets to succ...",
        "source": "Forbes India",
        "index": 2
      },
      ...
    ]
  },
  ...
}
```
##### Example with nested lists

```
{
  ...
  "ai_overview": {
    "text_blocks": [
      {
        "type": "paragraph",
        "snippet": "Drop shipping is a business model where a company sells products online without keeping them in stock. When a customer places an order, the company forwards the order and payment to a supplier or manufacturer, who then ships the product directly to the customer.",
        "snippet_highlighted_words": [
          "a business model where a company sells products online without keeping them in stock"
        ],
        "reference_indexes": [
          0,
          1,
          2
        ]
      },
      {
        "type": "heading",
        "snippet": "Here are some steps to start a dropshipping business:",
        "reference_indexes": [
          3
        ]
      },
      {
        "type": "list",
        "list": [
          {
            "snippet": "Choose a niche",
            "reference_indexes": [
              3
            ]
          },
          {
            "snippet": "Find a supplier: When choosing a supplier, you can consider things like:",
            "reference_indexes": [
              3,
              6
            ],
            "list": [
              {
                "snippet": "Profit margin: Whether the wholesale price is high enough to make a profit",
                "reference_indexes": [
                  6
                ]
              },
              {
                "snippet": "Handling fees: How these might affect your profit margin",
                "reference_indexes": [
                  6
                ]
              },
              {
                "snippet": "Shipping: Whether the supplier uses a service that provides tracking numbers",
                "reference_indexes": [
                  6
                ]
              },
              {
                "snippet": "Billing: Whether the supplier charges your credit card as soon as you submit an order",
                "reference_indexes": [
                  6
                ]
              }
            ]
          },
          {
            "snippet": "Build an online store",
            "reference_indexes": [
              3
            ]
          },
          ...
        ]
      },
      {
        "type": "paragraph",
        "snippet": "Some say that dropshipping can be a low-risk business model with lower running costs than other models. This can make it easier to become profitable faster, but the average dropshipper only makes between 10% and 30% compared to 50% to 70% for traditional e-commerce retailers.",
        "reference_indexes": [
          16,
          17
        ]
      }
    ],
    "references": [
      {
        "title": "What Is Dropshipping and How Does It Work? (2024) - Shopify",
        "link": "https://www.shopify.com/blog/what-is-dropshipping#:~:text=Dropshipping%20is%20a%20retail%20method,retail%20activities%20such%20as%20marketing.",
        "snippet": "May 22, 2024 — Dropshipping is a retail method where an online store doesn't keep its products in stock. Instead, when a customer mak...",
        "source": "Shopify",
        "index": 0
      },
      {
        "title": "Drop-Shipping: What you Need to Know Before You Buy or ...",
        "link": "https://www.michigan.gov/consumerprotection/protect-yourself/consumer-alerts/shopping/before-you-buy-or-sell-online#:~:text=Drop%2Dshipping%20is%20when%20a%20person%2C%20or%20company%2C,are%20middlemen%2C%20they%20may%20charge%20more%20money.",
        "snippet": "Drop-shipping is when a person, or company, sells goods on their website that they do not keep in stock. When an order is received...",
        "source": "State of Michigan",
        "index": 1
      },
      {
        "title": "Is Dropshipping Legal? A Guide to the Legal Risks (2024) - Shopify",
        "link": "https://www.shopify.com/blog/is-dropshipping-legal#:~:text=Yes%2C%20dropshipping%20is%20legal.,products%20directly%20to%20the%20customer.",
        "snippet": "Jun 17, 2024 — Yes, dropshipping is legal. It is a widely used business model in which a retailer does not keep the products it sells...",
        "source": "Shopify",
        "index": 2
      },
      ...
    ]
  },
  ...
}
```
##### Example with table

```
{
  ...
  "ai_overview": {
    "text_blocks": [
      ...
      {
        "type": "table",
        "table": [
          [
            "IrAE",
            "Description"
          ],
          [
            "Gastrointestinal",
            "Diarrhea, gastrointestinal bleeding, and enterocolitis"
          ],
          [
            "Pulmonary",
            "Pneumonitis"
          ],
          [
            "Hepatic",
            "Hepatitis"
          ],
          [
            "Endocrine",
            "Thyroid dysfunction"
          ],
          [
            "Dermatologic",
            "Rash, vitiligo, and alopecia"
          ]
        ],
        "detailed": [
          [
            {
              "snippet": "IrAE"
            },
            {
              "snippet": "Description"
            }
          ],
          [
            {
              "snippet": "Gastrointestinal"
            },
            {
              "snippet": "Diarrhea, gastrointestinal bleeding, and enterocolitis"
            }
          ],
          [
            {
              "snippet": "Pulmonary"
            },
            {
              "snippet": "Pneumonitis"
            }
          ],
          [
            {
              "snippet": "Hepatic"
            },
            {
              "snippet": "Hepatitis"
            }
          ],
          [
            {
              "snippet": "Endocrine"
            },
            {
              "snippet": "Thyroid dysfunction"
            }
          ],
          [
            {
              "snippet": "Dermatologic"
            },
            {
              "snippet": "Rash, vitiligo, and alopecia"
            }
          ]
        ],
        "formatted": [
          {
            "ir_ae": "Gastrointestinal",
            "description": "Diarrhea, gastrointestinal bleeding, and enterocolitis"
          },
          {
            "ir_ae": "Pulmonary",
            "description": "Pneumonitis"
          },
          {
            "ir_ae": "Hepatic",
            "description": "Hepatitis"
          },
          {
            "ir_ae": "Endocrine",
            "description": "Thyroid dysfunction"
          },
          {
            "ir_ae": "Dermatologic",
            "description": "Rash, vitiligo, and alopecia"
          }
        ]
      },
      ...
    ],
    ...
  },
  ...
}
```
##### 
    
      
    
    Example with `LaTeX` equations in the paragraph
  

  ```
{
  ...
  "ai_overview": {
    "text_blocks": [
      {
        "type": "paragraph",
        "snippet": "Assuming you want to solve the equation $x^{2}=0$, the solution is $\mathbf{x=0}$.",
        "snippet_latex": [
          "x^{2}=0",
          "\mathbf{x=0}"
        ]
      },
      {
        "type": "paragraph",
        "snippet": "To solve the equation $x^{2}=0$, you need to find the value of $x$ that, when multiplied by itself, equals zero. The only number that satisfies this condition is zero. $x^{2}=0$ $\sqrt{x^{2}}=\sqrt{0}$ $x=0$",
        "snippet_latex": [
          "x^{2}=0",
          "x",
          "x^{2}=0",
          "\sqrt{x^{2}}=\sqrt{0}",
          "x=0"
        ]
      }
    ]
  }
}
```
##### 
    
      
    
    Example with `LaTeX` equations in the table
  

  ```
{
  ...
  "ai_overview": {
    "text_blocks": [
      {
        "type": "paragraph",
        "snippet": "The root mean square (rms) velocity of hydrogen will double at a temperature of 819°C if the pressure remains unchanged:",
        "snippet_highlighted_words": [
          "819°C"
        ]
      },
      {
        "type": "table",
        "table": [
          [
            "Step",
            "Explanation"],
          [
            "1",
            "Let v_{1} be the rms velocity at standard temperature and pressure (S.T.P.)"],
          [
            "2",
            "Let v_{2} be the rms velocity at unknown temperature T_{2}"],
          ],
          ...
        ],
        "detailed": [
          [
            {
              "snippet": "Step"
            },
            {
              "snippet": "Explanation"
            }
          ],
          [
            {
              "snippet": "1"
            },
            {
              "snippet": "Let v_{1} be the rms velocity at standard temperature and pressure (S.T.P.)",
              "snippet_latex": [
                "v_{1}"
              ]
            }
          ],
          [
            {
              "snippet": "2"
            },
            {
              "snippet": "Let v_{2} be the rms velocity at unknown temperature T_{2}",
              "snippet_latex": [
                "v_{2}",
                "T_{2}"
              ]
            }
          ],
          ...
        ],
        "formatted": [
          {
            "step": "1",
            "explanation": "Let v_{1} be the rms velocity at standard temperature and pressure (S.T.P.)"
          },
          {
            "step": "2",
            "explanation": "Let v_{2} be the rms velocity at unknown temperature T_{2}"
          },
          ...
        ]
      }
    ],
    ...
  },
  ...
}
```
##### 
    
      
    
    Example with `LaTeX` equations in the list
  

  ```
{
  ...
  "ai_overview": {
    "text_blocks": [
      {
        "type": "paragraph",
        "snippet": "The root mean square (RMS) velocity of a gas doubles when the temperature of the gas quadruples. This is because the RMS velocity is directly proportional to the square root of the gas's temperature.",
        "snippet_highlighted_words": [
          "the RMS velocity is directly proportional to the square root of the gas's temperature"
        ]
      },
      {
        "type": "paragraph",
        "snippet": "Explanation"
      },
      {
        "type": "list",
        "list": [
          {
            "snippet": "The RMS velocity is the square root of the average of the squares of the speeds of each molecule in a gas."
          },
          {
            "snippet": "The RMS velocity is a key concept in understanding how gas molecules behave."
          },
          {
            "snippet": "The RMS velocity of a gas is directly proportional to the square root of the gas's temperature in Kelvin T.",
            "snippet_latex": [
              "T"
            ]
          },
          {
            "snippet": "This relationship can be expressed mathematically as v_{rms}\\propto \\sqrt{T}",
            "snippet_latex": [
              "v_{rms}\\propto \\sqrt{T}"
            ]
          },
          {
            "snippet": "To double the RMS velocity, the temperature must quadruple."
          }
        ]
      }
    ],
    ...
  },
  ...
}
```
##### Paragraph with video

```
{
  ...
  "ai_overview": {
    "text_blocks": [
      ...
      {
        "type": "paragraph",
        "snippet": "You can also watch this video to learn more about Android:",
        "video": {
          "link": "https://www.youtube.com/watch?v=Si2UR2gCq9M&t=92",
          "thumbnail": "https://i.ytimg.com/vi/Si2UR2gCq9M/mqdefault.jpg?sqp=-oaymwEGCPgEEOQC&rs=AMzJL3n0e0ap28VMcvonPp-z2mhM1Y6r5A",
          "source": "Google Open Source",
          "date": "Feb 9, 2023"
        }
      }
      ...
    ],
    ...
  },
  ...
}
```
##### Example with expandable sections

```
{
  ...
  "ai_overview": {
    "text_blocks": [
      {
        "type": "paragraph",
        "snippet": "Dropshipping is a retail model where an online store doesn't keep products in stock, but instead forwards orders to a supplier who then ships the products directly to the customer. This model is popular with business owners because it outsources inventory management and order fulfillment, and can be profitable with lower running costs than other business models.",
        "snippet_highlighted_words": [
          "a retail model where an online store doesn't keep products in stock, but instead forwards orders to a supplier who then ships the products directly to the customer"
        ],
        "reference_indexes": [
          0,
          4,
          7,
          11
        ]
      },
      {
        "type": "expandable",
        "title": "Starting a Dropshipping Business",
        "subtitle": "Steps for launching a dropshipping venture",
        "text_blocks": [
          {
            "type": "paragraph",
            "snippet": "Here are some steps to start a dropshipping business:"
          },
          {
            "type": "list",
            "list": [
              {
                "snippet": "Choose a business concept"
              },
              {
                "snippet": "Select products to sell"
              },
              {
                "snippet": "Choose suppliers"
              },
              {
                "snippet": "Build an online store"
              },
              {
                "snippet": "Register your business"
              },
              {
                "snippet": "Market your business and products",
                "reference_indexes": [
                  5
                ]
              }
            ]
          }
        ]
      },
      {
        "type": "expandable",
        "title": "Dropshipping Suppliers",
        "subtitle": "Examples of companies that offer dropshipping services",
        "text_blocks": [
          {
            "type": "paragraph",
            "snippet": "Some dropshipping suppliers include:"
          },
          {
            "type": "list",
            "list": [
              {
                "snippet": "Spocket"
              },
              {
                "snippet": "AliExpress Dropshipping"
              },
              {
                "snippet": "Modalyst"
              },
              {
                "snippet": "SaleHoo"
              },
              {
                "snippet": "Doba"
              },
              {
                "snippet": "Wholesale2B"
              },
              {
                "snippet": "Worldwide Brands",
                "reference_indexes": [
                  8
                ]
              }
            ]
          }
        ]
      },
      ...
    ],
    "thumbnail": "https://serpapi.com/searches/66c53cd315afff0a2878caf0/images/20fdf62b7cc11067c251b1374115d7a3e2082bff823672e8.png",
    "references": [
      {
        "title": "What Is Dropshipping and How Does It Work? (2024) - Shopify",
        "link": "https://www.shopify.com/blog/what-is-dropshipping#:~:text=Dropshipping%20is%20a%20retail%20method,the%20product%20to%20the%20customer.",
        "snippet": "May 22, 2024 — Dropshipping is a retail method where an online store doesn't keep its products in stock. Instead, when a customer mak...",
        "source": "Shopify",
        "index": 0
      },
      {
        "title": "Drop shipping - Wikipedia",
        "link": "https://en.wikipedia.org/wiki/Drop_shipping#:~:text=Amazon%2C%20the%20online%20shopping%20giant,customer%20using%20packaging%20from%20Amazon.",
        "snippet": "Amazon, the online shopping giant, found early success in a dropshipping business model where they could offer over a million diff...",
        "source": "Wikipedia",
        "index": 1
      },
      {
        "title": "What Is dropshipping? How does it work in 2024? - Sell on Amazon",
        "link": "https://sell.amazon.com/learn/what-is-dropshipping#:~:text=For%20Amazon%20sellers%2C%20using%20a,and%20identify%20yourself%20as%20such.",
        "snippet": "For Amazon sellers, using a dropshipping service is generally allowed by Amazon dropshipping policy, as long as you're the seller ...",
        "source": "Sell on Amazon",
        "index": 2
      },
      ...
    ]
  },
  ...
}
```
##### 
    
      
    
    Example of paragraph with `snippet_links`
  

  ```
  {
  ...
  "ai_overview": {
    "text_blocks": [
      {
        "type": "paragraph",
        "snippet": "Ruby is an open-source, dynamically typed, interpreted programming language that prioritizes simplicity and productivity. It's known for its elegant and readable syntax, making it relatively easy to learn and use. Ruby is often used for web development, particularly with the popular Ruby on Rails framework, but also finds applications in data analysis and other areas.",
        "snippet_highlighted_words": [
          "an open-source, dynamically typed, interpreted programming language that prioritizes simplicity and productivity"
        ],
        "snippet_links": [
          {
            "text": "Ruby on Rails",
            "link": "https://www.google.com/search?sca_esv=45c8bf4228d081b3&hl=en&gl=us&q=Ruby+on+Rails&sa=X&ved=2ahUKEwjU67mfy-yNAxUdCBAIHY9yECYQxccNegQICxAB"
          },
        ],
        "reference_indexes": [
          0,
          4,
          7,
          11
        ]
      },
      ...
    ],
    ...
  },
  ...
}
```
##### 
    
      
    
    Example of list with `snippet_links`
  

  ```
{
  ...
  "ai_overview": {
    "text_blocks": [
      ...
      {
        "type": "heading",
        "snippet": "Key Features:"
      },
      {
        "type": "list",
        "list": [
          {
            "title": "Object-Oriented:",
            "link": "https://www.google.com/search?sca_esv=abfa54d360d79d5a&hl=en&gl=us&q=Object-Oriented&sa=X&ved=2ahUKEwjghIb87JGOAxXrhlYBHRcUAIgQxccNegQIPxAD",
            "snippet": "Everything in Ruby is treated as an object, with features like single inheritance, mixins, and metaclasses.",
            "snippet_links": [
              {
                "text": "metaclasses",
                "link": "https://www.google.com/search?sca_esv=abfa54d360d79d5a&hl=en&gl=us&q=metaclasses&sa=X&ved=2ahUKEwjghIb87JGOAxXrhlYBHRcUAIgQxccNegQIPhAB"
              }
            ],
            "reference_indexes": [
              1
            ]
          },
          {
            "title": "Dynamic Typing:",
            "link": "https://www.google.com/search?sca_esv=abfa54d360d79d5a&hl=en&gl=us&q=Dynamic+Typing&sa=X&ved=2ahUKEwjghIb87JGOAxXrhlYBHRcUAIgQxccNegQIQBAD",
            "snippet": "You don't need to declare the data type of a variable, making it more flexible.",
            "reference_indexes": [
              1,
              16
            ]
          },
         ...
        ],
      },
    }
  ...
}
```
##### 
    
      
    
    Example with `top_stories`
  

  ```
{
  ...
  "ai_overview": {
    "text_blocks": [
      ...
      {
        "type": "top_stories",
        "top_stories": [
          {
            "title": "U.S.-Iran Latest: Slow progress on peace deal as Iran strikes ship in Strait of Hormuz, Hezbollah balks at disarming",
            "link": "https://www.cbsnews.com/live-updates/us-iran-war-israel-hezbollah-strait-of-hormuz-peace-deal-talks/",
            "source": "CBS News",
            "live": true,
            "date": "2 hours ago",
            "thumbnail": "https://serpapi.com/searches/6a429b2bce4eb0531889e4e0/images/GkVXQbx2QkZcLydxjY7mHGw-BnSLgxXyjMAL9VyEUnp4JStP1iBIoG2Nyx4sGVB4yQHcboDI8rA28dGLf8TvEg.jpeg",
            "source_icon": "https://serpapi.com/images/i/iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAARVBMVEX___8hISEAAAASEhIfHx8gICCjo6MICAiAgIChoaGurq7Nzc21tbV5eXl2dnaFhYXz8_OXl5fp6ekyMjJJSUkvLy8VFRW_1GjAAAAAeElEQVQYlWWP2w7DIAxDjQOhtIXe9_-fugVaaRV-QNEhThw4k5cYxdcS9lAG1UF4g8CEKmWogBNuTTRABeacNM_W4-AFuy_2n90O8ZBl5dEcB9dFEMeTWwMbzzH2wCzXv8V_nqEl1KFtbUnpWdsH-0XXd_TuuPf5X0N7BEhK7acFAAAAAElFTkSuQmCC.png"
          },
          {
            "title": "Iran war live: Iran says Hormuz transit only via Tehran-approved routes",
            "link": "https://www.aljazeera.com/news/liveblog/2026/6/26/iran-war-live-israel-attacks-lebanon-as-netanyahu-says-troops-to-stay",
            "source": "Al Jazeera",
            "live": true,
            "date": "1 hour ago",
            "thumbnail": "https://serpapi.com/searches/6a429b2bce4eb0531889e4e0/images/GkVXQbx2QkZcLydxjY7mHGw-BnSLgxXyjMAL9VyEUnrMaZHNd_mR0q49wYUUkx3vRlCwZ25s6HcPueqJAyReCg.jpeg",
            "source_icon": "https://serpapi.com/images/i/iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAjVBMVEX6kAD6jgD6iwD6hgD6igD6lAD6kwv7qT_8yJj5gQD-69T7rWb7pEX-7M_8uWv-59H8yI392q_8v377q139zqD8xHv8vYD8xZH8uXj8wov7tXH7s2j927X90rL7pTv8xob8tFn92bv7qkn90pz-7N3-8uv5dAD8y6X7p038vHH___j7oj_-4cb-8t_6mRyYFfs_AAAAhUlEQVQYlV2PyxqCIBhE-bkkmooWWZiYUnS393-8NkDQ7OZ8ZzGDkAugNKvsjzBOkw55sY4VKKta4AiQpt1sBfl1KXfd_qC8g9u-rI5MDF7BejxNZJaGO4UOTXeW4yXXAVi2XO3tPjsAtZlMIR9Pvx9e70VxpT9hGkAmrWHxVKp6nL4L9Qs4Pweb-cI-egAAAABJRU5ErkJggg.png"
          },
          {
            "title": "Mediators worked through threats and strikes to broker the US-Iran deal, and challenges remain",
            "link": "https://www.washingtonpost.com/world/2026/06/26/us-iran-war-mediation-peace-deal-pakistan-qatar/b972401a-715b-11f1-8730-e7fd0e2a6404_story.html",
            "source": "The Washington Post",
            "date": "9 minutes ago",
            "thumbnail": "https://serpapi.com/searches/6a429b2bce4eb0531889e4e0/images/GkVXQbx2QkZcLydxjY7mHGw-BnSLgxXyjMAL9VyEUnphGB24sqrYxM6Y-Gfn8XXhJlHA6AtsaImWBj0QEkDF_w.jpeg",
            "source_icon": "https://serpapi.com/images/i/iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAZlBMVEX___8AAACrq6v39_fHx8d0dHTj4-PMzMzR0dHa2tq5ubnw8PA1NTXn5-ft7e2enp5NTU2Dg4NSUlIaGhpiYmJ8fHzAwMCwsLBHR0coKCiUlJQICAgTExOkpKQxMTGOjo5ra2tAQECDU3esAAAAgUlEQVQYlYXP7Q7CIAwF0F4LjI3BxIkfTKZ7_5dc8R-LiU2TNidp2hL9jzAd4BwPUNDDdGAP2y-DQAd1EdM8X1WCwA3uDhoTz9pIQx4IJ4H4gDbSEFu4ClryC6TgpT5zhTpCbsGAV6GMiPVd9_JEoRCXMWXVHLR-THvhZn0L_PvXHWUHBNCK7AF_AAAAAElFTkSuQmCC.png"
          },
          ...
        ],
      },
      ...
    ],
  },
  ...
}
```
##### Example with products comparison

```
{
  ...
  "ai_overview": {
    "products": [
      {
        "thumbnail": "https://serpapi.com/searches/68496f27fe1c6b10a13f4f91/images/b92ecfbc4c7deb844c133ac2aa0d6589d046597f475651f4be1e3f20de8d3d970262af7ad7baaba8.webp",
        "title": "Apple iPhone 16",
        "rating": "4.7",
        "reviews": "10K",
        "price": "$0",
        "extracted_price": 0,
        "installments": "• $22mo × 36"
      },
      {
        "thumbnail": "https://serpapi.com/searches/68496f27fe1c6b10a13f4f91/images/b92ecfbc4c7deb844c133ac2aa0d6589cd7413b35b3b2365df59602a18b3d20f68811ceeae1f2621.webp",
        "title": "Apple iPhone 15",
        "rating": "4.7",
        "reviews": "28K",
        "price": "$0",
        "extracted_price": 0,
        "installments": "• $29mo × 24"
      }
    ],
    "text_blocks": [
      {
        "type": "paragraph",
        "snippet": "The iPhone 16 has a more vibrant pink color than the iPhone 15. The iPhone 16 also features an action button, camera control, and fast charging. The iPhone 15 features a Dynamic Island and USB-C charging.",
        "reference_indexes": [
          0,
          1,
          4,
          14,
          13,
          16,
          17
        ]
      },
      {
        "type": "expandable",
        "title": "Camera",
        "text_blocks": [
          {
            "type": "paragraph",
            "snippet": "The iPhone 16 and iPhone 15 have the same front and rear camera resolution, lens types, and digital zoom."
          },
          {
            "type": "paragraph",
            "snippet": "The iPhone 16 features an advanced dual-camera system with a TrueDepth camera. The iPhone 15 also features a dual-camera system, and its camera improvements are often made possible by software solutions like machine learning.",
            "reference_indexes": [
              5,
              6,
              12,
              13
            ]
          },
          {
            "type": "comparison",
            "product_labels": [
              "Apple iPhone 16",
              "Apple iPhone 15"
            ],
            "comparison": [
              {
                "feature": "Front camera resolution",
                "values": [
                  "12 MP",
                  "12 MP"
                ]
              },
              {
                "feature": "Rear camera resolution",
                "values": [
                  "48 MP",
                  "48 MP"
                ]
              },
              {
                "feature": "Lens type",
                "values": [
                  "Ultra wide angle, telephoto",
                  "Ultra wide angle, telephoto"
                ]
              },
              ...
            ]
          }
        ]
      },
      {
        "type": "expandable",
        "title": "Design",
        "text_blocks": [
          {
            "type": "paragraph",
            "snippet": "The iPhone 16 and iPhone 15 have the same height, width, and depth.",
            "reference_indexes": [
              5,
              6
            ]
          },
          {
            "type": "paragraph",
            "snippet": "The iPhone 16 features a color-infused glass back in pink, teal, ultramarine, and black. The iPhone 15 also features a color-infused glass back in pink, blue, green, yellow, and black.",
            "reference_indexes": [
              5,
              6
            ]
          },
          {
            "type": "comparison",
            "product_labels": [
              "Apple iPhone 16",
              "Apple iPhone 15"
            ],
            "comparison": [
              {
                "feature": "Height",
                "values": [
                  "5.81 inches",
                  "5.81 inches"
                ]
              },
              {
                "feature": "Width",
                "values": [
                  "2.82 inches",
                  "2.82 inches"
                ]
              },
              {
                "feature": "Depth",
                "values": [
                  "0.31 inches",
                  "0.31 inches"
                ]
              },
              ...
            ]
          }
        ]
      },
      ...
    ],
    "references": [
      {
        "title": "Pink Apple iPhone 16 Plus vs iPhone 15 Plus Unboxing ... - Instagram",
        "link": "https://www.instagram.com/superscientific/reel/DAJ71gcSAKn/?hl=en#:~:text=The%20iPhone%2016%20definitely%20has%20the%20more,going%20for%20the%20iPhone%2016%20Pro%20Max?",
        "snippet": "Sep 20, 2024 — The iPhone 16 definitely has the more vibrant pink color but the baby pink iPhone 15 also looks good. The Google Pixel...",
        "source": "Instagram · superscientific",
        "index": 0
      },
      {
        "title": "Pink Apple iPhone 16 Plus vs iPhone 15 Plus Unboxing ... - Instagram",
        "link": "https://www.instagram.com/superscientific/reel/DAJ71gcSAKn/#:~:text=15%20Plus%20Unboxing!-,Which%20smartphone%20has%20the%20better%20Pink?,I%20had%20to%20compare%20them.",
        "snippet": "Sep 20, 2024 — Which smartphone has the better Pink? The iPhone 16 definitely has the more vibrant pink color but the baby pink iPhon...",
        "source": "Instagram",
        "index": 1
      },
      {
        "title": "Iphone 16 vs 15 plus, which one to buy? : r/iphone15 - Reddit",
        "link": "https://www.reddit.com/r/iphone15/comments/1gn3qng/iphone_16_vs_15_plus_which_one_to_buy/",
        "snippet": "Nov 9, 2024 — The 16 was much more expensive. Besides, I also liked the colors of 15 more, the pink 16 made me feel nauseous (literal...",
        "source": "Reddit · r/iphone15",
        "index": 2
      },
      ...
    ]
  },
  ...
}
```
##### Example with an extra request required

Google can return AI Overview content through a separate request instead of directly in a response. In these cases we return `page_token` for the associated request and `serpapi_link` for the corresponding SerpApi search using our Google AI Overview API. The resulting JSON structure is the same as the above examples.

The rendered HTML will show "Can't generate an AI overview right now. Try again later." — this is expected behaviour and can be ignored.`page_token` and `serpapi_link` will expire within 4 minutes of the search and should be used immediately.

```
{
  ...
  "ai_overview": {
    "page_token": "rWmjgXictZPdkqI4FMcv90nWvWBUtO0e7SpqKiBqHL8ifuENhRADgnwFjHo377JPtU-zAdtunXFqZ6t2U6UkOTkn55xf_t_-9N3A--u3P5w0jehrtcoYq5AwJD6uWOG-atJTYFW3oU8Ty_mSZT6WmKAAiKACTbRanO2unw06Ux93O-dBZ5GZq6m_VuSZ3e2I69WwRHwpoyXHl3BQOh2kp5JFJbGEXSlmm5d1loDu-Ox5BzRxrHY5BGGpuFEyNibFO57QcUerRpX_eb8_tfmiQis4MOZaRYsmSdzw-119WMH0uTKumnt-BPziQB9TRSFIKWYQKHeHyPtpBchAA0QuVj3-U6dFCAigcnHyEDgYTfXO3wJva9nKo80vt0IA2nc5kHzr0ZB5o9vNB4nLBIEuT6RRbF0uQXmQBgTD99JYTwTN9pGMv2rsh9gRIHsw0VbH2zo_Ku8vd65FVKCgqk14X8XqJuGfWjWheZeVWUsMO3F9uNTMZrpqiu3M7kCViaNa92W3mKJPBUGLviOktwihGwf2aD0-U1YZVOTalR7qQagW3VAJICJ51BcFfXROyXMnIPR4fWTA8t6OinJ6-YbFG6Nf3bSrw_KjXD5RYE6PqPBqzvuaD5g3VB0C4HAMQIacnkZ6jTk3tYsAyAO6LrsgBF8BWDPl5ulAcrmjcXlQKsD8hbGhvFKZChB_RQh4edSCHIJyXhAaMvWOXlHoP4z5T_Zl8ABXV1_EZXdAengab2akpZ2yaLJbOGc0vuIK95t_JTnrf0HqckHGb0iVx0hvBMkdVtz-JsiQC_KC1NMLQd4htaD6htS6QQp_GakMGnq7_AgpF-QeyFyQOdJ5gRTp3yP9rwRZkMWXz706sx35HruqlkeeU4u9ujwD09MzEeOTZcv0qCUc-3afvkZJSD4Zrv0q1_vpyS7FUi9kgh1iKqQOFrQoTFLKsJkI_IFEZnASRq6Hha3p-wJ1uFEIA4EG2PRwIriBMA_cFNuClpoppl9Kez8JJdF8YYd4pKvePGUG7O_Ugb8sPwf-4uwaT9vjYVSvRb10arx8Xs2i3uzZH_WV5SrIlL4xaTlKH4VqbwyDhOygbY1OmaqjxdA9U9dtmed2f6e7x3lnvWZav564IjvPxvt6013TcmO8Ao0BMpA8D7F23srrGvDnNivyopLeXWTQ6SxbC1SilmlgepDqm-Zn88ls1uubzab21CwMWXSQan8DmsQweA",
    "serpapi_link": "https://serpapi.com/search.json?engine=google_ai_overview&page_token=rWmjgXictZPdkqI4FMcv90nWvWBUtO0e7SpqKiBqHL8ifuENhRADgnwFjHo377JPtU-zAdtunXFqZ6t2U6UkOTkn55xf_t_-9N3A--u3P5w0jehrtcoYq5AwJD6uWOG-atJTYFW3oU8Ty_mSZT6WmKAAiKACTbRanO2unw06Ux93O-dBZ5GZq6m_VuSZ3e2I69WwRHwpoyXHl3BQOh2kp5JFJbGEXSlmm5d1loDu-Ox5BzRxrHY5BGGpuFEyNibFO57QcUerRpX_eb8_tfmiQis4MOZaRYsmSdzw-119WMH0uTKumnt-BPziQB9TRSFIKWYQKHeHyPtpBchAA0QuVj3-U6dFCAigcnHyEDgYTfXO3wJva9nKo80vt0IA2nc5kHzr0ZB5o9vNB4nLBIEuT6RRbF0uQXmQBgTD99JYTwTN9pGMv2rsh9gRIHsw0VbH2zo_Ku8vd65FVKCgqk14X8XqJuGfWjWheZeVWUsMO3F9uNTMZrpqiu3M7kCViaNa92W3mKJPBUGLviOktwihGwf2aD0-U1YZVOTalR7qQagW3VAJICJ51BcFfXROyXMnIPR4fWTA8t6OinJ6-YbFG6Nf3bSrw_KjXD5RYE6PqPBqzvuaD5g3VB0C4HAMQIacnkZ6jTk3tYsAyAO6LrsgBF8BWDPl5ulAcrmjcXlQKsD8hbGhvFKZChB_RQh4edSCHIJyXhAaMvWOXlHoP4z5T_Zl8ABXV1_EZXdAengab2akpZ2yaLJbOGc0vuIK95t_JTnrf0HqckHGb0iVx0hvBMkdVtz-JsiQC_KC1NMLQd4htaD6htS6QQp_GakMGnq7_AgpF-QeyFyQOdJ5gRTp3yP9rwRZkMWXz706sx35HruqlkeeU4u9ujwD09MzEeOTZcv0qCUc-3afvkZJSD4Zrv0q1_vpyS7FUi9kgh1iKqQOFrQoTFLKsJkI_IFEZnASRq6Hha3p-wJ1uFEIA4EG2PRwIriBMA_cFNuClpoppl9Kez8JJdF8YYd4pKvePGUG7O_Ugb8sPwf-4uwaT9vjYVSvRb10arx8Xs2i3uzZH_WV5SrIlL4xaTlKH4VqbwyDhOygbY1OmaqjxdA9U9dtmed2f6e7x3lnvWZav564IjvPxvt6013TcmO8Ao0BMpA8D7F23srrGvDnNivyopLeXWTQ6SxbC1SilmlgepDqm-Zn88ls1uubzab21CwMWXSQan8DmsQweA"
  },
  ...
}
```
##### 
    
      
    
    Example of `header_images` in AI Overview
  

  ```
{
  ...
  "ai_overview": {
    ...
    "header_images": [
      {
        "image": "https://serpapi.com/searches/69fa39adfc8a2b7c19e3eba0/images/ERo1aEunycf4bXVO1wFUrAeEW5gnKaRXfLiWFUbo_OFauDJQ2KzUSUBcvl_DxZwG.jpeg",
        "source": "https://www.reddit.com/r/skyscrapers/comments/1ehvjf8/worlds_tallest_buildings_with_spire_vs_without/"
      },
      {
        "image": "https://serpapi.com/searches/69fa39adfc8a2b7c19e3eba0/images/ERo1aEunycf4bXVO1wFUrJvcmPLk4TdMbvBcJUsn33FioJNbK5A45fv5MtWKMcYY.jpeg",
        "source": "https://www.britannica.com/topic/Burj-Khalifa"
      },
      {
        "image": "https://serpapi.com/searches/69fa39adfc8a2b7c19e3eba0/images/ERo1aEunycf4bXVO1wFUrH9ncmejXi2gZjTL0IFg8gXI8ZZkfyUhQqI4OZtCGCx0.jpeg",
        "source": "https://learningenglish.voanews.com/a/where-are-the-top-ten-tallest-buildings-in-the-world/3809420.html"
      },
      {
        "image": "https://serpapi.com/searches/69fa39adfc8a2b7c19e3eba0/images/ERo1aEunycf4bXVO1wFUrBe54T9lhoCiZs8NuVSRPDsDjw7nYaiDzSu2021mKrLK.jpeg",
        "source": "https://www.voronoiapp.com/real-estate/The-Worlds-Tallest-Buildings-in-2024--2107"
      },
      {
        "image": "https://serpapi.com/searches/69fa39adfc8a2b7c19e3eba0/images/ERo1aEunycf4bXVO1wFUrDsFcxoxOLhwqKf2cE3ryzefZzgzCedd6SYJM27Me29P.jpeg",
        "source": "https://www.bbc.co.uk/newsround/articles/c80z22pgglyo"
      }
    ]
  ...
}
```
##### JSON structure overview

```
{
  ...
  "ai_overview": {
    // When separate request is required for the AI Overview content
    "page_token": "String - Token for the AI Overview block",
    "serpapi_link": "String - URL to the corresponding SerpApi search",
    // When the AI Overview block includes products
    "products": [
      {
        "thumbnail": "String - URL to the product thumbnail image",
        "title": "String - Title of the product",
        "rating": "String - Product rating",
        "reviews": "String - Number of reviews for the product",
        "price": "String - Price of the product",
        "extracted_price": "Number - Extracted price value from the product",
        "installments": "String - Installment information for the product"
      },
      ...
    ],
    // When the AI Overview block is embedded in the search results
    "text_blocks": [
      {
        "type": "String - Type of the text block. Can be 'heading', 'paragraph', 'list', 'expandable', or 'comparison'",
        "snippet": "String - Snippet of the text block",
        "snippet_latex": "Array of strings - LaTeX equations in the snippet",
        "snippet_highlighted_words": "Array of strings - Highlighted words in the snippet",
        "snippet_links": {
          "text": "String - Text content of inline link",
          "link": "String - URL of inline link",
        },
        "reference_indexes": "Array of integers - Indexes of the references in the root 'references' field",
        "thumbnail": "String - URL to the thumbnail image",
        "video": {
          "link": "String - URL to the video",
          "thumbnail": "String - URL to the thumbnail image",
          "source": "String - Source of the video",
          "date": "String - Date of the video"
        },
        // Only for 'list' type
        "list": [
          {
            "title": "String - Title of the list item",
            "link": "String - Link URL of the list item title",
            "snippet": "String - Snippet of the list item",
            "snippet_latex": "Array of strings - LaTeX equations in the snippet",
            "reference_indexes": "Array of integers - Indexes of the references in the root 'references' field",
            "thumbnail": "String - URL to the thumbnail image",
            // Nested lists
            "list": [
              {
                "snippet": "String - Snippet of the nested list item",
                "reference_indexes": "Array of integers - Indexes of the references in the root 'references' field",
              },
              ...
            ]
          },
          ...
        ],
        // Only for `table` type
        "table": [
          [
            "String - Table cell snippet",
            ...
          ],
          ...
        ],
        "detailed": [
          [
            {
              "snippet": "String - Table cell snippet",
              "snippet_latex": "Array of strings - LaTeX equations in the snippet"
            },
            ...
          ],
          ...
        ],
        "formatted": "Array or Object, depending on the structure of the table - Formatted table data",
        // Only for 'expandable' type
        "text_blocks": [
          // The same structure as the parent 'text_blocks' field
        ],
        // Only for 'comparison' type
        "product_labels": "Array of strings - Labels for the products being compared",
        "comparison": [
          {
            "feature": "String - Feature being compared",
            "values": [
              "String - Value for the first product",
              "String - Value for the second product"
            ]
          },
          ...
        ]
      },
      {
        "type": "top_stories",
        "top_stories": [
          {
            "title": "String - Title of the top story",
            "link": "String - URL to the top story",
            "source": "String - Source of the top story",
            "live": "Boolean - Whether the top story is live",
            "date": "String - Date of the top story",
            "thumbnail": "String - URL to the thumbnail image of the top story",
            "source_icon": "String - URL to the source icon of the top story"
          },
          ...
        ],
      },
      ...
    ],
    "thumbnail": "String - URL to the thumbnail image",
    "header_images": [
      {
        "image": "String - URL to the header image",
        "source": "String - URL to the source page of the header image"
      },
      ...
    ],
    "references": [
      {
        "title": "String - Title of the reference",
        "link": "String - URL to the reference",
        "snippet": "String - Snippet of the reference",
        "source": "String - Source of the reference",
        "index": "Integer - Index of the reference"
      },
      ...
    ],
    "error": "String - Error message if the AI Overview results are not available",
  },
  ...
}
```

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
