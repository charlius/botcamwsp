import os
import time
import datetime
import threading

# Diccionario que almacenará los IDs de los procesos asociados a cada usuario
procesos_por_usuario = {}
# Cargar la estructura de datos desde el archivo JSON
with open('procesos.json', 'r') as archivo:
    procesos_por_usuario = json.load(archivo)

def guardar_imagen():
    # Código para guardar la imagen en la carpeta correspondiente
    ...

def procesar_imagen(camara, guardar):
    # Cargar modelo y preparar la cámara
    ...

    while True:
        # Leer el frame actual de la cámara
        ret, frame = cam.read()

        # Realizar la detección de personas en el frame
        ...

        # Si la opción de guardar imágenes está activada
        if guardar:
            # Obtener la fecha y hora actual
            now = datetime.datetime.now()
            date_folder = now.strftime("%Y-%m-%d")
            time_folder = now.strftime("%H-%M")

            # Si el usuario ya tiene un proceso asociado, comprobar si todavía está vivo
            if current_user in procesos_por_usuario:
                process_id = procesos_por_usuario[current_user]
                if not os.path.exists(f"/proc/{process_id}"):
                    # El proceso ya no está vivo, eliminarlo del diccionario
                    del procesos_por_usuario[current_user]

            # Si el usuario no tiene un proceso asociado, crear uno
            if current_user not in procesos_por_usuario:
                # Crear un nuevo proceso para guardar imágenes
                p = threading.Thread(target=guardar_imagen)
                p.start()

                # Guardar el ID del proceso en el diccionario
                procesos_por_usuario[current_user] = p.ident
                # Guardar la estructura de datos en un archivo JSON
                with open('procesos.json', 'w') as archivo:
                    json.dump(procesos_por_usuario, archivo)

        # Mostrar el frame con la detección de personas
        ...

        # Esperar un segundo antes de procesar el siguiente frame
        time.sleep(1)

# Obtener el usuario actual y la opción de guardar imágenes desde algún lugar
current_user = "usuario1"
guardar_imagenes = True

# Crear la cámara y procesar los frames en un bucle
camara = cv2.VideoCapture(0)
procesar_imagen(camara, guardar_imagenes)