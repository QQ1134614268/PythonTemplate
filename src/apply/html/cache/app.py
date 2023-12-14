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

    # file = open("index.html", 'r', encoding="UTF-8")
    # io_file = io.StringIO(file.read())
    # return render_template_string(io_file)

    with open("index.html", 'r', encoding="UTF-8") as f:
        lines = f.readlines()
    # return render_template_string("".join(lines))
    return "".join(lines)


@app.route('/has/cache')
def has_cache():
    response = make_response({
        'txt': '被缓存的数据, 服务端生成时间戳为：',
        'timestamps': datetime.datetime.now()
    })
    # cache_control_header = request.headers.get('Cache-Control')
    cache_control_header = request.args.get('Cache-Control') or request.headers.get('Cache-Control')
    if cache_control_header:
        response.headers['Cache-Control'] = cache_control_header
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3009, debug=True, threaded=True)
