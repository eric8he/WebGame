from flask_restful import Resource, reqparse


class UsersResource(Resource):

    def get(self):
        """
        test with http://127.0.0.1:5000/users?id=eric8he@gmail.com
        """
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True)
        args = parser.parse_args()
        return args.get('id'), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        args = parser.parse_args()
        return '', 202
