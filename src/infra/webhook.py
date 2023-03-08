from flask import Response
from flask import  render_template
from flask_restful import Resource
from flask_restful import request
from src.app.camara import VideoCamera

from src.app.send_message import SendWsp
from src.wsp.infra.wsp_repository import WspRepository

class CamOnline(Resource):
    def gen(self, camera):
        while True:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    def get(self, op):
        print(op)
        if "vivo" in op:
            return Response(self.gen(VideoCamera()),
                        mimetype='multipart/x-mixed-replace; boundary=frame')


class HelloWorld(Resource):
    def get(self):
        return render_template('index.html')

    def post(self):
        data = request.form.get("data")
        print(f"entro data {data}")
        result =SendWsp(WspRepository()).send_txt()
        return result, 200



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