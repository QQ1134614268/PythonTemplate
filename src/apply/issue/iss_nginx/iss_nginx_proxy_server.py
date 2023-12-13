from flask import Flask, request

app = Flask(__name__)


@app.route('/<name1>')
def index(name1):
    print(request.full_path, name1)
    return request.full_path


@app.route('/<name1>/<name2>')
def index2(name1, name2):
    print(request.full_path, name1, name2)
    return request.full_path


@app.route('/<name1>/<name2>/<name3>')
def index3(name1, name2, name3):
    print(request.full_path, name1, name2, name3)
    return request.full_path


@app.route('/')
def hello():
    # request.path
    # request.host_url
    # request.query_string
    # request.root_url
    # request.root_path
    # request.url
    # request.url_root
    # request.url_rule
    # request.values
    print(request.full_path)
    return request.full_path


@app.errorhandler(404)  # 当发生404错误时，会被该路由匹配
def handle_404_error(err_msg):
    print(request.full_path)
    return "404: " + request.full_path


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=20090, debug=True, threaded=True)
