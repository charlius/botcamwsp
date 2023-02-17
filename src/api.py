from flask import Flask
from flask_restful import Api

from src.infra.webhook import HelloWorld
from src.infra.webhook import WebhookWsp
from src.infra.listener_wsp import ListenerWsp

app = Flask(__name__)
api = Api(app)


api.add_resource(ListenerWsp, '/listener/wsp')
api.add_resource(WebhookWsp, '/webhooks')

api.add_resource(HelloWorld, '/test')
if __name__ == '__main__':
    app.run(port=80)