from flask_restful import Resource
from flask_restful import request

from app.send_message import SendWsp
from wsp.infra.wsp_repository import WspRepository


class ListenerWsp(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        SendWsp(WspRepository()).sendtxt()
        return {'mensaje': 'enviado'}