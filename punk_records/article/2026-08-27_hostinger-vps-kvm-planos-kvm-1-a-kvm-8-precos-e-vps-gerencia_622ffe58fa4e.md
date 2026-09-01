---
item_id: "4e7795d9-2e66-46c8-bcea-87b4cce92e8a"
platform: article
external_id: "622ffe58fa4e"
canonical_url: "https://www.hostinger.com/br/precos/vps-hosting"
channel: "Hostinger"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["hostinger", "vps", "kvm", "precos", "docker", "n8n", "mcp", "infraestrutura"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Hostinger VPS KVM — planos (KVM 1 a KVM 8), preços e VPS gerenciado por IA

🔗 https://www.hostinger.com/br/precos/vps-hosting

## Resumo

Página de preços de VPS da Hostinger. Planos KVM com preço mensal informado na FAQ: KVM 1 R$ 29,99, KVM 2 R$ 43,99 (2 vCPUs, 8 GB RAM, 100 GB NVMe — recomendado para n8n), KVM 4 R$ 59,99, KVM 8 R$ 119,99. Todos com acesso root, IP dedicado, backups semanais grátis, servidores em vários países, hardware Dell/HPE com AMD EPYC e NVMe, mitigação DDoS, firewall com IA e scanner de malware. Diferencial anunciado: 'VPS gerenciado por IA' — um assistente integrado via MCP que executa tarefas no servidor (Docker, monitoramento, firewall) por linguagem natural, sem custo extra; há API pública e um servidor MCP da Hostinger para conectar Claude ou Cursor ao VPS. Casos de uso listados: sites grandes, aplicações e APIs, servidores de jogos, n8n, LLMs locais com Ollama. Diferença para cloud: cloud é gerenciada pela Hostinger sem acesso ao servidor; VPS é autogerenciado com root e templates de SO com painéis (cPanel, Plesk, CyberPanel, DirectAdmin) em um clique. Upgrade pelo painel.

## Tópicos

- **Planos e preços** — KVM 1 R$ 29,99 · KVM 2 R$ 43,99 (2 vCPU, 8 GB, 100 GB) · KVM 4 R$ 59,99 · KVM 8 R$ 119,99, por mês.
- **Infra e segurança** — KVM isolado, Dell/HPE, AMD EPYC, NVMe, IP dedicado, DDoS, firewall com IA, scanner de malware, backups semanais.
- **VPS gerenciado por IA e API** — Assistente via MCP executa tarefas (Docker, monitoramento, configs); API pública e servidor MCP para Claude/Cursor.
- **VPS vs cloud** — Cloud é gerenciada sem acesso ao servidor; VPS é autogerenciado com root, templates de SO e painéis.

## Ferramentas citadas

- **KVM**: virtualização usada em todos os planos VPS
- **Hostinger MCP server**: conecta Claude/Cursor ao VPS pela API pública
- **n8n**: automação citada como caso de uso do KVM 2
- **Ollama**: LLM local como caso de uso de VPS
- **cPanel / Plesk / CyberPanel / DirectAdmin**: painéis compatíveis

## Pontos-chave

- KVM 2 (R$ 43,99/mês) é o ponto de entrada realista para Docker + n8n ou um SaaS pequeno; KVM 1 para testes.
- Acesso root e IP dedicado em todos os planos; backups semanais inclusos (diários não).
- Assistente de IA e API pública sem custo adicional — dá para administrar o servidor via Claude Code por MCP.
- VPS é autogerenciado: atualizações e segurança do SO são responsabilidade sua.
- Cloud gerenciada é a alternativa sem administração, mas sem root.

## Como aplicar

Candidato natural para hospedar o SaaS (e o próprio Vegapunk) fora da máquina local: KVM 2 com Docker Compose. Antes: York *roi comparando R$ 43,99/mês com o custo de ficar local; Shaka *risk sobre backup só semanal.

## 🍩 York diz

Esse tem número na cara, gosto. KVM 2: R$ 43,99 por mês, R$ 528 por ano, e roda Docker com o Vegapunk inteiro e um SaaS pequeno — é um jantar por mês. O que eu cobro: backup só semanal, então o Punk Records continua indo pro GitHub todo dia. E o assistente de IA 'grátis' me cheira a upsell futuro; usa, mas não depende.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Planos e preços

30 dias para pedir reembolso

Suporte 24h

Cancele a qualquer momento

##### Cada plano tem **tudo o que você precisa** e muito mais

**Servidores**em várias partes do mundo

**semanais grátis**

**Servidores**em várias partes do mundo

**semanais grátis**

#### Perguntas Frequentes (FAQ) sobre os planos da Hostinger

##### O que é um VPS e para que ele serve?

A virtual private server (VPS) is a type of hosting that provides an isolated environment with its own software, configuration, data, and resources, including CPU, RAM, storage, and bandwidth.

Unlike a dedicated server, a VPS operates as a virtual machine running on top of a physical host using virtualization technology. It works like traditional web hosting but with full root access and a significantly higher level of isolation, which provides better flexibility and reliability.

Combining the best of both worlds, a VPS is ideal for web professionals who want a high-performance hosting solution without the hassle of managing a physical server. It also caters to a vast range of user needs, such as, but not limited to:

- **Website hosting.** Host different types of websites, including large online stores built on platforms like PrestaShop, Magento, or WordPress.
- **Software application hosting.** Use a control panel, containerization software, or a framework to deploy various applications, such as databases, analytics platforms, customer relationship management apps, and more.
- **Game server.** Launch a private multiplayer server for online games like Minecraft or Counter-Strike.
- **Workflow automation.** Deploy n8n to connect various applications and create a custom workflow for automatic data processing, all on a centralized dashboard
- **Personal large language models or AI agents.** Run and tune personal large language models with Ollama, or host custom ChatGPT to assist you with specific tasks.

For more information, check out our complete guide on virtual private servers.

##### O que é um VPS gerenciado por IA?

O VPS gerenciado por IA é uma nova categoria de hospedagem que combina o controle total do servidor com o gerenciamento inteligente integrado. Trata-se de um VPS autogerenciado com poder de IA, capaz de executar operações reais no seu servidor, indo muito além de simples sugestões.

Integrada via Model Context Protocol (MCP), a IA da Hostinger se conecta diretamente à infraestrutura do seu servidor e ao painel de controle. Basta descrever o que você precisa em linguagem natural para que a IA resolva problemas, gerencie contêineres Docker, monitore recursos e configure políticas de segurança — tudo isso sem exigir comandos complexos ou conhecimento avançado de administração de sistemas.

Aproveite o poder e a flexibilidade de um VPS com a simplicidade da gestão por IA, sem custo adicional.

##### O que é KVM? Quais são suas vantagens?

Uma máquina virtual baseada em Kernel (KVM) é uma solução de virtualização completa que divide um servidor físico em ambientes virtuais totalmente isolados e independentes. Na Hostinger, essa tecnologia é a base de todos os nossos planos de VPS.

Diferente de outros tipos de virtualização, o KVM garante o máximo nível de isolamento, estabilidade e personalização — a escolha ideal para projetos de desenvolvimento que exigem alto desempenho e flexibilidade.

Com a hospedagem VPS KVM, você tem autonomia total para personalizar o sistema operacional, o painel de controle e a arquitetura de software da sua aplicação. Enquanto você gerencia o seu servidor virtual, nós cuidamos da infraestrutura física para garantir alta velocidade, estabilidade e disponibilidade (uptime).

Nossos servidores KVM são construídos com hardware de ponta Dell e HPE, armazenamento SSD NVMe ultrarrápido e processadores AMD EPYC. Essa combinação entrega performance máxima e baixíssima latência para suas aplicações.

##### Por que escolher um servidor VPS? Quando devo fazer upgrade para um VPS?

A hospedagem VPS é ideal para **projetos em expansão ou de alta complexidade**, como aplicações web, APIs, servidores de jogos, ambientes WordPress multisite e aplicações de alta demanda. O VPS garante **CPU, RAM e armazenamento dedicados**, além de autonomia total para configurar o servidor e o sistema operacional.

Em comparação com a hospedagem de sites tradicional, o VPS entrega **mais desempenho, estabilidade e flexibilidade** para acompanhar o crescimento da sua estrutura.

Com o **VPS gerenciado por IA**, você combina esse poder computacional com um assistente capaz de **executar tarefas reais de gerenciamento no servidor**. Basta usar linguagem natural para solucionar falhas, gerenciar contêineres Docker, monitorar métricas e ajustar configurações — tudo sem exigir conhecimento avançado de administração de sistemas.

O upgrade para o VPS é recomendado quando a hospedagem compartilhada ou a hospedagem gerenciada deixarem de suprir suas necessidades, ou quando você buscar mais controle com simplicidade. Se este for seu primeiro servidor virtual, a gestão por IA facilita a rotina diária sem abrir mão do controle total.

Para fazer upgrade do seu plano de VPS, basta acessar o painel da Hostinger e clicar em **Fazer Upgrade**.

##### Os servidores virtuais privados baseados em KVM são seguros?

Sim, nossa hospedagem VPS foi desenvolvida com foco total em segurança. O isolamento de servidores garante o mais alto nível de proteção, combinado com mitigação avançada contra ataques DDoS e um firewall inteligente movido a IA para proteger a infraestrutura.

Além disso, cada plano VPS KVM inclui um IP dedicado, permitindo configurar regras de segurança personalizadas, como restrições e políticas de firewall exclusivas para o seu IP.

Para reforçar a proteção, você conta com um scanner de malware integrado que detecta e remove arquivos maliciosos de forma automática.

##### Posso instalar um software personalizado no meu servidor VPS?

Sim. Com acesso root completo, você pode instalar e configurar **qualquer software personalizado** no seu VPS — de aplicações e APIs de alta demanda a ambientes Docker, fluxos de automação e modelos de IA locais.

Com o **VPS gerenciado por IA**, você mantém o controle total enquanto usa a inteligência artificial para **simplificar a gestão diária do servidor**. Basta solicitar à IA para solucionar falhas, gerenciar contêineres Docker, monitorar recursos ou ajustar configurações, sem precisar executar comandos manualmente.

Também é possível gerenciar seu servidor através dos principais painéis do mercado, como **cPanel, Plesk, CyberPanel e DirectAdmin**, todos compatíveis com nossos planos de VPS.

E para acelerar a sua implantação, nossos **templates de SO Linux** já vêm pré-configurados com painéis e softwares instalados em um único clique, entregando um ambiente de servidor pronto para uso em poucos minutos.

##### Quanto custa um servidor VPS? Como escolher o plano VPS certo para minhas necessidades?

Nossos planos de hospedagem VPS KVM variam de **R$ 29,99 a R$ 119,99/mês**:

- KVM 1 – **R$ 29,99/mês**
- KVM 2 – **R$ 43,99/mês**
- KVM 4 – **R$ 59,99/mês**
- KVM 8 – **R$ 119,99/mês**

Ao escolher o seu plano, leve em consideração as necessidades do seu projeto. Por exemplo, o plano KVM 2 conta com 2 vCPUs, 8 GB de RAM e 100 GB de armazenamento SSD NVMe — capacidade ideal para rodar aplicações de médio porte, como a ferramenta de automação n8n.

Não se preocupe em escolher o plano perfeito logo de início: você pode começar com uma opção de entrada e fazer upgrade para planos superiores sempre que precisar de mais recursos.

##### Quais são os limites de CPU, RAM, inode e disco dos planos da Hostinger?

Confira nosso guia sobre os parâmetros e limites dos planos de hospedagem para ver todos os recursos disponíveis em nossos serviços. O artigo detalha os limites de cada plano para ajudar você a escolher a opção ideal para o seu projeto.

##### Como começar a usar o servidor VPS na plataforma da Hostinger?

Para ajudar você a dar os primeiros passos na hospedagem VPS, criamos um processo de configuração inicial bem simples. Basta escolher o sistema operacional e as aplicações pré-instaladas para ter seu servidor pronto em poucos cliques.

Para conferir o passo a passo completo, veja nossos tutoriais sobre como começar a usar sua hospedagem VPS e quais os primeiros passos após contratar um VPS.

##### Quais sistemas operacionais estão disponíveis no servidor VPS?

Nossa plataforma de hospedagem VPS oferece uma ampla variedade de sistemas operacionais para que você escolha a melhor opção para o seu projeto.

Para conferir a lista completa e as especificações, acesse nosso guia sobre os sistemas operacionais disponíveis para VPS.

##### Vou receber suporte ao usar o VPS?

Sim. Nossa hospedagem VPS é **autogerenciada**, oferecendo controle total sobre o seu servidor virtual — além de diversas opções de suporte para facilitar sua gestão diária.

Com o **VPS gerenciado por IA**, você conta com um assistente integrado capaz de **executar tarefas reais de gerenciamento no servidor**. Usando linguagem natural, basta descrever o que precisa para a IA resolver problemas, gerenciar contêineres Docker, monitorar recursos, ajustar configurações e guiar você em ações técnicas — tudo direto no seu painel.

Você também tem acesso a:

- Painel de controle intuitivo com modelos prontos para uso
- Tutoriais completos e guias passo a passo
- Cursos em vídeo exclusivos da Hostinger Brasil

Para dúvidas sobre faturamento ou planos, nossa **equipe de Sucesso do Cliente está disponível 24 horas por dia via chat ao vivo**.

##### Qual é a diferença entre hospedagem VPS e hospedagem cloud?

Tanto os nossos planos de VPS quanto os de hospedagem cloud são indicados para projetos de alta demanda que exigem máxima velocidade, segurança e alta disponibilidade.

A principal diferença está no modelo de gestão. Na nossa hospedagem cloud gerenciada, nós cuidamos da manutenção e da segurança do servidor por você. Além do suporte 24 horas da equipe de Sucesso do Cliente, o plano cloud inclui recursos automatizados, como atualizações de WordPress — porém, sem acesso para alterar as configurações do servidor.

Já no VPS, você tem autonomia total — com acesso root e integração direta com suas ferramentas via API da Hostinger. Isso permite instalar qualquer sistema operacional, aplicar softwares personalizados e automatizar rotinas no seu servidor.

Embora a gestão do VPS exija um pouco de conhecimento técnico, nosso assistente de IA ajuda a executar diversas tarefas de administração com facilidade.

##### O VPS da Hostinger tem uma API pública?

Sim, a hospedagem VPS oferece uma API pública que permite interagir diretamente com o servidor por meio de código, sem complicações. Com um conjunto abrangente de endpoints, você pode gerenciar diversos aspectos do sistema sem precisar acessar a interface.

Quer ir além? Configure o servidor MCP da Hostinger para conectar ferramentas de IA, como Claude e Cursor, ao seu VPS usando nossa API pública. Essa integração oferece uma abordagem simplificada de administração do sistema no estilo *vibe coding*, permitindo gerenciar seu servidor como nunca antes.

Confira os principais benefícios da API pública da Hostinger para VPS:

- **Integração simplificada** – amplie os recursos do seu VPS com qualquer plataforma, seja um painel de controle personalizado ou ferramentas de implantação, para criar a infraestrutura de hospedagem ideal para suas necessidades.
- **Automação sem esforço** – configure fluxos de trabalho para automatizar tarefas repetitivas, como backups, e deixe o restante por conta da nossa API.
- **Insights em tempo real** – mantenha a disponibilidade dos seus serviços com acesso a dados essenciais do VPS, como uso de CPU, RAM, armazenamento e rede.

A API pública da Hostinger está disponível em todos os planos de hospedagem VPS e pode ser configurada de forma simples pelo hPanel. Acesse nossa página dedicada para pessoas desenvolvedoras para saber mais sobre como usá-la.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
