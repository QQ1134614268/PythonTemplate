```
Python: # https://blog.csdn.net/xietansheng/article/details/115558069
websocket: flask_socketio, Flask 本身并不直接支持 WebSocket,使用第三方库
异步服务器: eventlet | gevent; 避免阻塞,可以支持更多链接
```    
```
场景:
    A -> 发送给B, 发送给C; 发送给A,B;
    群组消息
    系统推送给所有用户

    post发布消息, 触发推送消息, 推送一个人,推送全部
    页面, 连接,发送,token, 回显, 前后分离
```
