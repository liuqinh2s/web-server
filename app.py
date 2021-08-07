from flask import Flask, request
import pika
import json

app = Flask(__name__)

# 创建socket实例，声明管道
connect = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connect.channel()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/register', methods=["POST"])
def register():
    apiKey = request.form.get('api-key')
    secretKey = request.form.get('secret-key')
    notifyUid = request.form.get('notify-uid')
    quantity = request.form.get('quantity')
    leverage = request.form.get('leverage')
    contact = request.form.get('contact')
    username = request.form.get('contact')

    keys = 'register'
    message = {"apiKey": apiKey, "secretKey": secretKey, "notifyUid": notifyUid, "quantity": quantity,
               "leverage": leverage, 'contact': contact, 'username': username}
    channel.basic_publish(
        exchange="",
        routing_key=keys,
        body=json.dumps(message)
    )
    print("send %s  %s" % (keys, message))
    return 'register success!'


@app.route('/stop', methods=["POST"])
def stop():
    pass


if __name__ == '__main__':
    app.run()
