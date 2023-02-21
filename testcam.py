from datetime import datetime, timedelta
import time
import cv2
def main():
    print("capturando cam...")
    cap = cv2.VideoCapture("rtsp://admin:Cadu+1894@201.215.145.33:554/onvif1")
    print("seleccionando codec...")
    fourcc = cv2.VideoWriter_fourcc(*'MPEG-4')
    time.sleep(3)
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
    ahora = datetime.now()
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
        diferencia = (new-ahora)
        print(round(diferencia.total_seconds()))
        if round(diferencia.total_seconds()) >= 30:
            break

    cap.release()
    out.release()
    # cv2.destroyAllWindows()
    del(cap)

def get_image():

    cap = cv2.VideoCapture('rtsp://admin:Cadu+1894@201.215.145.33:554/stream1')

    leido, frame = cap.read()

    if leido == True:
        cv2.imwrite("../foto.png", frame)
        print("Foto tomada correctamente")
        up_ftp_image()
        time.sleep(2)
        send_image()
    else:
        print("Error al acceder a la cámara")

token = "EAAZA0LuBg7yMBAOXnXQPrNEmC8SMP13qQoPx9d1ZAV3PbZCfGZBzKvxhgLoXSHzVt9XTVltoKKA9RWnsN6BID4DvMP3bQGHE2JcbuZA9rKps5EmgtrGek6ZAEhGtxo3762iOhgGVSrWBk9h0mJPlAxJTE5Hgvz2BAymbhtpKyFxF4zScC6wvxoenddujC3KHsec3pE0niV8AZDZD"


def send_image(token):
    import requests
    import json

    url = "https://graph.facebook.com/v15.0/104981199191453/messages"

    payload = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": "56961720045",
        "type": "text",
        "text": {
            "preview_url": False,
            "body": "text-message-content"
        }
        })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

def up_ftp_image():
    # import ftplib
    # ftp = ftplib.FTP("access952227001.webspace-data.io")
    # result = ftp.login("u111288009", "Cadu@1894")
    # print(result)
    # localfile='foto.png'
    # remotefile='/imagen/foto.png'
    # with open(localfile, "rb") as file:
    #     ftp.storbinary('STOR %s' % remotefile, file)
    import pysftp
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    myHostname = "access952227001.webspace-data.io"
    myUsername = "u111288009"
    myPassword = "Cadu@1894"

    with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, cnopts=cnopts) as sftp:
        print ("Connection succesfully stablished ... ")
        with sftp.cd("/imagen"):
            # Subir el archivo local hola.txt al servidor.
            sftp.put("foto.png")
            print ("imagen subida correctamente ... ")

if __name__ == '__main__':
    import sys
    sys.exit(main())
    # sys.exit(send_image(token))


from datetime import datetime, timedelta

captura = cv2.VideoCapture("rtsp://admin:Cadu+1894@201.215.145.33:554")
#salida = cv2.VideoWriter('videoSalida1.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
ahora = datetime.now()
video = cv2.VideoWriter('db0.mp4',cv2.VideoWriter_fourcc(*'mp4v'),2,(640,480))
while (captura.isOpened()):

    ret, imagen = captura.read()

    if ret == True:
        frame=cv2.resize(imagen, (960, 540))
        cv2.imshow('Capturing',imagen)
        # cv2.imshow('video', imagen)
        video.write(frame)
        new = datetime.now()
        diferencia = (new-ahora)
        print(round(diferencia.total_seconds()))
        if round(diferencia.total_seconds()) == 10:
            break
    else: break
captura.release()
video.release()
cv2.destroyAllWindows()