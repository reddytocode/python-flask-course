from flask_restful import reqparse, Resource

parser = reqparse.RequestParser()
parser.add_argument('username', help='Username flied cannot be blank', required=True)
parser.add_argument('password', help='Password field cannot be blank', required=True)


class Wrapper:

    def __init__(self, parser):
        data = parser.parse_args()
        self.username = data['username']
        self.password = data['password']


class Login(Resource):

    def post(self):
        success_message = {"message": "Welcome"}
        error_message = {"message": "Error creating User"}
        #lamdas
        wrapper = Wrapper(parser)
        return success_message

