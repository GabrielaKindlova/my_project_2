from . import db


class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    addr = db.Column(db.String(150))
    city = db.Column(db.String(150))
    zip = db.Column(db.String(6))
    
# def __init__(self, firstName, lastName, city, addr, zip):
#    self.firstName = firstName
#    self.lastName = lastName
#    self.addr = addr
#    self.city = city
#    self.zip = zip
    

  
    