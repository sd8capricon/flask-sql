from flask import Flask, render_template, request, redirect
from db_utils import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        data = get_reviews()
        return render_template('index.html', data=data)
    except Exception as e:
        return {'error': e}


@app.route('/create-review', methods=['POST'])
def create():
    restaurant = request.form['restaurant']
    review = request.form['review']
    try:
        create_review(restaurant, review)
        return redirect('/')
    except Exception as e:
        return {'error': e}


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        update_review(id, request.form['restaurant'], request.form['review'])
        return redirect('/')
    else:
        restaurant = get_restaurant(id)
        return render_template('update.html', data=restaurant)


@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    delete_review(id)
    return redirect('/')
