Instrucciones
1.- En una terminal ya estando en la carpeta del archivo “Dockerfile” ejecuta el siguiente comando :

    docker build --tag myapp .


2.- Ejecuta el siguiente comando en la terminal para ejecutar el contenedor de manera “Detach” y con los puertos mapeados (Se puede modificar el puerto de la derecha a cualquier puerto disponible, ej. 5000: 3000 ):

    docker run -d -p 5000:5000 myapp


3.- Ingrese en un buscador web al siguiente link (el numero debe de ser el puerto que se eligió ):

    http://localhost:5000/

4.- Ingrese su nombre de usuario y contraseña para acceder (el nombre de usuario debe de comenzar con mayúscula y la contraseña debe de contener únicamente letras y números, de lo contrario no se dará acceso).

5.- En cuanto se quiera detener el contenedor ingrese los siguientes comandos:

    docker ps

6.- Copie el "CONTAINER ID" del contenedor que quiera detener.

7.- Ingrese el siguiente comando sustituyendo <ID> por el "CONTAINER ID" (ej. docker stop f13737dff6a8 ):

    docker stop <ID>
