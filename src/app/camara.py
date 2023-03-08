from datetime import datetime, timedelta
import os
import time
import cv2
import paramiko
import pysftp


class VideoCamera(object):
    def __init__(self):
        self.cam1 = "rtsp://admin:Cadu+1894@201.215.145.33:99"
        self.video = cv2.VideoCapture(self.cam1)

    def __del__(self):
        self.video.release()
    
    # def get_image(self):

    #     leido, frame = self.video.read()

    #     if leido == True:
    #         cv2.imwrite("../imagen/foto_cam1.png", frame)
    #         print("Foto tomada correctamente")
    #         return "foto_cam1.png"
    #     else:
    #         print("Error al acceder a la cámara")
    #         return ""

    def get_image(self):

        leido, frame = self.video.read()

        if leido == True:
            cam = "cam1.png"
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            cv2.imwrite(f"{BASE_DIR}/imagen/{cam}", frame)
            print("Foto tomada correctamente")
            name = self.up_ftp_image(cam)
            #gtime.sleep(2)
            return name
        else:
            print("Error al acceder a la cámara")
            return ""

    def up_ftp_image(self, cam):

        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        myHostname = "access952227001.webspace-data.io"
        myUsername = "u111288009"
        myPassword = "Cadu@1894"

        with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, cnopts=cnopts) as sftp:
            print ("Connection succesfully stablished ... ")
            if "mp4" in cam:
                with sftp.cd("/video"):
                # Subir el archivo local hola.txt al servidor.
                    sftp.put("output.mp4")
                    print ("imagen subida correctamente ... ")
                    return "output.mp4"
            elif ".png" in cam:
                BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                with sftp.cd("/duran/imagen"):
                    # Subir el archivo local hola.txt al servidor.
                    sftp.put(f"{BASE_DIR}/imagen/{cam}")
                    print ("imagen subida correctamente ... ")
                    return cam

    def get_frame(self):
        face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        success, frame = self.video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        (flag, encodedImage) = cv2.imencode(".jpg", frame)

        # ret, jpeg = cv2.imencode('.jpg', image)
        return encodedImage.tobytes()

    def get_video(self):
        print("capturando cam...")
        cap = cv2.VideoCapture("rtsp://admin:Cadu+1894@201.215.145.33:99")
        print("selecionado codec")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        time.sleep(3)
        ahora = datetime.now()
        cam = "cam1.mp4"
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        out = cv2.VideoWriter(f'{BASE_DIR}/video/{cam}', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
        print("capturando frames...")
        while True:
            new = datetime.now()
            ret, frame = cap.read()

            try:
                if ret and cap.isOpened():
                    # cv2.imshow('frame', frame)
                    out.write(frame)

            except:
                print ('ERROR - Not writting to file')
                gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                #cv2.imshow('frame', gray)
                return ""
            diferencia = (new-ahora)
            if round(diferencia.total_seconds()) >= 40:
                print("sale del while")
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        del(cap)
        print("video tomado correctamente")
        name = self.up_ftp_image(cam)

        # os.remove(f'{BASE_DIR}/video/{cam}')
        return name
    
