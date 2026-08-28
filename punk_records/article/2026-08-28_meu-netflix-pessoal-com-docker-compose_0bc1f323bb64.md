---
item_id: "8d385486-eb09-426b-bcde-83497b663818"
platform: article
external_id: "0bc1f323bb64"
canonical_url: "https://akitaonrails.com/2024/04/03/meu-netflix-pessoal-com-docker-compose"
channel: "Fabio Akita · AkitaOnRails.com"
captured_at: 2026-08-28
status: enriched
triage: null
tags: ["docker-compose", "self-hosting", "plex", "homelab", "transcoding", "nas", "radarr", "sonarr"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: baixa
  estudo_geral: alta
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Meu "Netflix Pessoal" com Docker Compose

🔗 https://akitaonrails.com/2024/04/03/meu-netflix-pessoal-com-docker-compose

## Resumo

Fabio Akita detalha a arquitetura completa do seu servidor de mídia e armazenamento pessoal baseado em mais de 80 TB de capacidade. A infraestrutura combina um NAS Synology DS1821+ para armazenamento em rede local de 10 Gbps e um mini-PC Intel NUC dedicado à execução de containers Docker em Ubuntu. Para alimentar o acervo, o autor combina mídias físicas extraídas via MakeMKV e HandBrake com automação de downloads via stack 'Arr' (Sonarr, Radarr, Prowlarr e qBittorrent). A reprodução e organização ficam a cargo do Plex Media Server, que utiliza aceleração por hardware via mapeamento do dispositivo /dev/dri. O autor relata também problemas práticos enfrentados, como travamentos de reprodução causados por legendas no formato gráfico PGS, resolvidos com legendas em SRT. Por fim, a infraestrutura se estende para leitura de mangás (Kaizoku e Kavita) e privacidade de rede local com Pi-hole e Cloudflared.

## Tópicos

- **Infraestrutura de Hardware e Armazenamento** — Combinação de NAS Synology com ~80TB em RAID, rede local de 10 Gbps e Intel NUC dedicado para subir containers Docker em Linux.
- **Extração e Otimização de Mídia (MakeMKV e HandBrake)** — Uso de MakeMKV para remux direto de discos UHD 4K e HandBrake com aceleração NVENC para comprimir arquivos em H.265 sem perda perceptível.
- **Automação do Fluxo de Download (*arr Stack)** — Integração entre qBittorrent, Sonarr (séries), Radarr (filmes), Flaresolverr (bypass de captchas) e Prowlarr para sincronização de indexadores.
- **Streaming e Resolução de Gargalos com Plex** — Configuração de aceleração de hardware via /dev/dri e diagnóstico de travamentos causados por legendas gráficas PGS rasterizadas no transcoding.
- **Serviços Auxiliares de Rede e Conteúdo** — Implementação de Pi-hole com DoH (Cloudflared) para filtragem de DNS, Overseerr para solicitações e Kaizoku/Kavita para mangás.

## Ferramentas citadas

- **Docker Compose**: Orquestração declarativa de todos os containers e volumes da stack de mídia.
- **Plex Media Server**: Servidor de streaming multimídia com interface estilo Netflix e suporte a Direct Play.
- **Sonarr**: Automação de busca, monitoramento de episódios e agendamento de séries de TV.
- **Radarr**: Gerenciamento e download automatizado de filmes integrando indexadores e clientes de torrent.
- **Prowlarr**: Gerenciador centralizado de indexadores e trackers integrado a Sonarr e Radarr.
- **qBittorrent**: Cliente BitTorrent controlado programaticamente via API e WebUI.
- **HandBrake**: Software de transcodificação de vídeo com aceleração de hardware NVENC/QSV.
- **MakeMKV**: Ferramenta para ripar e descriptografar discos Blu-Ray e UHD para arquivos MKV (Remux).
- **Pi-hole**: Servidor DNS local para bloqueio de anúncios e telemetria na rede.
- **Flaresolverr**: Serviço proxy para contornar desafios de proteção anti-bot da Cloudflare em indexadores.

## Pontos-chave

- Legendas no formato gráfico PGS exigem rasterização em tempo real sobre o vídeo, provocando gargalos severos de transcoding que são resolvidos trocando para arquivos de texto .SRT.
- Mapear o dispositivo '/dev/dri' no Docker Compose é indispensável para liberar aceleração por hardware (Intel QSV / NVIDIA NVENC) no transcoding do Plex.
- O Prowlarr resolve o overhead de gerenciar trackers manualmente ao sincronizar indexadores funcionais diretamente no Sonarr e Radarr.
- Rede cabeada local de 10 Gbps é fundamental para reproduzir arquivos 4K Remux (50 a 80 GB por filme) sem depender de conexões de internet lentas.
- O conceito de 'Direct Play' no Plex elimina o uso de CPU/GPU ao enviar o fluxo de dados bruto diretamente quando o cliente suporta o codec original.
- Para coleções digitais críticas, a regra de ouro inclui redundância local em RAID aliada a backups frios em nuvem (como Amazon S3 Glacier).

## Como aplicar

Serve como referência arquitetural para estruturação de serviços com Docker Compose, configuração de rede interna e passagem de dispositivos de hardware (/dev/dri) para containers Linux.

## 🍩 York diz

Nossa, Fernando, você viu o preço de montar esse monstro com mais de 80 TB? Com o dinheiro de todos esses HDs de 20 TB e placa de 10 Gbps, eu comprava um caminhão de donuts recheados e pagava todas as assinaturas de streaming pro resto da vida! Mas admito que automatizar o download e organização pra nunca mais ter trabalho braçal é o tipo de preguiça inteligente que eu aprovo.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Meu "Netflix Pessoal" com Docker Compose

*Se tem preguiça de ler, clique aqui pro TL;DR*

Quem acompanhava meu canal no YouTube ou meu Instagram já acompanhou a saga com meu NAS (meu servidor pessoal), meu Synology DS1821+ com quase 80 TB de espaço.

Todos os videos do meu canal, incluindo os arquivos originais, estão lá. Só isso dá terabytes. Todo minha biblioteca do Steam está lá, são uns 4 terabytes. Todos os meus jogos antigos, retro-games, também, incluindo ISOs de Xbox 360 e PS3. São mais 4 terabytes. Toda minha coleção de discos Ultra HD (BluRay 4K) eu ripei (fiz backup), são mais alguns terabytes. Neste instante já estou usando mais de 50 terabytes.

Antes que venham dar palpite, sim, isso não é pra qualquer um. Estamos falando de 8 HDs de 10.9 TB, mais upgrade de 2 HDs de 20 TB, mais outros 2 HDs de 20 TB de backup pra caso um deles dê pane, mais 2 NVMEs de 1 TB cada só pra ser cache, mais placa de rede de 10 Gbps. Além disso eu mantenho várias cópias online de parte desse conteúdo em Google Drive ou Dropbox, e um backup inteiro na Amazon Glacier, pra rara ocasião se minha casa pegar fogo, por exemplo. Estou preparado pra qualquer catástrofe, sempre.

A Synology é uma das melhores marcas de NAS caseiros. Sim, dá pra fazer bem mais sofisticado também, basta montar um servidor de verdade, com CPUs como AMD EPYC ThreadRipper, usando sistemas como TrueNAS. Mas aí é demais pra mim, já não me sinto confortável dando manutenção. Como eu disse, os limites cada um tem que saber os seus.

1o HD de 20TB terminou de se integrar ao RAID! Levou 2 dias inteiros!! Colocando o 2o HD ... de 4 😅 pic.twitter.com/Rv6dqBQr05

— Akitando.com (@AkitaOnRails) March 27, 2024

*“Por que não deixar tudo online??”* Pra maioria das pessoas é o caminho mais fácil mesmo. Como eu disse, meu caso é particular. Você NÃO QUER ter mais de 50 TERAbytes online. Minha rede cabeada local é de 10 Gbps, minha internet de fibra é míseros 0.5 Gbps (500 Mbps). Trafegar video de alta qualidae pela internet é horrivelmente lento. Eu quero tudo em tempo real, e pra isso só sendo rede cabeada local.

Isso dito, eu montei um segundo mini-computador, usando um Intel NUC, conectado na mesma rede cabeada com o NAS. É Core i7, 32GB de RAM, ethernet 2.5Gbps, com o único intuito de ser um servidor Ubuntu vazio (poderia ser qualquer Linux, só escolhi o mais fácil mesmo) que serve pra subir containers Docker.

Mesmo esse PC-zinho é overkill, muito mais do que é necessário. Muitos vão comentar que um Raspberry-Pi 5 seria suficiente, e não estão errados. A melhor solução é a que você tem orçamento pra comprar e se sente confortável em dar manutenção. Não tente copiar exatamente o setup de ninguém, estude o que melhor encaixa pra você. E não percam tempo dando pitaco no setup dos outros, façam o seu.

De qualquer forma, resolvi compartilhar com vocês todos os arquivos de docker-compose que estou usando pra subir os containers docker nesse servidor. Eis o repositório no GitHub.

*AVISO:* não esqueçam que precisa editar os diretórios nos scripts. Ele está configurado pra acessar o mount point do meu NAS em rede, que é `/mnt/terachad`. Arrume pra apontar pros lugares certos na sua máquina.

*AVISO 2:* existem muitos detalhes que não estou cobrindo neste artigo. Este fórum do Reddit tem mais detalhes e mais discussões. Dependendo se estiver com dúvidas ou problemas específicos, talvez esteja respondido lá.

Deixa eu começar explicando um a um dos principais.

#### Portainer e Utilitários

Este é o trecho (veja completo no repositório):

```
volumes:
  portainer_data:
services:
  portainer:
    image: portainer/portainer-ce:latest
    restart: unless-stopped
    volumes:
      - portainer_data:/data
      - /var/run/docker.sock:/var/run/docker.sock
    ports:
      - '9000:9000'
```
Portainer é um gerenciador visual dos recursos gerenciados pelo serviço de Docker na sua máquina. Objetivo é mais pra eu visualmente conseguir “bater o olho” e ver se tem algum container com problema ou pra testar algum ajustezinho rápido em alguma configuração antes de editar no arquivo de docker compose.

No arquivo utils-docker-compose.yml tem outros serviços como Organizr que eu instalei mas ainda não parei pra configurar nem ver se realmente quero manter. Tem o Librespeed, que funciona como aqueles testes de velocidade de internet, mas pra rede local. Tem o Watchtower, que monitora atualização das imagens de todos os containers Docker, faz o download e automaticamente manda reiniciar com versões novas, pra manter todos os containers sempre atualizados.

E tem o ZeroTier que, assim como TailScale, oferece uma boa alternativa de serviço fácil de VPN, com baixa configuração, pra facilitar acessar seus serviços locais fora de casa. Sim, sim, antes que alguém vá pros comentários, dá pra montar OpenVPN do zero ou algo assim, mas vai por mim, essas opções são infinitamente mais “plug and play” e possivelmente mais seguros - porque todo mundo instala, mas poucos tem a disciplina de dar manutenção e atualizar o que precisa o tempo todo.

#### MakeMKV e HandBrake

Pra montar sua biblioteca pessoal de filmes, de forma legítima, o correto é você ser proprietário de discos de BluRay ou UHD e “ripar” eles. Se for esse o caso, recomendo comprar modelos de leitor de discos como o Pioneer BDR-XS07S Tem que ficar MUITO esperto porque não é qualquer leitor que funciona.

Veja no fórum do MakeMKV quais os modelos mais recomendados. Tem modelos que tiveram atualização de firmware que impedem deles serem usados pra ripar BluRay. Precisa achar modelos que ou não foram atualizados, ou que não é difícil fazer downgrade de firmware. O ideal é já comprar modelos que todo mundo sabe que funciona, e pra isso tem que fuçar fóruns como esse.

MakeMKV, como o próprio nome diz, “Faz arquivos de video MKV”, que é o bom e velho formato Matroska de envelope de video, um dos mais versáteis (porque suporta múltiplos streams não só de áudio, mas de legenda também).

*Crash course:* uma coisa é o codec que faz o encodings dos streams de video e streams de audio. Por exemplo, H.265 ou AV1, são codecs de video. MP3 ou AAC são codecs de áudio. Agora precisamos empacotar esses dois streams (ou mais, caso tenha múltiplas dublagens, por exemplo), num “envelope”, um “container”, um “formato de arquivo”, como arquivos “.mp4” ou “.mov”. Matroska é um formato de envelope de arquivo, que é bem flexível, permite múltiplos streams de tudo, incluindo de legenda, por isso é muito usado pra compartilhar em torrent.

Com esse container, você consegue acessar via navegador a interface gráfica do aplicativo (é como se fosse um cliente remoto de Windows, como VNC). Basta ter o leitor de Blu-Ray conectado via USB no seu computador e deve achar. Ele vai usar a biblioteca libredrive pra descriptografar os streams de dados do Blu-Ray, e por isso a importância das versões de firmware serem compatíveis (já terem sido quebrados).

Muitos não sabem que a gente chama tudo de “Blu-Ray” mas na realidade Blu-Ray é pra filmes encodados em versão Full HD, que é 1080p. As versões em 4K (2160p) vem em UHD, que é **Ultra HD**. A caixa de Blu-Ray costuma ser azul, as de UHD são pretas, você quer as UHD sempre que possível, claro. E eu tenho uma coleção enorme:

"onde eu tô gastando tanto espaço??"

Boa parte é fazendo Rip (backup) de todos os meus UHD (BluRay 4K). E isso porque estou re-encodando em bitrate menor depois de ripar kkkk pic.twitter.com/T1yPa6EIcV


A vantagem de um app como MakeMKV é conseguir descriptografar o stream de video e copiar bit a bit exatamente como está no UHD, a melhor qualidade possível. É o que se chama de REMUX (remuxing), que é extrair o stream do container e colocar em outro container sem re-encodar. Já deve ter visto em alguns arquivos de Torrent, é a melhor qualidade. Porém significa que vai gastar o mesmo espaço que no disco, uma faixa de 50 a 80 GIGAbytes, por filme. Cada uma dúzia de filmes vai consumir quase 1 terabyte. Dependendo de quantos filmes você quer ter, seu espaço livre vai acabar muito rápido.

Pra minimizar isso, podemos recodificar ou “re-encodar”. É como quando pegamos uma foto em RAW e re-encodamos pra um formato de menor qualidade, como PNG ou mesmo JPEG. Se souber onde procurar, vai achar os artefatos de compressão, mas no geral, compensa. Por exemplo, no meu caso, encodar pra H.265 10-bit, QP 15 Constant Quality.

A melhor opção é ter uma placa de video NVIDIA, com suporte a encoding de video via hardware NVENC e usar o melhor software pra encoding de video: Handbrake. No meu caso, eu escolho o perfil pré-configurado de **Matroska H.265 MKV 4K60fps** e mudo pra usar o encoder NVENC da minha placa RTX 4090, que isso acelera o encoding em múltiplas vezes.

No docker compose, assim como MakeMKV, posso subir esse app pra ter acesso via navegador web, assim:

```
  handbrake:
    restart: unless-stopped
    image: jlesage/handbrake
    ports:
      - "5801:5800"
    environment:
      - AUTOMATED_CONVERSION=0
      - HANDBRAKE_GUI=1
      - DARK_MODE=1
      - TZ=America/Sao_Paulo
    volumes:
      - "/home/akitaonrails/handbrake:/config:rw"
      - "/home/akitaonrails:/storage:ro"
      - "/mnt/terachad/Videos/BluRay:/watch:rw"
      - "/mnt/terachad/Videos/BluRayOptimized:/output:rw"
    devices:
      - /dev/dri:/dev/dri
```
Seu PC tem no mínimo uma placa de video Intel com suporte a encoding via hardware QSV ou melhor, da NVIDIA, com suporte a NVENC. Em ambos os casos, fazemos o container ter acesso a isso mapeando o dispositivo `/dev/dri`. Sem isso, o encoding vai ser via CPU, e vai demorar ordens de grandeza mais.

Lembrando que encoding via software, é mais lento mas vai ter qualidade superior a Intel QSV que, apesar de rápido, sempre me dá qualidade de video inferior. NVENC é o melhor dos dois mundos: excelente qualidade e muito rápido.

**AVISO:** no meu caso, quero a melhor qualidade possível, por isso faço backup de UHD, por isso mesmo torrent eu baixo BR-DISC que é backup de UHD, e isso é absurdamente pesado como expliquei. Daí eu manualmente refaço o encoding pro perfil Matroska H.265 como também expliquei.

Muitos não querem ter esse trabalho, pra isso não deixe de ler o fórum do Reddit que explica como configurar os próximos serviços pra não baixar arquivos grandes assim, eu não vou mostrar aqui, porque não é meu caso.

#### QBitTorrent

Por mais Blu-Ray e UHDs que você tenha ou consiga comprar, muita coisa nem existe em disco físico. Nesse caso, sua única opção é BitTorrent. E sim, é **ilegal piratear**, eu **não estou incentivando pirataria** bla bla bla …

Cada país tem uma lei, vá pesquisar. Vou assumir que todo mundo sabe com o que está fazendo e não é problema meu. Não adianta comentar sobre isso, não vou alongar isso. A Web já está abarrotada de material a respeito, vá no Google e procure você mesmo.

Primeira coisa que queremos é instalar QBitTorrent, provavelmente o melhor e mais completo aplicativo pra baixar torrent, e também tem interface web e funciona via Docker:

```
  qbittorrent:
    image: linuxserver/qbittorrent:latest
    restart: unless-stopped
    environment:
      - TZ=America/Sao_Paulo
      - WEBUI_PORT=8080
      - PUID=1000
      - PGID=1000
    volumes:
      - /home/akitaonrails/qbittorrent/config:/config
      - /mnt/terachad/Downloads/torrents:/downloads
    ports:
      - '8080:8080'
      - '62609:62609'
```
É importante lembrar de gerar uma porta aleatória nas configurações do QBitTorrent, como mostrado na imagem abaixo. Qualquer porta entre 1025 e 65535 deve funcionar, mas é possível que sua rede bloqueie alguma sequência de portas nesse intervalo, então tem que testar. Pesquise fóruns na web, cuidado que tem muita dica online que já está desatualizado.

Precisa entender o mínimo de redes, entender se está atrás de um NAT, como mapear portas externas, se tem firewall ativo bloqueando portas, etc.

Se o torrent não estiver baixando, “pode ser” isso. Coloco entre aspas porque é só uma possibilidade. Então clique em “random” pra escolher outra porta, edite a configuração de docker compose pra mapear a porta nova e reinicie o container.

Por alguma razão o gerenciamento de salvamento vem tudo como Manual, é importante mudar pra automático:

Outro detalhe é pedir pro QBitTorrent re-anunciar os downloads para os trackers quando a porta mudar. Pra isso habilite essa opção “Reannounce to all trackers when IP or port changed”, senão os downloads podem não reiniciar.

Finalmente, como pesquiso coisas pra baixar? Posso manualmente ir no Google ou DuckDuckGo ou direto em sites como os do PirateBay da vida e buscar arquivos “.torrent” ou links magnéticos. Pra saber o que é isso, assista meu vídeo sobre Criptografia na Prática onde explico tudo sobre Torrent também.

O QBitTorrent tem suporte a plugins de pesquisa. Ele já vem com alguns habilitados. No canto inferior direito, tem o botão de “Search plugins”. Queremos adicionar o plugin que engloba tudo: o serviço Jackett.

Veja que ele quer um host com nome “jackett” habilitado na porta 9117, pra isso temos este trecho no docker compose:

```
  jackett:
    image: ghcr.io/linuxserver/jackett:latest
    restart: unless-stopped
    environment:
      - TZ=America/Sao_Paulo
      - PUID=1000
      - PGID=1000
    volumes:
      - /home/akitaonrails/jackett/downloads:/downloads
      - /home/akitaonrails/jackett/config:/config
    ports:
      - '9117:9117'
```
Ele vai subir um serviço onde podemos acessar a interface web assim:

É um serviço que consolida dezenas de sites de pesquisa de torrents num lugar só, consegue testar se estão online e, mais importante, fornece uma chave de API no canto superior direito, que devemos copiar e editar na configuração do plugin do QBitTorrent. Com isso é possível fazer pesquisar diretamente, recebendo respostas assim:

Veja na coluna da direita que lista de onde puxou esses resultados: está vindo do serviço Jackett.

#### Radarr (Filmes)

Procurar manualmente funciona, mas existem formas melhores: deixar um serviço fazer a procura e gerenciar o download pra você, e pra baixar filmes, podemos usar o serviço Radarr:

Pra isso, temos este trecho no docker compose:

```
  radarr:
    image: ghcr.io/linuxserver/radarr:latest
    restart: unless-stopped
    depends_on:
      - qbittorrent
    environment:
      - TZ=America/Sao_Paulo
      - PUID=1000
      - PGID=1000
    volumes:
      - /home/akitaonrails/radarr/appdata/config:/config
      - /mnt/terachad/Downloads/torrents:/downloads
      - /mnt/terachad/Videos/radarr/movies:/movies
      - /mnt/terachad/Videos/radarr/anime:/anime
    ports:
      - '7878:7878'
```
Veja que mapeei diretórios diferentes pra filmes ocidentais e filmes anime, é uma preferência minha, você pode organizar como quiser. Como avisei antes, não copie e cole igual estou mostrando aqui: ajuste os diretórios pra sua máquina.

O principal é que uma vez iniciado, podemos navegar pela interface web, pra opção “Settings”. Ali vai ter “Download Clients"e podemos registrar o serviço web de QBitTorrent:

Eu não mostrei, mas nas configurações do QBitTorrent vai ter um lugar pra cadastrar essa senha de admin pra acessar a API dele via web. Não esqueça de cadastrar lá e usar a mesma senha aqui. Assim o Radarr pode controlar o download de filmes diretamente com o QBitTorrent, sem você precisar se meter.

#### Sonarr (Séries de TV)

Mesma coisa que o Radarr, mas pra séries de TV, temos o serviço Sonarr:

Esse serviço é sensacional. Ele acha suas séries, cruzando com bancos de dados online com detalhes como temporadas, nomes de cada episódio e vários outros metadados. Daí ele não só consegue baixar episódios antigos, como mantém uma agenda pra ir baixando séries que ainda estão passando. Toda semana aparece episódio novo sozinho:

E mesma coisa do Radarr: em Settings e Download Clients, posso registrar meu QBitTorrent, daí o Sonarr se vira pra ir baixando os episódios:

E pra subir o serviço, no docker compose temos este trecho:

```
  sonarr:
    image: ghcr.io/linuxserver/sonarr:latest
    restart: unless-stopped
    depends_on:
      - qbittorrent
    environment:
      - TZ=America/Sao_Paulo
      - PUID=1000
      - PGID=1000
    volumes:
      - /home/akitaonrails/sonarr/appdata/config:/config
      - /mnt/terachad/Videos/sonarr:/tv
      - /mnt/terachad/Downloads/torrents:/downloads
    ports:
      - '8989:8989'
```
Mesma coisa que o Radarr, eu mapeei pastas diferentes pra anime e não-anime, que é questão de preferência da sua organização.

#### Prowlarr (indexador)

Pra tanto o Radarr e Sonarr saberem de onde puxar os torrents de séries e filmes, eles precisam pesquisar em indexadores ou trackers públicos (ou privados, se você tiver bons contatos - eu não tenho, nem pergunte). Pra isso temos Prowlarr. Esse é o serviço mais importante de todos, porque se esse não funcionar, nada vai baixar direito.

Por outro lado, é o serviço que eu não sei dizer direito qual a melhor forma de configurar. Por enquanto é realmente gastar horas nele fazendo tentativa e erro e fuçando o quanto puder. Nunca fiquei 100% satisfeito com minha configuração. Se tiverem dicas sobre isso, mandem nos comentários abaixo.

Veja que lista dezenas de indexadores, ou trackers. É parecido com o Jackett. A diferença é que o Jackett é pra pesquisas manuais que você mesmo vai fazer, direto no QBitTorrent. Já os indexadores do Prowlarr vão ser configurados direto no Sonarr e Radarr. Aqui começa a confusão, vamos entender:

Tanto no Sonarr quanto no Radarr, além de Download Clients, onde podemos configurar o QBitTorrent, também vai ter essa opção de “Indexers”, onde podemos configurar em quais trackers procurar pela mídia.

Pense num tracker como um mini-Google público, é onde as pessoas registram seus torrents quando querem compartilhar. Torrents não são mágicos e nem aparecem do nada. Alguém tem que criar um registro em algum lugar. Mas não existe só “um” lugar: é uma rede distribuída e qualquer participante pode subir um tracker se quiser. É como se você pudesse subir seu próprio Google miniatura, só pra registrar arquivos de torrent.

É um saco ficar gerenciando isso. Alguns trackers pequenos resolvem sair do ar, novos aparecem, configurações são modificadas, e precisamos ficar gerenciando manualmente isso, tanto no Sonarr quanto no Radarr. Pra isso serve o Prowlarr: pra gerenciar os trackers pra você. Vamos entender como.

Nas configurações do Prowlarr, começamos configurando onde encontrar nossos serviços de Sonarr e Radarr:

Por exemplo, esta é a configuração do meu Sonarr. Notem que o hostname é “sonarr” e isso funciona porque no meu docker compose eu subo todos os serviços na mesma VLAN, e por padrão o docker registra como hostname o nome do serviço configurado no arquivo YAML. Se não entende Docker, não deixe de assistir meus videos sobre containers.

Também precisamos configurar acesso ao QBitTorrent:

Esse outro “Sabnzdb” é usando outro protocolo de downloads mais antigo, baseado em newsreader de USENET. Sim, aquela antiga Usenet mesmo. Quem sabe, sabe. Tem esse serviço no meu docker compose, mas nunca consegui fazer funcionar direito. Melhor até apagar essa entrada pra não confundir. Hoje eu deixo só torrent mesmo, mas é porque muito conteúdo parece que só existe nesses grupos mais antigos de newsreader.

Finalmente, muitos trackers hoje implementam algum tipo de proteção contra bots usando captcha da Cloudflare, sabe aquele troço que fica “você é um humano?”. Pra passar por isso, precisamos do serviço Flaresolvrr, que podemos subir no docker compose assim:

```
  flaresolverr:
    image: ghcr.io/flaresolverr/flaresolverr:latest
    restart: unless-stopped
    volumes:
      - /home/akitaonrails/flaresolverr/config:/config
    ports:
      - '8191:8191'
```
E no Prowlarr podemos configurar na seção de Indexers, assim:

Como eu disse, é um saco de configurar isso. Mas ainda não acabamos. Na tela principal, tem que sair habilitando todos os indexers que fazem sentido pra você. Não é bom habilitar tudo, porque vai ficar muito pesado depois. Veja os tags de cada um. Tem indexer que é só de pornô, por exemplo, eu pulei todos esses. Tem indexers específico só pra conteúdo em russo ou chinês, daí pula também.

No final, é bom clicar esse “Test All Indexers” pra checar quais ainda estão ativos ou não. E por fim, podemos clicar em “Sync App Indexers”, que vai cadastrar todos os indexers que sabemos que estão funcionando, nos registros do Sonarr e Radarr. Entenderam? O Prowlarr vai configurar os dois com os indexers mais atualizados, e remover os que não estão mais ativos. Não precisamos configurar cada um deles manualmente.

É importante entender isso, porque senão você vai ver o Sonarr e o Radarr não conseguindo baixar nada e não vai saber porque: mas é porque os indexers estão errados ou obsoletos ou insuficientes. Gaste bastante tempo lendo a documentação do Prowlarr.

#### Plex (Netflix Particular)

Pra assistir tudo que baixar, tem várias opções. Se é só pra você, basta ir baixando tudo num HD externo ou algo assim, e assistir diretamente do seu PC ou notebook. Dependendo da Smart TV ou console de videogame, também dá pra conectar seu HD ou pendrive via USB e assistir direto.

Se for um pouquinho mais sofisticado, e tiver um PC ou Raspberry Pi sobrando, dá pra instalar Sonarr, Radarr, e compartilhar o diretório de downloads pela rede, usando protocolos como CIFS, que é pra pasta compartilhada de Windows. Novamente, muitas Smart TVs e consoles suportam montar pastas compartilhadas pela rede.

Mas se quiser algo mais amigável e sofisticado, dá pra ter literalmente seu “Netflix Particular”, com uma interface gráfica parecida com qualquer plataforma de streaming, onde mostra thumbnails, descrições, detalhes do filme ou série, tocador de video e tudo mais e até sugestões do que assistir, sugestões de filme baseado no que está assistindo, informações de atores e tudo mais.

Existem vários projetos que fazem isso. Um deles, que a comunidade curte mais por ser 100% aberto, é o Jellyfin (derivado do antigo Emby). Recomendo que testem, tem tudo que a maioria das pessoas precisa. Basta mapear as pastas de downloas do Sonarr, Radarr e ele vai indexar tudo e organizar pra você. Daí, de qualquer PC, é só acessar a interface web e tudo só funciona.

Mas eu pessoalmente prefiro o Plex, que é mais antigo, é mais fechado (por isso alguns não gostam), mas por oferecer planos pagos com funcionalidades exclusivas, o nível de polimento é nitidamente melhor. A interface é bem mais bonita, e parece mais “profissional”. Jellyfin, por melhor que seja, ainda tem cara que foi um programador backend que fez, com muita má vontade em UX e design.

Além disso, pra assistir numa Smart TV ou Android TV da vida, precisa ter app no Google Play Store. Jellyfin não tem app pra tudo, algumas TV, não lembro se LG ou Samsung, nem tem o app disponível. Então precisa fazer side-load. Não é amigável. Plex, por outro lado, está disponível em bem mais lugares, então costuma ser mais “plug and play”, parecido com baixar app de Netflix ou Amazon Prime.

Plex também tem funcionalidades que “just works”, coisas triviais que se espera num tocador, como botão de “pular abertura” ou “resumir a partir de onde parou” ou “pular pro próximo episódio” ou “pesquisar e trocar legenda”. É isso que interfaces como essas vão te oferecer, daí a usabilidade é realmente muito parecida com assistir Netflix. Não tem isso se usar um tocador genérico de PC como um VLC da vida.

Pra subir é fácil, eis o trecho do meu docker compose:

```
  plex:
    image: plexinc/pms-docker:latest
    restart: unless-stopped
    environment:
      - TZ=America/Sao_Paulo
      - PUID=1000
      - PGID=1000
      - VA_DRIVER=IHD
      - PLEX_HW_TRANS_MAX=16
    volumes:
      - /home/akitaonrails/plex/config:/config
      - /home/akitaonrails/plex/data:/data
      - /home/akitaonrails/plex/transcode:/transcode
      - /mnt/terachad/Videos:/media
    devices:
      - /dev/dri:/dev/dri
      - /dev/bus/usb:/dev/bus/usb
    network_mode: host
```
Existe um pequeno detalhe que muitos não entendem: Plex faz *transcoding* dos videos. Ou seja, ele vai re-encodar o video antes de mandar pro app ou navegador que vai tocar, isso é pesado, é conversão de stream de video. Se seu servidor não for forte o suficiente, seu video vai ficar engasgando pra tocar.

Na realidade, é mais complicado do que isso. Existe um protocolo chamado “Direct Play” ou “Direct Stream”. Tem um artigo que explica isso no site do Plex. Se o PC, SmartTV, console, etc, tiverem suporte ao codec do video em questão, teoricamente o Plex só vai passar os bits direto, sem tentar converter nem nada. Entenda: nem todo dispositivo tem capacidade pra tocar qualquer codec de video.

A maioria do conteúdo hoje em dia é encodado em H.264 ou H.265 ou até AV1, que é mais novo e mais eficiente. Problema, digamos que você queira tocar num PC bem antigo ou num PS4 da vida. Eles vão ter suporte a H.264, talvez H.265, se tiver sorte, mas certamente não a AV1. Daí seria super lento tentar tocar usando só a CPU. O certo é ter instruções de hardware pra tocar AV1, especialmente num CPU antigo.

Então o Plex pergunta pro dispositivo: *“você suporta AV1?”* O tocador vai dizer *“nope, sou fraco.”* Então o Plex vai fazer o transcoding de AV1 pra H.264, por exemplo. Tudo isso é transparente pra você.

Mas aí você vai notar que na hora de tocar o video fica engasgando, pausa toda hora. Pode ser um problema de banda da sua rede ou, pode ser problema do seu servidor de Plex ser muito fraco ou, de não estar configurado pra transcoding via hardware, e estar indo na força bruta usando só a CPU.

Assista meu video sobre compressão, onde explico sobre codecs, mas em resumo, o correto é que seja lá qual PCzinho estiver usando pro seu Plex, que ele tenha o mínimo de capacidade de encoding de video em hardware. A maioria costuma ter pelo menos capacidade de H.264, como as instruções **Intel QSV**, veja se sua CPU tem esse suporte. Só não vai ter se for velho demais, tipo coisa de 10 anos pra trás. Se for um servidor forte, com GPU NVidia, vai ter coisas como **NVENC**, que dá suporte a H.265. Se for CPU Intel moderna, vai ter suporte a **AV1**.

Em todo caso, em Linux, essas instruções devem ficar expostas no dispositivo `/dev/dri`, e por isso precisamos mapear no container docker como fiz acima. Cheque se existe esse dispositivo.

Se estiver tudo certo, no Plex vai ter essa opção de configurar “Transcoder”:

Queremos nos certificar que a qualidade está em “Make my CPU hurt” e que a opção de “Use hardware acceleration when available” está hablitado também, daí ele vai usar o `/dev/dri` pra acelerar o transcoding. E isso faz uma diferença BRUTAL na velocidade. Se estiver com playback sendo engasgado, muito provavelmente é o transcoding.

Quando o dispositivo, seu smartphone ou sua TV, tem suporte ao exato codec usado no arquivo de video que queremos assistir, teoricamente, o Plex consegue passar o stream direto, sem transcodar, que é o mundo ideal, porque aí não processamento nenhum. Isso é Direct Play. Mas pra isso os arquivos de video precisam estar num determinado codec, numa determinada configuração. Mas mesmo num codec suportado, se sua TV for fraca e não suportar 4K, e pedir pro Plex em Full HD (1080p), daí o Plex vai transcodar de H.264 4K pra H.264 1080p, por exemplo. Por isso falo que é mais complicado do que parece.

**DETALHE IMPORTANTE:** Recentemente fiquei confuso ao tocar alguns dos meus videos. Eu tenho o melhor hardware, tanto pro servidor de Plex, com aceleração via hardware, quanto Android TV pra tocar que é meu NVIDIA Shield Pro, quando rede cabeada, etc. Mas alguns videos ficavam engasgando. E no final o culpado não era hardware, nem configuração, nem nada disso, era a maldita legenda:

Quem já precisou baixar legendas, já deve ter visto o formato mais comum, que é o **.SRT** (SubRip). Alguns que se aventuraram mais, já devem ter visto outros formatos, como SSA (SubStation Alpha), TTML (Timed Text Markup Language), VTT (Web Video Text Track), VOBSUB, etc.

Sim, existe MUITO mais que SRT. Em particular, se você fizer como eu e ripar UHDs e extrair as trilhas de legenda do próprio disco, aplicativos como o MakeMKV podem baixar em formato VOBSUB (que é ok) ou o maldito **PGS** (Presentation Graphic Stream Subtitle Format).

A maioria das trilhas de legenda foram feitas pra serem enviadas ao tocador em paralelo, e separado, da trilha de video. Assim como a trilha de áudio vai separado. O tocador recebe trilha de video, trilha de áudio, e toca os dois sincronizados. Mesma coisa com trilha de legenda, no caso de arquivos SRT ou SSA ou TTML da vida.

Mas PGS é diferente: ele tem capacidades gráficas! Estou chutando, mas se já viu legenda coloridas, animadas, que se mexem ou se posicionam em locais absolutos na tela (como pra ficar exatamente em cima de outdoor no video, por exemplo), daí precisa haver um passo antes de rasterizar e renderizar essa legenda gráfica **EM CIMA** do stream de video. Isso existe um passo mais pesado de encoding, ou seja, vai ser **PESADO** de tocar em tempo real.

A solução: use o Plex pra pesquisar uma nova legenda, em formato SRT, e ignore a legenda PGS. Só de fazer isso, parou de engasgar na hora de tocar.

#### Overseerr

Só com o Sonarr e Radarr, mais os indexers do Prowlarr, já é suficiente pra conseguir procurar e baixar tudo. Mas tem um outro app que tenta facilitar o processo de descobrir coisas novas pra baixar. Esse é o Overseerr:

Ele vai em bancos de dados online gratuitos (tipo os IMDB) da vida e fica de olho em tudo que sai de novo, tudo que está em “trending”. Se eu quero achar alguma coisa nova, é uma boa. Mesmo coisas que já sei o que quero, basta pesquisar no Overseerr e clicar em “Request”:

Eu configuro integração com Sonarr e Radarr nas configurações, assim ele sabe pra quem mandar a requisição. Funciona tudo integrado. Só preciso usar a interface do Overseer pra requisitar as coisas e posso esquecer do Sonarr e Radarr em background.

#### Bazarr (legendas)

Eu não preciso, mas minha namorada às vezes prefere assistir com legendas em português. E é um saco isso porque nem sempre tem, ou o que tem é de baixa qualidade. Aliás, deixa eu já avisar que tanto legenda oficial quanto não-oficial, eu tô cansado de ver tradução errada. Minha diversão é ficar achando os erros na legenda. Se você depende de legenda, saiba que muitos significados importantes estão errados mesmo. Sempre prefira original.

Antigamente tinha que ir manualmente em sites como OpenSubtitles.org da vida, baixar o arquivo “.SRT”, renomear igual o nome do arquivo de video e ficar testando manualmente pra ver se tá sincronizado ou não.

Existem dois jeitos de resolver isso. Um é pelo próprio Plex, que tem a opção de pesquisar legendas em diversas línguas e ficar testando direto da interface do tocador. Facilita bastante porque pula o passo de ter que ficar no PC, manualmente baixando arquivos. Como expliquei na seção anterior, no meu caso, que a legenda dos backups de UHD foram extraídos no formato PGS, eu preciso buscar no formato SRT pra não engasgar na hora de tocar.

Outra forma é tentar baixar as legendas automaticamente antes. Isso não é perfeito porque existem diversas versões de legendas, algumas foram feitas pra DVD, outras pra BluRay, alguns até pra versões mais populares de “CAM” que são torrents de videos gravados direto no cinema com um smartphone, que é a versão mais porcaria de todas.

É muito importante até renomear os arquivos de video no melhor formato, com os metadados bem organizados, como explicado no fórum de Reddit que mencionei no começo do artigo. Eu não configuro tanto porque como disse, não preciso tanto de legenda assim. Mas leia lá pra ter os detalhes de como configurar Sonarr e Radarr pra já baixar os arquivos pra facilitar achar legendas depois. E avisando também que Português do Brasil é uma das línguas que menos tem legendas. É mais fácil achar legenda em Francês, Italiano, Russo, menos em Português.

Pra facilitar isso temos o serviço Bazarr:

Na configuração do Bazarr, vamos apontar pros nossos serviços locais de Sonarr e Radarr, assim ele fica sabendo toda vez que aparece episódio novo de série ou algum filme novo, e já agenda pra tentar procurar a legenda:

O principal é configurar os Providers, que são sites como o OpenSubtitles.org que mencionei antes, de onde baixávamos legendas manualmente. O Bazarr tem integração com vários deles, mas precisamos registrar manualmente, não é difícil. Quanto mais, melhor.

Pra subir o serviço, no docker compose, temos este trecho:

```
  bazarr:
    image: ghcr.io/linuxserver/bazarr:latest
    restart: unless-stopped
    environment:
      - TZ=America/Sao_Paulo
      - PUID=1000
      - PGID=1000
    volumes:
      - /mnt/terachad/Videos/radarr:/movies
      - /mnt/terachad/Videos/sonarr:/tv
      - /home/akitaonrails/bazarr/appdata/config:/config
    ports:
      - '6767:6767'
```
Aqui precisamos mapear as pastas do radarr e sonarr pra ele saber onde gravar as legendas.

Pra mim o Bazarr é o serviço que menos tem sido útil, porque ele não acha a maioria das legendas. Eu acabo procurando manualmente pelo Plex toda vez. Pode ser porque eu não fiz a configuração de renomear os arquivos baixados pelo Sonarr e Radarr. Então leiam o fórum que mandei antes.

#### Outros Serviços

No meu repositório tem outros arquivos de Docker Compose pra minha infra local. Não vou explicar em detalhes, mas só a saber:

Em net-docker-compose.yml eu configuro cloudflared e pi-hole. Pra quem não sabe, Pi-Hole é um servidor de DNS que tem funcionalidade de bloquear acesso a banners, ads, propaganda e até sites de malwares. Ele não substitui um anti-virus ou anti-malware, mas já ajuda muito.

Olha quantas queries bloqueadas tem. Isso me dá paz de espírito que estou dificultando bastante que terceiros consigam criar uma boa impressão digital dos meus padrões de navegação. Mais ainda porque estou usando DoH que é DNS over HTTPS com o serviço cloudflared. Se não sabia disso, queries de DNS é um protocolo texto aberto. Seu provedor sabe exatamente tudo que você navega. Eu prefiro não dar esse dado de graça pra eles, então mando tudo pra Cloudflare via HTTPS encriptado. Sim, a Cloudflare tem meus dados, mas eles não estão na minha jurisdição, então tá suficiente. É só pela diversão de dificultar mesmo.

Agora, no arquivo kaizoku-docker-compose.yml tem outro serviço tipo Sonarr pra TV, Radarr pra filmes, que é o Kaizoku pra mangá. Se você lê mangá online, já deve ter visto muitos sites sendo fechados por causa de copyright, direitos autorais e tudo mais. Eventualmente, os mangás online que você leu, vão desaparecer. Com o Kaizoku podemos preservar eles localmente também.

O Kaizoku é só pra baixar. Pra ler, precisamos de um leitor, da mesma forma que temos Plex pra video, temos Kavita Reader pra ler os mangás baixados. Assim como Plex, basta na primeira configuração apontar pra pasta onde o Kaizoku baixa tudo, daí o Kavita vai se virar pra organizar a biblioteca, baixar capas e outros metadados. É literalmente o Plex pra Mangá.

Ainda não explorei muito esse serviço. Ou ainda tem coisas pra refinar nele, ou eu que não sei configurar direito, mas nem tudo baixa capas direito. Vejam como não está bonito. Se tiverem dicas sobre Kavita e Kaizoku, não deixem de compartilhar abaixo.

Pra ler em si, é bem parecido com um Kindle Web ou outros sites online de mangá. Dá pra ler página a página, ou “scrollar” o capítulo inteiro, ele vai lembrar onde você parou e coisas básicas assim. Pode ser um bom projeto pra contribuir, se tem vontade de treinar com código aberto.

Finalmente, eu não sou muito de música, tenho músicas antigas que baixei em mp3 décadas atrás e não tenho muito apreço por música nova. Toco o que tem na playlist de Top 50 do Spotify e é isso. Mas pra quem é entendedor de música e quer algo similar a Sonarr e Radarr, ainda tem o serviço Lidarr. Esse eu não testei, mas fica a dica pra quem quiser uma biblioteca offline de música.

#### Conclusão

Fico muito contente com o estado atual dos serviços de compartilhamento de arquivos. Não percam muito tempo pensando demais. Só instalem e se divirtam. O código de tudo é aberto, se você é programador, vá lá fuçar o código e aprender algo novo, e quem sabe, até contribuir.

Eu não sou adepto de teorias apocalípticas, teorias da conspiração, nem nada assim. Eu só considero que, o que eu não tenho controle físico, eu **não tenho**. Se o que “é meu” está no controle de um terceiro, então “não é meu”. Esse é o princípio. Eu quero tudo que é meu sob meu único e exclusivo controle e pronto. Não importa se é menos conveniente, não importa se é mais caro. É uma questão de princípios: meu é meu e ponto final.

Além disso, nas plataformas de streaming, não existe tudo. Muita coisa de décadas passadas simplesmente foram apagadas da memória. Muitos nem lembram mais, especialmente quem não viu na época. Eu tenho nostalgia por programas de TV, filmes, que não existe online. Muitos sequer existem em mídia física. Tem filmes que depois de VHS nem chegaram a sair em DVD. Tem DVD que nunca saiu como Blu-Ray. Tem coisa em disco físico que nunca vai sair em streaming. Tem coisa em streaming que vai ser apagado em breve, e muitos nem vão notar.

O que é meu, é meu. Podem apagar o quanto quiserem. O que é meu, ninguém apaga. Se você tem apreço pelo que é seu, comece a explorar estas opções. Não precisa ser um setup gigante como o meu. Qualquer HD externo sobrando já dá pra começar. Comece pequeno, vá aumentando aos poucos. Eu coleciono essas coisas faz décadas! Não comecei hoje.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
