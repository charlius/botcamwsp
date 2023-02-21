import json
from flask_restful import Resource
from flask_restful import request

from src.app.camara import VideoCamera
from src.app.send_message import SendWsp
from src.wsp.infra.wsp_repository import WspRepository


class ListenerWsp(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        phone = request.form.get("phone")
        message = request.form.get("message").lower()
        op = request.form.get("op", "")
        print(f"entro data phone: {phone}, message: {message}")

        if "imagen" in message:
            name = VideoCamera().get_image()
            if name:
                SendWsp(WspRepository()).send_txt("Cargando imagen...")
                result = SendWsp(WspRepository()).send_image(name ,phone)
                print(json.dumps(result))
                return {'mensaje': result}, 200
        elif "video" in message:
            name = VideoCamera().get_video()
            if name:
                print(f"video enviando... {name}")
                result = SendWsp(WspRepository()).send_video(name ,phone)
                print(json.dumps(result))
                return {'mensaje': result}, 200

        result = SendWsp(WspRepository()).send_txt("Cargando imagen")
        print(json.dumps(result))
        return {'mensaje': 'enviado1'}, 200

