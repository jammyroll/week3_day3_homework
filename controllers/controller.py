from flask import render_template
from models.orders import all_orders

from app import app

@app.route('/shop')
def index():
    return render_template('index.html',title='Orders',order=all_orders)

@app.route('/shop/<id>')
def order(id):
    return render_template('order.html',title='single Order',single_order=all_orders[int(id)])