from flask_restful import Resource, reqparse


class UsersResource(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True)
        args = parser.parse_args()
        return args.get('id')

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=False)
        args = parser.parse_args()
        name = args.get('username')
        password = args.get('password')
        return 'Hi {}! Your password:{}'.format(name, password), 202
