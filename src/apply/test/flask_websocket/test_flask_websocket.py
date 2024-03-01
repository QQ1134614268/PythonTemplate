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

app = Flask(__name__, template_folder=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'template'))
# socketio = SocketIO(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# 安装完成后，我们可以在 Flask 应用中引入 eventlet 并使用其提供的 WebSocket 服务器来处理 WebSocket 连接。


@app.route('/')
def index():
    return render_template('index_socketio.html')


@socketio.on('hello')
def test_connect(msg):
    print('hello', msg)
    emit('server_response', {'data': 'hello client'})


@socketio.on('connect2')
def test_connect():
    print('test_connect')
    emit('server_response', {'data': 'connected'})


@socketio.on('add')
def add(a, b):
    print(a + b)
    emit('server_response', {'path': '/add', 'data': 'connected'})


@socketio.on('json')
def handle_json(json):
    print('json: ' + str(json))
    send(json, json=True)
    emit('json', json)


if __name__ == '__main__':
    socketio.run(app)
