#!/bin/sh
# Flaskのデバックモードで起動する。
# debuggerとautoreloadが有効になる
# あと複数リクエストは処理できない(--with-threads)
# 止めるときは./stop_flask.sh

export FLASK_ENV=development
export FLASK_APP=run.py

flask run --port 4044 &

sleep 0.5
ps xf | fgrep "flask run" | fgrep -v grep
