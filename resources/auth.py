from models.user import UserModel
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token 


def authenticate(username, password):
    user = UserModel.find_by_username(username=username)
    
    if user and password == user.password:
        return user 
    
    return None


class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(username, password)
        if user:
            access_token = create_access_token(identity=username)
            return { 'access_token': access_token }, 200
        
        return { 'message': 'Bad username or password'}, 400
        
