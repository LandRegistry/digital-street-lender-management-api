from lender_management_api.extensions import db
import json


class User(db.Model):
    """Class representation of a User."""
    __tablename__ = 'user'

    # Fields
    identity = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email_address = db.Column(db.String, nullable=False, unique=True, index=True)
    phone_number = db.Column(db.String, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.address_id'), nullable=False)

    # Relationships
    address = db.relationship("Address", backref=db.backref('users', lazy='dynamic'), uselist=False)

    # Methods
    def __init__(self, identity, first_name, last_name, email, phone, address):
        self.identity = identity
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email.lower()
        self.phone_number = phone
        self.address = address

    def __repr__(self):
        return json.dumps(self.as_dict(), sort_keys=True, separators=(',', ':'))

    def as_dict(self):
        return {
            "identity": self.identity,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email_address": self.email_address,
            "phone_number": self.phone_number,
            "address": self.address.as_dict()
        }


class Address(db.Model):
    """Class representation of a Address."""
    __tablename__ = 'address'

    # Fields
    address_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    house_name_number = db.Column(db.String, nullable=False)
    street = db.Column(db.String, nullable=False)
    town_city = db.Column(db.String, nullable=False)
    county = db.Column(db.String, nullable=True)
    country = db.Column(db.String, nullable=False)
    postcode = db.Column(db.String, nullable=False)

    # Methods
    def __init__(self, house_name_number, street, town_city, county, country, postcode):
        self.house_name_number = house_name_number
        self.street = street
        self.town_city = town_city
        self.county = county
        self.country = country
        self.postcode = postcode

    def __repr__(self):
        return json.dumps(self.as_dict(), sort_keys=True, separators=(',', ':'))

    def as_dict(self):
        return {
            "house_name_number": self.house_name_number,
            "street": self.street,
            "town_city": self.town_city,
            "county": self.county,
            "country": self.country,
            "postcode": self.postcode
        }
