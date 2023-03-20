from flask import Flask, render_template, request, redirect
from db_utils import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Hello World"
    # return render_template("index.html")


@app.route('/create-review', methods=['POST'])
def create():
    pass


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        pass
    else:
        pass


@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    pass
