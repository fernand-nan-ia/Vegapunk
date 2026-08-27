# Task: vegapunk-healthcheck

Executada por York (`*health`). Somente leitura.

| Verificação | Comando | Atenção se |
|---|---|---|
| container | `docker compose ps` | não `Up` |
| erros recentes | `docker compose logs --tail 200` | `ERROR`/`extraction_failed` repetido |
| estados | `select status,count(*) from knowledge_items group by status` | `extraction_failed` > 0, `enriched` (sem triagem) > 5 |
| pendentes | `ls punk_records/_pending` | qualquer arquivo |
| yt-dlp | versão no container vs PyPI | diferente (causa nº 1 de falha) |
| disco | `du -sh data whisper-cache` | > 2 GB |

Saída: tabela + 1 recomendação com custo em minutos. Ações destrutivas: descrever e pedir.
