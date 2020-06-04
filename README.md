# flask1

Python 3.xでFlaskを使う最小のサンプルコード
(兼テンプレート)

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
(モジュールに関しては不明)


```sh
./stop_flask.sh
```
で終了


# Flaskのインストール

(TODO)
