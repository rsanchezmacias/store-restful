from models.item import ItemModel
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from typing import Dict


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', required=True, type=float, help='price cannot be left empty')    
    parser.add_argument('store_id', required=True, type=int, help='store id cannot be left empty')    
    
    @jwt_required()
    def get(self, name: str) -> Dict:
        item = ItemModel.find_by_name(name=name)
         
        if item:
            return item.json(), 200
        
        return { 'message': 'No item found with name: {}'.format(name) }, 404
         
    @jwt_required()         
    def post(self, name: str) -> Dict:        
        data = self.parser.parse_args()
        
        existing_item = ItemModel.find_by_name(name=name)
        if existing_item:
            response = { 'message': 'Duplicate item with name: {}'.format(name) }, 400
        else:
            item = ItemModel(name=name, price=data['price'], store_id=data['store_id'])
            item.save_to_db()
            response = item.json(), 201
        
        return response
        
    @jwt_required()
    def delete(self, name: str) -> Dict: 
        item_to_delete = ItemModel.find_by_name(name=name)
        
        if item_to_delete:
            response = {'message': 'Deleted the item with name {}'.format(name) }, 200
        else:
            response = { 'message': 'No item found to delete' }, 404
        
        return response
        
    @jwt_required()
    def put(self, name: str) -> Dict:
        affected_item = ItemModel.find_by_name(name=name)
        data = self.parser.parse_args()
        
        if affected_item:
            affected_item.price = data['price']
            response = affected_item.json(), 204
        else:
            affected_item = ItemModel(name=name, price=data['price'], store_id=data['store_id'])
            response =  affected_item.json(), 201
        
        affected_item.save_to_db()
        return response    
    
    
class ItemList(Resource):
    @jwt_required()
    def get(self):    
        return { 'items': [item.json() for item in ItemModel.select_all()] }, 200

