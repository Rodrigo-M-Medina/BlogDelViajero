# README Blog del viajero
Creadores: Alori Guadalupe, Medina Rodrigo, Rosenman Fernando.

Back end realizado íntegramente en Python y Django, front end HTML, CSS y JS.

	Comenzamos con el proyecto y tras 3 reuniones nos dimos cuenta de que habíamos comenzado en forma desordenada por lo que volvimos a comenzar replanteando, reorganizando y escribiendo el paso a paso de lo que queríamos lograr. A continuación link del primer proyecto que abandonamos para comenzar de 0 en un proyecto más ordenado: 
https://github.com/Rodrigo-M-Medina/ProyectoGrupal.git

El blog se divide en 2 apps: AppUsuarios y AppMensajería. 
AppUsuarios: podemos encontrar: login, logout, registrarse, ingresar, desconectarse, subir, modificar y eliminar posteos, cada posteo cuenta con su respectivo CRUD.
Acciones sobre los posteos requieren que el usuario se haya logueado previamente, para lo cual se utiliza el decorador @login required en las vistas. 
De esta forma nos aseguramos de que solo los creadores del post o el administrador pueden eliminar o modificar el posteo.  
Cada usuario tiene la posibilidad de generar un avatar propio y en caso de no generarlo, el blog cuenta con un avatar por defecto. 
Solo los usuarios creadores de sus respectivas cuentas y administradores pueden eliminar/editar perfiles de usuario. 
Solo el admin/superuser puede realizar CRUD sobre todos los perfiles activos de la página. 
App mensajería: consta de un servicio de mensajería entre usuarios en el que los mismos pueden enviarse mensajes entre sí, con un booleano que confirma si el mensaje ha sido leído o no.
En about us se encuentra información de los 3 integrantes del grupo, así como un link de acceso al linkedin de cada uno.
Utilizamos Git Merge para unificar el trabajo que se realizó por fuera de las reuniones donde escribimos código en equipo. 
La mayoría del código fue escrito en reuniones de Discord, alternando quienes codeaban, mientras los otros 2 integrantes del grupo buscaban errores y trabajaban en alternativas a las opciones que no funcionaban, revisando nombres de variables y posibles inconsistencias que pudieran generar problemas en el funcionamiento del blog.

Credenciales del super usuario
usuario : admin
clave : admin
