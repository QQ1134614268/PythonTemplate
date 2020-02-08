from time import time

from flask import Flask, request, abort, redirect
from flask import jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'todolist'

# app.config['MONGO_URI'] = 'mongodb://todo:towait.com@localhost:27017/todolist'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/todolist'

app.url_map.strict_slashes = False

mongo = PyMongo(app)


# CORS(app, supports_credentials=True)


@app.route("/", methods=['GET'])
def home_page():
    return "Hello World!"


class Todo(object):
    @classmethod
    def create_doc(cls, content):
        return {
            'content': content,
            'created_at': time(),
            'is_finished': False,
            'finished_at': None
        }


@app.route('/todo/', methods=['GET'])
def index():
    print("/todo/ GET")
    todos = list(mongo.db.todos.find({}))
    for i in todos:
        i["_id"] = str(i["_id"])
    return jsonify(todos)


@app.route('/todo/', methods=['POST'])
def add():
    print(request.form)
    content = request.form.get('content', None)
    if not content:
        abort(400)
    mongo.db.todos.insert(Todo.create_doc(content))
    return "/todo/ POST"


@app.route('/todo/<content>/finished')
def finish(content):
    print("finish GET")
    result = mongo.db.todos.update_one(
        {'content': content},
        {
            '$set': {
                'is_finished': True,
                'finished_at': time()
            }
        }
    )
    return redirect('/todo/')


@app.route('/todo/<content>')
def delete(content):
    result = mongo.db.todos.delete_one(
        {'content': content}
    )
    return redirect('/todo/')


@app.route('/todo/search/<content>')
def find(content):
    todos = list(mongo.db.todos.find(
        {'content': {"$regex": content}}
    ))
    for i in todos:
        i["_id"] = str(i["_id"])
    return jsonify(todos)


if __name__ == '__main__':
    app.run(debug=True)
