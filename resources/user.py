from models.user import UserModel
from flask_restful import Resource, reqparse


class UserRegistered(Resource): 
    
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, help='username is required', type=str)
    parser.add_argument('password', required=True, help='username is required', type=str)
    
    @classmethod
    def does_registered_user_exist_with(cls, username: str) -> bool:
        existing_user = UserModel.find_by_username(username=username)
        return existing_user != None
        
    
    def post(self):
        arguments = self.parser.parse_args()
        
        if UserRegistered.does_registered_user_exist_with(username=arguments['username']):
            return { 'message': 'Username {} is already taken'.format(arguments['username']) }, 400
        
        user = UserModel(**arguments)
        user.save_to_db()
        
        return { 'message': '{} account has been created '.format(arguments['username']) }, 201  
