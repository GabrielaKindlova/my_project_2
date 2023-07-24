from website import create_app
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


app = create_app()
db = SQLAlchemy(app)

class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    addr = db.Column(db.String(150))
    city = db.Column(db.String(150))
    zip = db.Column(db.String(6))


@app.route('/')
def home():
   return render_template("home.html")

from flask import Blueprint, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash


client_section = Blueprint('client_section', __name__)


app.route('/new_client', methods=['POST'])                
def new_client():
    if request.method == 'POST':
        firstName = request.form.get ('firstName')
        lastName = request.form.get ('lastName')
        addr = request.form.get ('addr')
        city = request.form.get ('city')
        zip = request.form.get ('zip') 
        
        client = Clients.query.all()
        
        new_client = Clients(firstName=firstName, lastName=lastName, addr=addr, 
            city=city, zip=zip)   
        
        db.session.add(new_client)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
