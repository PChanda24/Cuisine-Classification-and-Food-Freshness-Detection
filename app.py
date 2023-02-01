from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from time import strftime
import time

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Suyash/Documents/Capstone Code/food.db'

db = SQLAlchemy(app)

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    expdate = db.Column(db.DateTime, default=datetime.now)
    consumed = db.Column(db.Boolean)

@app.route('/')
def index():
    incomplete = Food.query.filter_by(consumed=False).all()
    consumed = Food.query.filter_by(consumed=True).all()
    today = datetime.now()

    return render_template('index.html', incomplete=incomplete, today=today, time=time)

@app.route('/add', methods=['POST'])
def add():
    food = Food(text=request.form['fooditem'], expdate=datetime.strptime(request.form['expdate'], '%Y-%m-%d'), consumed=False)
    db.session.add(food)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/consumed/<id>')
def consumed(id):

    food = Food.query.filter_by(id=int(id)).first()
    food.consumed = True
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)