---
item_id: "38a2dffc-1061-4995-a838-8f470c6cbaf8"
platform: article
external_id: "6e292cc70559"
canonical_url: "https://github.com/metafates/mangal"
channel: "Metafates · GitHub"
captured_at: 2026-09-05
status: discarded
triage: discard
tags: ["mangal", "cli-de-manga", "projeto-descontinuado", "scraper-lua", "risco-de-manutencao"]
applicability:
  saas_pessoal: nenhuma
  projeto_cliente: nenhuma
  estudo_geral: baixa
confidence: alta
theme: jogos-e-entretenimento
content_type: article
---

# mangal: leitor e downloader de mangá em linha de comando (descontinuado)

🔗 https://github.com/metafates/mangal

## Resumo

O mangal é um aplicativo de linha de comando para buscar, baixar e ler mangá, distribuído como binário único sem dependências de runtime, com uma interface de terminal e integração com o Anilist para metadados e sincronização de progresso. Seus diferenciais eram scrapers escritos em Lua 5.1, que permitiam adicionar qualquer fonte, quatro fontes embutidas, cache agressivo, histórico para retomar a leitura e exportação em PDF, CBZ, ZIP ou imagens soltas. A instalação cobria script único, AUR, Homebrew, Scoop, Termux, Gentoo, Nix e Docker. O aviso mais importante está no topo do README: desde abril de 2025 o projeto não é mais mantido. O autor agradece a quem usou e contribuiu, lembra que o código é aberto e pode ser bifurcado, e recomenda explicitamente não usá-lo como está, porque rodar software sem manutenção introduz risco de segurança.

## Tópicos

- **Descontinuação declarada** — Sem manutenção desde abril de 2025; o autor recomenda não usar como está por risco de segurança, e sugere bifurcar para quem quiser continuar.
- **Scrapers em Lua** — Qualquer fonte podia ser adicionada por um scraper Lua 5.1, além das quatro fontes embutidas.
- **Binário monolítico** — Zero dependências de runtime, com o próprio Lua embutido, rodando em Linux, macOS, Windows e Termux.

## Ferramentas citadas

- **Anilist**: fonte de metadados e sincronização de progresso de leitura
- **Lua 5.1**: linguagem dos scrapers de fonte, embutida no binário
- **Docker**: uma das formas de execução, montando volumes de downloads e configuração

## Pontos-chave

- Sem manutenção desde abril de 2025, com recomendação explícita do autor para não usar como está.
- Software sem manutenção é apontado pelo próprio autor como risco de segurança.
- Scrapers em Lua permitiam adicionar qualquer fonte sem recompilar.
- Exportava em PDF, CBZ, ZIP ou imagens soltas.
- Distribuído como binário único, sem dependências de runtime.
- É a dependência de download do Kaizoku, que herda o mesmo abandono.

## Como aplicar

Não aplicável aos projetos. Serve como aviso operacional: o Kaizoku depende dele, então adotar um arrasta o outro, ambos sem manutenção.

## 🏴‍☠️ Lilith diz

Morto desde abril de 2025, e quem diz isso é o próprio autor — na primeira linha, com a palavra risco de segurança escrita por extenso. Não fui eu que ataquei, ele se entregou. E olha a graça: o Kaizoku que você acabou de guardar depende deste defunto. Guardar a memória, tudo bem. Instalar, não.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Caution

As of April 2025, Mangal is no longer maintained. I am incredibly grateful to everyone who used it, contributed, or gave feedback along the way - thank you! Unfortunately, I just don't have the time to keep it going right now. That said, it's open source, so you're more than welcome to fork it, build on it, or maintain your own version. I might return to it someday, but for now, I don't recommend using it as-is - running unmaintained software can introduce security risks.

`curl -sSL mangal.metafates.one/run | sh`
**Note** This script does not install anything, it just downloads, verifies and runs Mangal.
Not available on Windows.


