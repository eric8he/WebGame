from flask_restful import Resource, reqparse


class UsersResource(Resource):

    def get(self):
        """
        test with http://127.0.0.1:5000/users?id=eric8he@gmail.com
        """
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True)
        args = parser.parse_args()
        return args.get('id')

    def post(self):
        """
        Test with json style
        curl -d '{"name": "dad"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/users

        or form submission style
        curl http://localhost:5000/users -d "name=something new&zip=12345" -X POST -v
        More cURL example at 

        https://gist.github.com/subfuzion/08c5d85437d5d4f00e58
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('zip', type=str, required=False)
        args = parser.parse_args()
        name = args.get('username')
        zipcode = args.get('zip')
        return 'Hi {}! zip:{}'.format(name, zipcode), 202
