from models.user import UserModel
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token 


''' JWT-Extended
Disabled for now, but just add jwt_required decorator to any function you want 
to secure access 
'''

''' With the db, we can replace these two mappings '''
# username_mapping = { user.username: user for user in users}
# userid_mapping = { user.id: user for user in users }

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
        
