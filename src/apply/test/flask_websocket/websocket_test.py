# -*- coding:utf-8 -*-
"""
@Time: 2022/3/4
@Description:
"""
# todo

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_socketio import send

app = Flask(__name__, template_folder='.')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index_socketio.html')


# @socketio.on('connect', namespace='/test_conn')
# def test_connect():
#     emit('server_response', {'data': 'connected'}, namespace='/test_conn')


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
