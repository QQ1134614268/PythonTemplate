# -*- coding:utf-8 -*-
"""
@Time: 2023/6/14
@Description:
"""
import datetime
import os

from flask import Flask, request, make_response
from flask_cors import CORS

app = Flask(__name__, template_folder=os.path.abspath(os.path.dirname(__file__)))
CORS(app)


@app.route('/')
def index():
    # return 'hello'

    # return 'index.html'

    # file = open("index.html", 'r', encoding="UTF-8")
    # io_file = io.StringIO(file.read())
    # return render_template_string(io_file)

    with open("index.html", 'r', encoding="UTF-8") as f:
        lines = f.readlines()
    # return render_template_string("".join(lines))
    return "".join(lines)


@app.route('/has/cache', methods=["GET", "POST"])
def has_cache():
    response = make_response({
        'txt': '被缓存的数据, 服务端生成时间戳为：',
        'timestamps': datetime.datetime.now()
    })
    res_cache = request.args.get('resCache') or request.headers.get('resCache')
    if res_cache:
        response.headers['Cache-Control'] = res_cache

    if request.args.get('lastModified') or request.headers.get('lastModified'):
        response.headers['Cache-Control'] = 'no-cache'
        response.headers['Last-Modified'] = request.args.get('lastModified') or request.headers.get('lastModified')

    if request.args.get('Etag') or request.headers.get('Etag'):
        response.headers['Cache-Control'] = 'no-cache'
        response.headers['Etag'] = request.args.get('Etag') or request.headers.get('Etag')

    # 模拟协商缓存,返回304
    if request.headers.get('status'):
        response.headers['Last-Modified'] = 'Thu, 14 Dec 2023 22:22:22 GMT'
        return response, request.headers.get('status')

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3009, debug=True, threaded=True)
