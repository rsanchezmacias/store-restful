import os 

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager  

from db_a import Base, engine
from resources.user import UserRegistered
from resources.item import Item, ItemList
from resources.auth import Login
from resources.store import Store, StoreList


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///db/data.db').replace('postgres', 'postgresql')

app.config["JWT_SECRET_KEY"] = "this_is_my_secret_key"  
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
jwt = JWTManager(app)

# Endpoints
api.add_resource(Item, '/item/<string:name>')  
api.add_resource(ItemList, '/items')
api.add_resource(Login, '/login')
api.add_resource(UserRegistered, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

@app.before_first_request
def create_tables():
    Base.metadata.create_all(engine)
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)
