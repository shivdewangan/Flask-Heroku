from flask_restful import Resource, reqparse
from models.userModel import UserModel

class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,help="This  field cant be blank")
    parser.add_argument('password', type=str,required=True,help="This  field cant be blank")
    
    def post(self):
        data = UserResource.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400
        
        user = UserModel(data['username'], data['password'])
        user.save_to_db()
        return {"message": "User created successfully."}, 201