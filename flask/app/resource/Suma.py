from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('x', help='Username flied cannot be blank', required=True)
parser.add_argument('y', help='Username flied cannot be blank', required=True)


class Wrapper:
    def __init__(self,parser):
        data = parser.parse_args()
        self.x = int(data['x'])
        self.y = int(data['y'])
    def suma(self):
        return self.x+self.y


class Suma(Resource):
    def post(self):
        def generate_result(value):
            return {"resultado": value}

        wrapper = Wrapper(parser)
        return generate_result(wrapper.suma()), 203