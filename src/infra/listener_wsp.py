import json
import os
import random
import string
import time
from flask_restful import Resource
from flask_restful import request
import pysftp


from src.app.camara import VideoCamera
from src.app.send_message import SendWsp
from src.wsp.infra.wsp_repository import WspRepository
from src.html import html
from src.app.data_convert import DataConvert


class ListenerWsp(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        message = DataConvert().get_data(request.data)
        id = message.get("id", "")
        phone = message.get("phone", "56961720045")
        message = message.get("message", "Error de servidor").lower()
        result_id = self.check_id(id)
        if not result_id:
            return {"error": "no id"}, 200
    
        op = request.form.get("op", "")
        print(f"phone: {phone}, message: {message}, id: {id}")

        if "error" in message:
            return {"message": message}, 200

        if "001" in message:
            name = VideoCamera().get_image()
            print(name)
            if name:
                SendWsp(WspRepository()).send_txt(txt="Cargando imagen...", phone=phone)
                result = SendWsp(WspRepository()).send_image(name ,phone)
                print(json.dumps(result))
                return {'mensaje': result}, 200
            txt = "Error al conectar con camaras, desconectadas o no conectadas al wifi"
            SendWsp(WspRepository()).send_txt(txt=txt, phone=phone)
            return {"error": "no camera"}, 200
        elif "002" in message:
            # name = VideoCamera().get_video()
            #if name:
            # print(f"video enviando... {name}")
            SendWsp(WspRepository()).send_txt(txt="generando enlace de video en vivo... (desface en la trasmision dependera del internet..)", phone=phone)
            # time.sleep(1)

            html = self.up_link_video()
            SendWsp(WspRepository()).send_video(name=html, phone=phone)
            result = SendWsp(WspRepository()).send_txt(txt=f"haz click -> https://www.hogarcam.com/duran/video/{html}", phone=phone)
            print(json.dumps(result))
            return {'mensaje': result}, 200

        # result = SendWsp(WspRepository()).send_txt(txt="vuelve a mandar el mensaje con una de las opciones: imagen o video", phone=phone)
        # result1 = SendWsp(WspRepository()).send_template_principal(phone=phone)
        result = SendWsp(WspRepository()).send_menu_principal_button(phone=phone)
        print(json.dumps(result))
        # print(json.dumps(result1))
        return {'mensaje': 'enviado1'}, 200

    def up_link_video(self):
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        myHostname = "access952227001.webspace-data.io"
        myUsername = "u111288009"
        myPassword = "Cadu@1894"

        longitud_cadena = 6

        # Generar una cadena aleatoria de longitud_cadena caracteres alfanuméricos
        nombre_aleatorio = ''.join(random.choices(string.ascii_letters + string.digits, k=longitud_cadena))

        # Crear y escribir en el archivo HTML
        with open(f"{nombre_aleatorio}.html", "w") as archivo:
            archivo.write(html)

        with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, cnopts=cnopts) as sftp:
            print ("Connection succesfully stablished ... ")
            with sftp.cd("/duran/video"):
            # Subir el archivo local hola.txt al servidor.
                sftp.put(f"{nombre_aleatorio}.html")
                print ("link generado correctamente ... ")
                os.remove(f"{nombre_aleatorio}.html")

                return f"{nombre_aleatorio}.html"
            
    def check_id(self, id):
       with open('ids.json', 'r') as archivo:
        datos = json.load(archivo)
        if not id:
            return False
        if id in datos:
            print("existe el dato")
            return False
        else:
            datos[id] = {}
            with open('ids.json', 'w') as archivo:
                json.dump(datos, archivo)
            return True