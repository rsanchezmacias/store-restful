from flask_restful import Resource, reqparse
from models.store import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='name field is required')
    
    def get(self, name):
        store = StoreModel.find_by_name(name=name)
        if store: 
            response = store.json(), 200
        else: 
            response = { 'message': 'Store with name {} not found'.format(name) }, 404
        return response 
    
    def post(self, name):    
        existing_store = StoreModel.find_by_name(name=name)
        
        if existing_store:
            return { 'message': 'A store with name {} already exists.'.format(name) }, 400
        
        store = StoreModel(name=name)
        try: 
            store.save_to_db()
        except:
            return { 'message': 'An error has occured' }, 500
        
        return store.json(), 201
        
    def delete(self, name):
        existing_store = StoreModel.find_by_name(name=name)
        
        if existing_store:
            existing_store.delete_from_db()
            response = { 'message': 'Deleted store with name {}'.format(name) }, 200
        else:
            response = { 'message': 'Could not find store with given name {}'.format(name) }, 404
        
        return response 


class StoreList(Resource):
    
    def get(self):
        return { 'stores': list(map(lambda store: store.json(), StoreModel.select_all())) }, 200
