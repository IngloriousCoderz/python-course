from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"


# try this after adding --debug
# 2 + "2"

# try http://localhost:5000/<script>alert('Gotcha!') (nothing bad really happens)
@app.route("/<name>")
def hello(name):
    # return f"Hello, {name}"
    return f"Hello, {escape(name)}"


@app.route("/ultimate-question/<int:answer>")
def fundamental_question(answer):
    return f"The Answer to the ultimate question of Life, the Universe, and Everything, is {answer}"


# try little/pigs, blind/mice
@app.route("/three/<path:subpath>")
def three(subpath):
    return f"Three {' '.join(escape(subpath).split('/'))}"

# converter types: string (default), int, float, path, uuid

# trailing slash can be omitted, will be directed to /projects/


@app.route('/projects/')
def projects():
    return 'The project page'

# adding a trailing slash will give 404
# also, note how this overrides the route above ("/<name>")


@app.route('/about')
def about():
    return 'The about page'
