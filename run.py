#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable-msg=C0103, C0111

from flask import Flask, jsonify
from datetime import timezone, datetime

app = Flask(__name__)


def now():
    return datetime.now(timezone.utc)


@app.route("/hello")
def hello():
    result = {"type": "message", "timestamp": str(now()), "text": "Hello world!"}
    return jsonify(result)


if __name__ == "__main__":
    app.run(
        host="127.0.0.1", port=4044, debug=True, use_reloader=True, use_debugger=True
    )
    # 開発用設定。"./run.py&"でdebug & reloadモードで起動する
