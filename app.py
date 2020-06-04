from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Contact Class/Model
class Contact(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  channel = db.Column(db.String(200))
  value = db.Column(db.String(200))
  obs = db.Column(db.String(200))

  def __init__(self, name, channel, value, obs):
    self.name = name
    self.channel = channel
    self.value = value
    self.obs = obs

# Contact Schema
class ContactSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'channel', 'value', 'obs')

# Init schema
contact_schema = ContactSchema()
contacts_schema = ContactSchema(many=True)

# Create a Contact
@app.route('/contact', methods=['POST'])
def add_contact():
  name = request.json['name']
  channel = request.json['channel']
  value = request.json['value']
  obs = request.json['obs']

  new_contact = Contact(name, channel, value, obs)

  db.session.add(new_contact)
  db.session.commit()

  return contact_schema.jsonify(new_contact)

# Get All Contacts
@app.route('/contact', methods=['GET'])
def get_contacts():
  all_contacts = Contact.query.all()
  result = contacts_schema.dump(all_contacts)
  return jsonify(result)

# Get Single Contact
@app.route('/contact/<id>', methods=['GET'])
def get_contact(id):
  contact = Contact.query.get(id)
  return contact_schema.jsonify(contact)

# Update a Contact
@app.route('/contact/<id>', methods=['PUT'])
def update_contact(id):
  contact = Contact.query.get(id)

  name = request.json['name']
  channel = request.json['channel']
  value = request.json['value']
  obs = request.json['obs']

  contact.name = name
  contact.channel = channel
  contact.value = value
  contact.obs = obs

  db.session.commit()

  return contact_schema.jsonify(contact)

# Delete Contact
@app.route('/contact/<id>', methods=['DELETE'])
def delete_product(id):
  contact = Contact.query.get(id)
  db.session.delete(contact)
  db.session.commit()

  return contact_schema.jsonify(contact)

# Run
if __name__ == '__main__':
  app.run(debug=True)