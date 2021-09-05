import os
import re

from datetime import timedelta
from db import db
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserRegister
from security import authenticate, identity
from resources.item import Item, ItemList
from resources.store import Store, StoreList



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URLA',
                                                       'postgres://mbbfjdfdhjafxe:33c11e1db66fde27b6e083127ca5613fc3f9d507cb4d325814348106e9f58a71@ec2-107-22-18-26.compute-1.amazonaws.com:5432/deqnaume1lid47')
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.secret_key = 'Jatin'
api = Api(app)

# changing the default token expiry time
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=30)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

api.add_resource(ItemList, '/items')

api.add_resource(Item, '/item/<string:name>')

api.add_resource(UserRegister, '/register')

# to avoid run this file in case of an import is done for app.py
if __name__ == '__main__':
    from db import db

    db.init_app(app)

    app.run(port=5000)
