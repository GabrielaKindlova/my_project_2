from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import Clients


client_section = Blueprint('client_section', __name__)


@client_section.route('/new_client', methods=['POST'])                
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

               # if len(firstname) <3:
        # else:
        #     flash('accout created', category='success')

        # if not request.form.get('firstName') or not request.form.get('lastName') or not request.form.get('city') or not request.form.get('addr') or not request.form.get('zip'):
        #     flash('vyplňte všechna pole', 'error')
        # else:
            # clients = clients(request.form.get('firstName'), request.form.get('lastName'), request.form.get('city'),
            # request.form.get('addr'),  request.form.get('zip') )
            # flash('Record was successfully added') 
        # else:
        #     client = Clients(firstName=firstName, lastName=lastName, addr=addr, 
        #     city=city, zip=zip)
        #     db.session.add(client)
        #     db.session.commit()
        #     flash('Account created!', category='success')          

    # return render_template("sign_up.html", user=current_user)           
                
    return render_template('new_client.html')
 
         

@client_section.route('/overview', methods=['GET', 'POST'])
def overview():
    return render_template("overview.html", text= "testování")
pass

 