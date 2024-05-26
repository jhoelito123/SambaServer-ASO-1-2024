# SambaServer-ASO-1-2024

App grafica para configurar servicio de transferencia de archivos Samba
Dirigido al sistema operativo OpenSUSE -Linux

Instrucciones de Uso:

- Clone la carpeta en un directorio que tenga los permisos de utilizar la interfaz gráfica
  en otras palabras, que la variable display esté configurada correctamente, de lo contrario el programa no se podrá iniciar (le recomendamos la carpeta /tmp)
- Su archivo de configuracion debe existir en la ruta "/etc/samba/smb.conf", si no se encuentra el
  archivo ahi adentro, no se podrá configurar el servicio
- Recuerde tener instalado los paquetes necesarios de python en su sistema operativo, incluyendo
  relacionadas a Tkinter, si no lo tiene puede ejecutar estos comandos:
  #sudo zypper install python3-tk
  #sudo zypper install python3-pillow
  #sudo pip install paramiko
- Para iniciar el programa debe dirigirse al directorio del proyecto y ejecutar el comando:
  #python3 App.py

En caso de no contar con python u otra dependencia necesaria el programa no se inicializará

Recomendaciones:

- Pueden aparecer algunos avisos en la consola que no afectan en el funcionamiento de la aplicación como:
  """"/usr/lib/python3.6/site-packages/paramiko/transport.py:32: CryptographyDeprecationWarning: Python 3.6 is no longer supported by the Python core team. Therefore, support for it is deprecated in cryptography. The next release of cryptography will remove support for Python 3.6.
  from cryptography.hazmat.backends import default_backend""""
