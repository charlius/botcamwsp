import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
myHostname = "access952227001.webspace-data.io"
myUsername = "u111288009"
myPassword = "Cadu@1894"

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, cnopts=cnopts) as sftp:
    with sftp.cd('/duran/video'): # cambiar al directorio que contiene los archivos a eliminar
        archivos = sftp.listdir() # obtener lista de archivos en el directorio

        # eliminar cada archivo en la lista
        for archivo in archivos:
            sftp.remove(archivo)

# cerrar conexion SFTP
sftp.close()