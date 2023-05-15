# -*- coding:utf-8 -*-
"""
@Time: 2022/3/4
@Description:

# todo 重要 (java 也需要), flask websocket
场景:
    A -> 发送给B, 发送给C; 发送给A,B;
    群组消息
    系统推送给所有用户

    post发布消息, 触发推送消息, 推送一个人,推送全部
    页面, 连接,发送,token, 回显, 前后分离
"""
import os

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_socketio import send

app = Flask(__name__, template_folder=os.path.abspath(os.path.dirname(__file__)))
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index_socketio.html')


@app.route('/create_msg')
def create_msg():
    return render_template('index_socketio.html')


@socketio.on('connect')
def test_connect(data):
    print(data)
    emit('server_response', {'data': 'connected'}, namespace='/test_conn')


@socketio.on('my_event')
def my_event(json):
    print('my_event: ' + str(json))
    send(json, json=True)
    emit('web_event', json)
    return 'one', 2


@socketio.on('json')
def handle_json(json):
    print('json: ' + str(json))
    send(json, json=True)


if __name__ == '__main__':
    socketio.run(app)
