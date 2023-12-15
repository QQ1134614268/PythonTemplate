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
    cache_control_header = request.args.get('Cache-Control') or request.headers.get('Cache-Control')
    if cache_control_header:
        response.headers['Cache-Control'] = cache_control_header

    if request.args.get('lastModified') or request.headers.get('lastModified'):
        response.headers['Cache-Control'] = 'no-cache'
        response.headers['Last-Modified'] = request.args.get('lastModified') or request.headers.get('lastModified')

    if request.args.get('Etag') or request.headers.get('Etag'):
        response.headers['Cache-Control'] = 'no-cache'
        response.headers['Etag'] = request.args.get('Etag') or request.headers.get('Etag')

    #                 If-None-Match:协商缓存; 请求时携带 Etag的值; 优先级高于if-modified-since; 缓存有效服务器响应304;
    #                 if-modified-since:协商缓存; 请求时携带Last-modified的值; 缓存有效服务器响应304;

    if request.headers.get('status'):
        response.headers['Last-Modified'] = 'Thu, 14 Dec 2023 22:22:22 GMT'
        return response, 304

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3009, debug=True, threaded=True)
