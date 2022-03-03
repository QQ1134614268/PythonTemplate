# -*- coding:utf-8 -*-
"""
@Time: 2022/3/4
@Description:
"""
# todo

from flask import Flask
from flask_socketio import SocketIO
from flask_socketio import send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('message')
def handle_message(message):
    send(message)


@socketio.on('json')
def handle_json(json):
    send(json, json=True)


@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json)


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    return 'one', 2


def my_function_handler(data):
    pass


socketio.on_event('my event', my_function_handler, namespace='/test')


@socketio.on('my event', namespace='/test')
def handle_my_custom_namespace_event(json):
    print('received json: ' + str(json))


@socketio.event
def my_custom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)


@socketio.on('my_event')
def handle_my_custom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))


@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)


# @socketio.on_error()        # Handles the default namespace
# def error_handler(e):
#     pass
#
# @socketio.on_error('/chat') # handles the '/chat' namespace
# def error_handler_chat(e):
#     pass
#
# @socketio.on_error_default  # handles all namespaces without an explicit error handler
# def default_error_handler(e):
#     pass
if __name__ == '__main__':
    socketio.run(app)
