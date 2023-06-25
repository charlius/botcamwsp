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
from src.html import get_html, add_div
from src.app.data_convert import DataConvert
from src.api import *


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

        # Alertar familia
        if "000" in message:
            connection = Connection()
            connection.connect()
            consulta = ConsultaFamilia(connection)
            resultado_integrantes = consulta.obtener_integrantes_por_telefono(phone)
            print(resultado_integrantes)
            name_integrante = ""
            for resultado in resultado_integrantes:
                if phone in resultado.get("telefono", "none"):
                    name_integrante = resultado.get("nombre_integrante", "none")
            for resultado in resultado_integrantes:
                phone_integrante = resultado.get("telefono")
                # if phone_integrante != phone:
                SendWsp(WspRepository()).send_txt(txt=f"*Se genero una alerta por {name_integrante}* esto es solo de prueba no pescar mensje", phone=phone_integrante)
                self.msg_cam_live(phone_integrante)
            return {"success": "ok"}, 200

        if "001" in message:
            SendWsp(WspRepository()).send_txt(txt=f"Cargando Fotos ⏳📷 ¡Por favor, espera un momento mientras se carga la imagen! ⌛️🔍", phone=phone)
            connection = Connection()
            connection.connect()
            consulta = ConsultaFamilia(connection)
            resultado_cameras = consulta.obtener_cameras_por_telefono(phone)
            connection.close
            for camaras in resultado_cameras:
                url = camaras.get("url", "none")
                name_camera = camaras.get("nombre_camara", "none")
                print(f"url: {url}, nombre: {name_camera}")
                name = VideoCamera(url).get_image(f"{name_camera}.png")
                print(name)
                if name:
                    SendWsp(WspRepository()).send_txt(txt=f"*camara {name_camera}*", phone=phone)
                    result = SendWsp(WspRepository()).send_image(name ,phone)
                    print(json.dumps(result))
                else:
                    txt = f"Error al conectar con camara {name_camera}, desconectadas del wifio red electrica"
                    SendWsp(WspRepository()).send_txt(txt=txt, phone=phone)
            return {"ok": "success"}, 200
        elif "002" in message:
           return self.msg_cam_live(phone)

        result = SendWsp(WspRepository()).send_menu_principal_button(phone=phone)
        print(json.dumps(result))
        return {'mensaje': 'enviado1'}, 200

    def msg_cam_live(self, phone):
        connection = Connection()
        connection.connect()
        consulta = ConsultaFamilia(connection)
        resultado_cameras = consulta.obtener_cameras_por_telefono(phone)
        connection.close
        # time.sleep(1)

        txt = """
            *Recuerda* que este enlace tiene una duración de *10 minutos* por motivos de seguridad. ⌛️ Además, ten en cuenta que puede haber un ligero desfase en la transmisión debido a la calidad de tu conexión a Internet o la señal. 🌐
        """
        SendWsp(WspRepository()).send_txt(txt=txt, phone=phone)
        html = self.up_link_video(resultado_cameras)
        SendWsp(WspRepository()).send_video(name=html, phone=phone)
        result = SendWsp(WspRepository()).send_txt(txt=f"⏯️ -> [https://www.hogarcam.com/duran/video/{html}]", phone=phone)
        print(json.dumps(result))
        return {'mensaje': result}, 200

        result = SendWsp(WspRepository()).send_menu_principal_button(phone=phone)
        print(json.dumps(result))
        return {'mensaje': 'enviado1'}, 200

    def up_link_video(self, resultado_cameras):
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        myHostname = "access952227001.webspace-data.io"
        myUsername = "u111288009"
        myPassword = "Cadu@1894"

        longitud_cadena = 6

        # Generar una cadena aleatoria de longitud_cadena caracteres alfanuméricos
        nombre_aleatorio = ''.join(random.choices(string.ascii_letters + string.digits, k=longitud_cadena))
        div = ""
        for camaras in resultado_cameras:
            url = camaras.get("url", "none")
            name_camera = camaras.get("nombre_camara", "none")
            url_video = camaras.get("url_video", "none")
            div = f"{div} {add_div(url_video, name_camera)}"
        html = get_html(div)
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