- **Lua Scrapers!!!** You can add any source you want by creating your own*(or using someone's else)* scraper with**Lua 5.1** . See mangal-scrapers repository
- **4 Built-in sources** - Mangadex, Manganelo, Manganato & Mangapill
- **Download & Read Manga** - I mean, it would be strange if you couldn't, right?
- **Caching** - Mangal will cache as much data as possible, so you don't have to wait for it to download the same data over and over again.
- **4 Different export formats** - PDF, CBZ, ZIP and plain images
- **TUI ✨** - You already know how to use it! (ﾉ>ω<)ﾉ :｡･::･ﾟ’★,｡･:･ﾟ’☆
- **Scriptable** - You can use Mangal in your scripts, it's just a CLI app after all. Examples
- **History** - Resume your reading from where you left off!
- **Fast?** - YES.
- **Monolith** - ZERO runtime dependencies. Even Lua is built in. Easy to install and use.
- **Cross-Platform** - Linux, macOS, Windows, Termux, even your toaster. (¬‿¬ )
- **Anilist integration** - Mangal will collect additional data from Anilist and use it to improve your reading experience. It can also sync your progress!

Install using this shell script

`curl -sSL mangal.metafates.one/install | sh`
This script will automatically detect OS & Distro and use the best option available.
For example, on macOS it will try to use Homebrew, on Ubuntu it will install the `.deb` package and so on...

AUR package (maintained by @balajsra, thank you)

Install using Homebrew

```
brew tap metafates/mangal
brew install mangal
```
Install using Scoop (thanks to @SonaliBendre for adding it to the official bucket)

```
scoop bucket add extras
scoop install mangal
```
Thanks to @T-Dynamos for adding it to the termux-packages

`pkg install mangal`
Install using third-party overlay raiagent. Thanks to @leycec for maintaining it.

```
eselect repository enable raiagent
emerge --sync raiagent
emerge mangal
```
Install using Nix. Thanks to @bertof for adding it to the nixpkgs

```
### NixOS
nix-env -iA nixos.mangal
### Non NixOS
nix-env -iA nixpkgs.mangal
```
Install using Docker. (thanks to @ArabCoders for reference)

```
docker pull metafates/mangal
```
To run

`docker run --rm -ti -e "TERM=xterm-256color" -v $(PWD)/mangal/downloads:/downloads -v $(PWD)/mangal/config:/config metafates/mangal`
Visit this link to install Go.

Clone the repo

```
git clone --depth 1 https://github.com/metafates/mangal.git
cd mangal
```
GNU Make **(Recommended)**

```
make install # if you want to compile and install mangal to path
make build # if you want to just build the binary
```
#### If you don't have GNU Make use this

```
### To build
go build -ldflags "-X 'github.com/metafates/mangal/constant.BuiltAt=$(date -u)' -X 'github.com/metafates/mangal/constant.BuiltBy=$(whoami)' -X 'github.com/metafates/mangal/constant.Revision=$(git rev-parse --short HEAD)' -s -w"
### To install
go install -ldflags "-X 'github.com/metafates/mangal/constant.BuiltAt=$(date -u)' -X 'github.com/metafates/mangal/constant.BuiltBy=$(whoami)' -X 'github.com/metafates/mangal/constant.Revision=$(git rev-parse --short HEAD)' -s -w"
```
If you want to build mangal for other architecture, say ARM, you'll have to set env variables `GOOS` and `GOARCH`

`GOOS=linux GOARCH=arm64 make build`
Available GOOS and GOARCH combinations

Download the pre-compiled binaries from the releases page and copy them to the desired location.

Just run `mangal` and you're ready to go.

#### Keybinds

| Bind | Description | 
|---|---|
| `?` | Show help | 
| `↑/j``↓/k``→/l``←/h` | Navigate | 
| `g` | Go to first | 
| `G` | Go to last | 
| `/` | Filter | 
| `esc` | Back | 
| `space` | Select one | 
| `tab` | Select all | 
| `v` | Select volume | 
| `backspace` | Unselect all | 
| `enter` | Confirm | 
| `o` | Open URL | 
| `r` | Read | 
| `q` | Quit | 
| `ctrl+c` | Force quit | 
| `a` | Select Anilist manga (chapters list) | 
| `d` | Delete single history entry | 

If you wonder what those icons mean - `D` stands for "downloaded", `*` shows that chapter is marked to be downloaded.
You can choose different icons, e.g. nerd font ones - just run mangal with `--icons nerd`.
Available options are `nerd`, `emoji`, `kaomoji` and `squares`


Mini mode tries to mimic ani-cli

To run: `mangal mini`

Inline mode is intended for use with other scripts.

Type `mangal help inline` for more information.

See Wiki for more examples.

See `mangal help` for more information

Mangal uses TOML format for configuration under the `mangal.toml` filename.
Config path depends on the OS.
To find yours, use `mangal where --config`.
For example, on **Linux** it would be `~/.config/mangal/mangal.toml`.

Use env variable `MANGAL_CONFIG_PATH` to set custom config path.

See `mangal env` to show all available env variables.


| Command | Description | 
|---|---|
| `mangal config get` | Get config value for specific key | 
| `mangal config set` | Set config value for specific key | 
| `mangal config reset` | Reset config value for specific key | 
| `mangal config info` | List all config fields with description for each | 
| `mangal config write` | Write current config to a file | 

TLDR; To browse and install a custom scraper from mangal-scrapers repository run

```
mangal sources install
```
Mangal has a Lua5.1 VM built-in + some useful libraries, such as headless chrome, http client, html parser and so on...

Check the defined modules for more information.

For scrapers examples, check the mangal-scrapers repository

This command will create `example.lua` file in the `mangal where --sources` directory.

```
mangal sources gen --name example --url https://example.com
```
Open the file and edit it as you wish. Take a look at the comments for more information. See mangal-scrapers repository for examples.

You can test it by running `mangal run <filepath>`

It should automatically appear in the list of available scrapers.

New to Lua? Quick start guide


Mangal also supports integration with anilist.

Besides fetching metadata for each manga when downloading, mangal can also mark chapters as read on your Anilsit profile when you read them inside mangal.

For more information see wiki

- kaizoku - Self-hosted manga downloader with mangal as its core 🚀

- mangadesk - Terminal client for MangaDex
- ani-cli - A cli tool to browse and play anime
- manga-py - Universal manga downloader
- animdl - A highly efficient, fast, powerful and light-weight anime downloader and streamer
- tachiyomi - Free and open source manga reader for Android

- bubbletea, bubbles & lipgloss - Made mangal shine! The best TUI libraries ever ✨
- gopher-lua - Made it possible to write custom scrapers with Lua ❤️
- cobra and viper - Responsible for the awesome CLI & config experience 🛠
- pdfcpu - Fast pdf processor in pure go 📄
- *And many others!*

And of course, thanks to all contributors! You are awesome!

If you find this project useful or want to say thank you, please consider starring it, that would mean a lot to me ⭐

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
