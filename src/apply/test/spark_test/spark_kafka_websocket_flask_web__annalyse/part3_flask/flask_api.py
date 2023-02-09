# -*- coding:utf-8 -*-
"""
@Time: 2022/3/4
@Description:
"""
from flask import Flask, render_template
from flask_socketio import SocketIO
from kafka import KafkaConsumer

from config.kafka_conf import KAFKA_GGOK

app = Flask(__name__, template_folder='.')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None


# 接收到消息就调用test_message方法，test_message是定义在web_socket对象上的js函数
def background_thread():
    consumer = KafkaConsumer('result', bootstrap_servers=[KAFKA_GGOK], group_id="KEY")
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
    socketio.run(app, debug=True)
