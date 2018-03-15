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
        """
        Test with
        curl -d '{"name": "dad"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/users

        More cURL example at 

        https://gist.github.com/subfuzion/08c5d85437d5d4f00e58
        """
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        args = parser.parse_args()
        name = args.get('name')
        return 'Hi {}!'.format(name), 202
