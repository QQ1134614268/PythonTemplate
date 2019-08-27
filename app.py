# encoding: utf-8
from flask import Flask, jsonify

app = Flask(__name__)
# 跨域
# swagger
a = ["kk"]
b = 1


@app.route("/")
def hello():
    return "jk"


@app.route("/change")
def change():
    a.append("kk")
    global b
    b = 2
    return jsonify({"data": a})


@app.route("/get")
def get():
    print(globals())
    return jsonify({"data": a})


@app.route("/get_b")
def get_b():
    return jsonify({"data": b})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True, threaded=True)
