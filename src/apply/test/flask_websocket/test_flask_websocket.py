# -*- coding:utf-8 -*-
from flask import Flask, send_file
from flask_socketio import SocketIO, emit, send

"""
Python: # https://blog.csdn.net/xietansheng/article/details/115558069
websocket: flask_socketio, Flask 本身并不直接支持 WebSocket,使用第三方库
异步服务器: eventlet | gevent; 避免阻塞,可以支持更多链接
"""
app = Flask(__name__, template_folder='./template')
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')  # async_mode='eventlet' 或者 'gevent'


@app.route('/')
def index():
    # return render_template('index_socketio.html')
    return send_file('./template/socketio.vue.html')


@socketio.on('connect')
def test_connect():
    print('connect')
    emit('connectRes', {'path': '/connect', 'code': 1, 'data': 'connected'})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


@socketio.on('message')
def test_message(msg: str):
    print('messageRes: ' + msg)
    emit('messageRes', {'path': '/message', 'code': 1, 'data': msg})


@socketio.on('json')
def test_json(json):
    print('json: ' + str(json))
    emit('jsonRes', {'path': '/json', 'code': 1, 'data': json})


@socketio.on('hello')
def test_connect(msg):
    print('hello', msg)
    emit('helloRes', {'path': '/hello', 'code': 1, 'data': 'hello client'})


@socketio.on('add')
def add(a, b):
    print('add ', a, b)
    emit('addRes', {'path': '/add', 'code': 1, 'data': a + b})


@socketio.on('send')
def test_websocket_send(json):
    print('send: ' + str(json))
    # , room=request.sid, broadcast=True
    send({'path': '/send', 'desc': 'json', 'code': 1, 'data': json}, json=True)
    send({'path': '/send', 'desc': 'message', 'code': 1, 'data': json}, json=False)


if __name__ == '__main__':
    socketio.run(app, debug=True)
