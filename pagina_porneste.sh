#!/bin/sh
# Porneste pagina de intrebari FiscalOS daca nu ruleaza deja (apelat din cron la @reboot si la 5 minute).
# Separata de iConta: alt port (8030, numai 127.0.0.1), alt director, alte date.
cd "$(dirname "$0")" || exit 1
mkdir -p pagina_date
if [ -f pagina_date/pagina.pid ] && kill -0 "$(cat pagina_date/pagina.pid)" 2>/dev/null; then
    exit 0
fi
nohup venv/bin/python -m fiscalos.pagina >> pagina_date/pagina.log 2>&1 &
echo $! > pagina_date/pagina.pid
