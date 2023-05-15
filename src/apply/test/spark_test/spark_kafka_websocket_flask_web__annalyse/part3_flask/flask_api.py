# -*- coding:utf-8 -*-
"""
@Time: 2022/3/4
@Description:
"""
import os

from flask import Flask, render_template
from flask_socketio import SocketIO
from kafka import KafkaConsumer

from apply.test.spark_test.spark_kafka_websocket_flask_web__annalyse.spark_kafka_conf import KAFKA_LOCAL

app = Flask(__name__, template_folder=os.path.abspath(os.path.dirname(__file__)))
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None


# 接收到消息就调用test_message方法，test_message是定义在web_socket对象上的js函数
def background_thread():
    consumer = KafkaConsumer('result', bootstrap_servers=[KAFKA_LOCAL], group_id="KEY")
    for msg in consumer:
        data_json = msg.value.decode('utf8')
        socketio.emit('test_message', {'data': data_json})


# JS代码中可以调用这个装饰器下的视图函数，以初始化消费者监听kafka
@socketio.on('test_connect')
def connect(message):
    print(message)
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)
    socketio.emit('connected', {'data': 'Connected'})


# 返回一个html页面
@app.route("/")
def handle_mes():
    return render_template("part4_web_index.html")


if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0", port=19090)
