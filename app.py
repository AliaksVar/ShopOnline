from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from cloudipsp import Api, Checkout

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    quantity = db.Column(db.Integer)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return self.title

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/buy/<int:id>')
def item_buy(id):

  #  item = Item.query.get(id)

 #   api = Api(merchant_id=1396424,
 #             secret_key='test')
 #   checkout = Checkout(api=api)
 #   data = {
 #       "currency": "USD",
#        "amount": item.price
#   }
#    url = checkout.url(data).get('checkout_url')
    return str(id) #url

@app.route('/products')
def products():
    items = Item.query.order_by(Item.price).all()
    return render_template('products.html',data=items)

@app.route('/create', methods=['POST','GET'])
def create():
    if request.method =='POST':
        title = request.form['title']
        price = request.form['price']
        quantity=request.form['quantity']
        text =request.form['text']

        item = Item(title=title, price=price, quantity=quantity, text =text)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return "Произошла ошибка"
    else:
        return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)