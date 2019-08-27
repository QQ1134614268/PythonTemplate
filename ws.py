# encoding: utf-8

import json

from flask import Flask, render_template, request
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.websocket import WebSocket

app = Flask(__name__, template_folder=".")

user_socket_dict = {}


@app.route("/ws/<username>")  # 同flask的路由，username是为了区分用户名
def we(username):
    print(username)
    user_socket = request.environ.get('wsgi.websocket')  # type:WebSocket  #相当于连接的那把伞，成功连接后意味着可以进行通信了
    ## type:WebSocket ：作用，使定义的user_socket拥有很多属性
    if user_socket:
        user_socket_dict[username] = user_socket  # 将用户登录时对信息存储,为了下次找到发送的对象
    while 1:
        msg = user_socket.receive()  # 通过"伞".receive()接收那个信息数据
        print(msg)
        msg_dict = json.loads(msg)
        msg_dict["from_user"] = username  # 返回客户端发送数据的用户名
        to_user = msg_dict.get("to_user")
        u_socket = user_socket_dict.get(to_user)  # type:WebSocket  #找到要发送数据的的人
        # 通过"伞".receive()获取那个信息 找出send属性
        u_socket.send(json.dumps(msg_dict))  # 通过后端发送给要发送的人,服务器模拟发送,u_socket就是那把伞
        # 通过"伞".send发送数据


@app.route("/")
def index():
    return render_template("ws.html")


if __name__ == '__main__':
    http_serv = WSGIServer(('0.0.0.0', 9527), app, handler_class=WebSocketHandler)  # 找对象
    http_serv.serve_forever()  # 对象的属性
