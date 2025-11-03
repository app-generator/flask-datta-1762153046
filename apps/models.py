# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Users(db.Model):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)

    #__Users_FIELDS__
    user_id = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(255),  nullable=True)
    email = db.Column(db.String(255),  nullable=True)
    password = db.Column(db.String(255),  nullable=True)
    role = db.Column(db.String(255),  nullable=True)

    #__Users_FIELDS__END

    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)


class Pet_Owners(db.Model):

    __tablename__ = 'Pet_Owners'

    id = db.Column(db.Integer, primary_key=True)

    #__Pet_Owners_FIELDS__
    phone = db.Column(db.String(255),  nullable=True)

    #__Pet_Owners_FIELDS__END

    def __init__(self, **kwargs):
        super(Pet_Owners, self).__init__(**kwargs)


class Pets(db.Model):

    __tablename__ = 'Pets'

    id = db.Column(db.Integer, primary_key=True)

    #__Pets_FIELDS__
    name = db.Column(db.String(255),  nullable=True)
    species = db.Column(db.String(255),  nullable=True)
    breed = db.Column(db.String(255),  nullable=True)
    age = db.Column(db.Integer, nullable=True)

    #__Pets_FIELDS__END

    def __init__(self, **kwargs):
        super(Pets, self).__init__(**kwargs)


class Veterinarians(db.Model):

    __tablename__ = 'Veterinarians'

    id = db.Column(db.Integer, primary_key=True)

    #__Veterinarians_FIELDS__
    specilization = db.Column(db.String(255),  nullable=True)
    clinic_name = db.Column(db.String(255),  nullable=True)
    contact = db.Column(db.String(255),  nullable=True)

    #__Veterinarians_FIELDS__END

    def __init__(self, **kwargs):
        super(Veterinarians, self).__init__(**kwargs)


class Appointments(db.Model):

    __tablename__ = 'Appointments'

    id = db.Column(db.Integer, primary_key=True)

    #__Appointments_FIELDS__
    appointment_id = db.Column(db.Integer, nullable=True)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    time = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(255),  nullable=True)

    #__Appointments_FIELDS__END

    def __init__(self, **kwargs):
        super(Appointments, self).__init__(**kwargs)


class Ngos(db.Model):

    __tablename__ = 'Ngos'

    id = db.Column(db.Integer, primary_key=True)

    #__Ngos_FIELDS__
    org_name = db.Column(db.String(255),  nullable=True)
    location = db.Column(db.String(255),  nullable=True)
    contact = db.Column(db.String(255),  nullable=True)

    #__Ngos_FIELDS__END

    def __init__(self, **kwargs):
        super(Ngos, self).__init__(**kwargs)


class Events(db.Model):

    __tablename__ = 'Events'

    id = db.Column(db.Integer, primary_key=True)

    #__Events_FIELDS__
    event_id = db.Column(db.Integer, nullable=True)
    title = db.Column(db.String(255),  nullable=True)
    description = db.Column(db.Text, nullable=True)
    event_type = db.Column(db.String(255),  nullable=True)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    location = db.Column(db.String(255),  nullable=True)

    #__Events_FIELDS__END

    def __init__(self, **kwargs):
        super(Events, self).__init__(**kwargs)


class Event_Registrations(db.Model):

    __tablename__ = 'Event_Registrations'

    id = db.Column(db.Integer, primary_key=True)

    #__Event_Registrations_FIELDS__
    registered_on = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Event_Registrations_FIELDS__END

    def __init__(self, **kwargs):
        super(Event_Registrations, self).__init__(**kwargs)



#__MODELS__END
