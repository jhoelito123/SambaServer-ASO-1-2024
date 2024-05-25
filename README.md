# SambaServer-ASO-1-2024
App grafica para configurar servicio de transferencia de archivos Samba

Banda recuerden tener ambos archivos, no se como hice la dependencia xddd pero Ustedes usen y ya, me avisan en caso de que tengan algun error o similar

Interface:
    - La ventana de navegacion para las 3 zonas de Inicio, Recursos e Identidad
forResource:
    - Hace enfasis a las ventanas que habran como opcion una vez demos la opcion de Edit dentro de un recurso
      compartido, con sus datos determinados y en caso de editar los existentes (solo lo necesario)
    - Ventana Check para los permisos del Create Mask de un recurso compartido
    - Extra ventana en caso de agregar un nuevo recurso compartido desde la firstInterface

For repair:
- La ventana de windows no detecta el caso "read only"
- Nos permite editar los nombres de recurso, nos deberia directo poner de titulo (modificar name resource)
- En la ventana de fisrtInterface nos permite modificar [Global] cuando no deberia aparecer en el listado