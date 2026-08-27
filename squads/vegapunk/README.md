# Squad Vegapunk — Dr. Vegapunk e os Satélites

Personas de Egghead (One Piece) sobre a memória de conhecimento do Fernando. O bot Telegram captura links e escreve o **Punk Records** (`knowledge/`); os Satélites são as formas de *usar* essa memória dentro do Claude Code.

| Punk | Agente | Faceta | Chame quando… | Comando-chave |
|---|---|---|---|---|
| 00 | 🧠 **Stella** | a soma | não sabe quem chamar; decisão grande | `*ask`, `*council` |
| 01 | 🪖 **Shaka** | bem | "vale a pena? é seguro? que triagem?" | `*judge`, `*risk` |
| 02 | 🏴‍☠️ **Lilith** | mal | "ataca essa ideia / isso é hype?" | `*attack`, `*hype-check` |
| 03 | 💡 **Edison** | pensamento | "o que eu poderia construir?" | `*ideas`, `*apply` |
| 04 | 📚 **Pythagoras** | sabedoria | "o que eu já sei sobre X?" | `*recall`, `*dossier` |
| 05 | 🔧 **Atlas** | violência | "faz / implementa / me explica" | `*build`, `*explain` |
| 06 | 🍩 **York** | ganância | "quanto custou / o que está preso?" | `*health`, `*cost` |

Invocação: `/vegapunk:agents:<id>` (ou `/vegapunk` para o Stella). Arquivos em `.claude/commands/vegapunk/agents/`.

Mapa do cânone → sistema: Punk Records = `knowledge/` · cabeça que cresce = `data/vegapunk.db` · Labophase = skills · Fabriophase = bot/pipeline · sincronização diária = `git push` · Mother Flame = tokens.
