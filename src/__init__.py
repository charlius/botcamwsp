from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from src.infra.webhook import CamOnline, HelloWorld
from src.infra.webhook import WebhookWsp
from src.infra.listener_wsp import ListenerWsp

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(ListenerWsp, '/listener/wsp')
api.add_resource(WebhookWsp, '/webhooks')

api.add_resource(HelloWorld, '/test')
api.add_resource(CamOnline, '/online/<op>')
