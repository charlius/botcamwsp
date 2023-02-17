from flask_restful import Resource
from flask_restful import request


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'hello': 'world'}


class WebhookWsp(Resource):
    def post(self):
        token ="botwsp"
        clave = request.args.get("hub_challenge")
        verify_token = request.args.get("hub_verify_token")
        print(clave)
        print(verify_token)
        if verify_token == token:
            return clave

    def get(self):
        data = request.args
        print(data)