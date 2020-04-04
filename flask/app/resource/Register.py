from flask_restful import reqparse, Resource
from app.models.UserModel import UserModel


parser = reqparse.RequestParser()
parser.add_argument('username', help='Username flied cannot be blank', required=True)
parser.add_argument('password', help='Password field cannot be blank', required=True)


class Wrapper:

    def __init__(self, parser):
        data = parser.parse_args()
        self.username = data['username']
        self.password = data['password']


class Register(Resource):

    def post(self):
        success_message = {"message": "Registered Successfully"}
        error_message = {"message": "Error creating User"}

        #lamdas
        wrapper = Wrapper(parser)
        register_db_response = UserModel.register(wrapper.username, wrapper.password)
        if(register_db_response == 200):
            return success_message, register_db_response
        else:
            return error_message, register_db_response


