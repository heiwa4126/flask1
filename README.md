# flask1

Python 3.xでFlaskを使う最小のサンプルコード
(兼テンプレート)

- [flask1](#flask1)
- [使い方](#使い方)
- [Flaskのインストール](#flaskのインストール)
- [注意](#注意)
- [参考](#参考)


# 使い方

```sh
./start_flask.sh
```
で開始(デバッグモード&オートリロード)

```sh
./test_flask.sh
```
でテスト。こんなの↓が帰る

```json
{
  "text": "Hello world!",
  "timestamp": "2020-06-04 08:52:06.153123+00:00",
  "type": "message"
}
```

オートリロードなので`run.py`を編集すると再読込してくれる
(モジュールに関しては不明)。


```sh
./stop_flask.sh
```
で終了


# Flaskのインストール

(TODO)

Debian/Ubuntuなら
```sh
sudo apt install uwsgi python3-flask
```


# 注意

この設定のまま本番で使わないこと。

- [Flaskのデフォルトでは同時アクセスを処理できない - Qiita](https://qiita.com/5zm/items/251be97d2800bf67b1c6)

まあ本番ならuWSGI使うだろうと思いますが。

# 参考

- [Welcome to Flask — Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja — Jinja Documentation](https://jinja.palletsprojects.com/)
- [Werkzeug — Werkzeug Documentation](https://werkzeug.palletsprojects.com/)
