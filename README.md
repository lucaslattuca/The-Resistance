# The-Resistance
The Resistance


Metodología de la investigación


Prof. Ing. Carlos R. Rodríguez
Autores: Lattuca Lucas
	    García Pablo
Índice

		
Introducción:	1
Resumen:	1
Objetivos generales:	2
Objetivos específicos:	2
Marco teórico:	2
Método y desarrollo:	3
Commit número 1:	3
Commit número 3:	4
Commit número 4:	4
Commit número 5:	4
Commit número 8:	5
Commit número 9:	6
Planificación:	6
Resultados y conclusiones:	6
Guía de instalación Python:	7
Windows	7
Linux	7
Bibliografía:	8

Introducción:

Para lograr que el juego pudiera ser utilizado tanto en sistemas de Windows como de Linux se decidió utilizar Python que es un lenguaje de programación interpretado. El sistema operativo de Windows fue enriquecido con este lenguaje ya que no viene pre-instalado, para esto se debió instalar un soporte del lenguaje, en este caso se utilizó la última versión del anteriormente nombrado. Diferente es el caso de Linux el cual ya lo trae pre-instalado, aunque se deben instalar algunas librerías en el IDE para poder orientarlo hacia juegos y correrlo, en este caso se instaló PIP y PyGame. Se recomienda actualizar Python a su última versión, el cual puede ser obtenido desde repositorio y actualización de paquetes.

Debido a que no se ha enseñado el lenguaje en nuestras asignaturas se buscó tutoriales y demás información pertinente para poder lograr el objetivo, además se utilizó un IDE de programación específico, en este caso es el PyCharm de JetBrians la cual es una compañía de desarrollo de software la cual nos brinda esta plataforma de forma gratuita. 

La idea principal del juego fue homenajear y revivir el antiguo juego Space Invader el cual en sus comienzos era un arcade lanzado en 1978 el cual resultó sumamente exitoso, para darle otra temática se decidió también utilizar la saga de Star Wars la cual cabe perfectamente en nuestra idea de juego. El nombre del proyecto presentado fue tomado de la saga anteriormente nombrada perteneciente a uno de los bandos como es La Resistencia, en este caso el juego lleva el nombre original.

Resumen:

La idea principal del juego fue recrear un juego antiguo llamado Space Invader, juego antiguo de plataforma Arcade (máquina). Se decidió utilizar el lenguaje de programación Python por la facilidad para agregar assets y gráficos, para el mismo se debió utilizar librerías gráficas propias del lenguaje.



Objetivos generales:

El objetivo del juego es destruir asteroides y demás partículas sueltas que puedan aparecer en pantalla, esto mismo será destruido con disparos y misiles los cuales serán lanzados desde una nave espacial la cual se moverá hacia izquierda y derecha. Al destruir estos asteroides saldrán aleatoriamente buffos de escudos y mejoras de armas las cuales aumentarán la cantidad de disparos. La nave al ser golpeada por un asteroide irá perdiendo dichos escudos, armas y vidas, al terminar las tres vidas el juego finaliza y muestra el puntaje obtenido. 

Objetivos específicos:

    • Juego con niveles infinitos.
    • Nivel de dificultad creciente mediante avance.
    • Implementación de un sistema de puntuación.
    • Agregación de bonus escudos y armas.
    • Implementación de un sistema de vidas.

Marco teórico:

Los conocimientos acerca del lenguaje de Python eran prácticamente nulos, se decidió comenzar a investigar sobre el mismo, se debió aprender cómo era y que se podía hacer con el mismo, su sintaxis y forma de escritura. Fue dificultoso poder aprender un nuevo lenguaje en tan poco tiempo lo que nos llevó a tener muchos errores y falencias. 
Se pudo consultar con personas que tenían un conocimiento mínimo del lenguaje que, aunque era bastante precario nos ayudó bastante en este nuevo emprendimiento, además pudimos contar con la ayuda de guías y tutoriales que se encuentran fácilmente en la internet. 


Método y desarrollo:

El juego se fue desarrollando a medida que podíamos hacer y aprender sobre el lenguaje, además de subir actualizaciones a GITHUB (https://github.com/pablongar/The-Resistance - https://github.com/lukalpda/The-Resistance ) el cual nunca antes habíamos utilizado, esto también presento algunos inconvenientes ya que desde el IDE se puede subir información directamente a esta plataforma lo cual de alguna forma nos ayudó, pero a su vez fue engorroso aprender a hacerlo.
El juego se completó con lo que fue ideado desde el principio, se buscó conseguir assets de forma gratuita ya que invertir en los que son de carácter pago era muy difícil para nosotros. De esta forma pudimos desarrollar el juego sin inconvenientes en cuanto a imágenes. 

El juego no llegó a completarse hasta las últimas versiones en la cual se alcanzó a finiquitar lo propuesto para el desarrollo. Al ser nuevos en el campo de desarrollo de videojuego nos topamos con muchas cosas nuevas con las cuales fuimos experimentando para llegar al resultado esperado. En las siguientes imágenes se puede observar el desarrollo y evolución del mismo a lo largo de las versiones (solo incluyendo saltos significativos)

Commit número 1: 
En esta fase se comenzó a desarrollar el código, en el cual tuvimos problemas al poder mostrar una interfaz ya que el “main” no era tomado desde las carpetas.
Commit número 3:
En esta fase luego se pudo mostrar el “main” con su imagen y distintos atributos, en este agregamos un texto.
Commit número 4: 
Se logra correr el juego, pero con problemas de assets, los cuales fueron reemplazados y cambiados a formato .png los cuales permiten tener una imagen sin fondo.

Commit número 5:

En esta versión casi dando por finalizado el juego se puede correr nuevamente, pero con errores en el inicio del juego, se logró resolver el problema y el juego muestra el menú de inicio como corresponde. 


Commit número 8:
Una vez finalizado el problema de inicio y assets que mostraban la nave, se pudo ingresar al juego y probarlo.

Commit número 9:
Después de poder correr el juego se agregó el puntaje final obtenido, con esto finaliza el juego.



Planificación:

Para poder aportar ideas sobre el juego, formas de realización, lenguaje a utilizar, distribución de tareas y discusión sobre errores decidimos reunirnos de dos a tres veces por semana durante los últimos meses, luego de terminar el cursado se realizaron las reuniones, tanto en el espacio de la facultad y en otros lugares donde tuviéramos los elementos básicos para poder llevar a cabo dicha reunión, las mismas fueron de una hora a dos horas dependiendo de lo realizado. 

Cabe destacar que uno de los integrantes dejó el grupo por razones personales, de ser tres personas quedaron solamente dos, situación que nos trajo muchos problemas tanto a la hora de trabajar como a la hora de poder comunicarnos.

Fechas de reuniones:
28/03 - Comenzamos a planificar el juego, que lenguaje e IDE íbamos a trabajar.

11/04 - Decidimos basar nuestro juego en el antiguo juego Space Invader y ambientar en el lejano oeste.

25/04 - Debido a problemas con Sprites, assets y sonidos respecto al tema elegido, decidimos cambiarlo a la saga de Star Wars.

09/05 - Comienza el desarrollo tanto de código como de diseño recreando nuestros propios assets y sprites. 

21/05 - Se terminan de modificar sprites y assets del juego, ademas se determina que sonidos se van a usar, que formato y como cargarlos al juego.

23/05 - Se comienza con la corrección de errores de código y bugs en interfaz gráfica, además se implementan los archivos de sonido correspondientes. 

25/05 - En esta fase se añade código, el cual podría mostrar la puntuación al finalizar el ciclo del juego y mejorar la jugabilidad. Terminando así con la fase de desarrollo.

06/06 - Se comenzó con la recopilación de la información usada para poder así terminar el informe.

12/06 - Se procede con darle formato a la información y subirlo a GITHUB.


Resultados y conclusiones:

El juego pudo ser concluido y cumplió con las expectativas planteadas que se formularon cuando ideamos el juego, los resultados fueron los esperados y se da margen para poder agregar nuevos elementos que pueden hacer al juego más dinámico y completo, con lo dicho anteriormente se sigue teniendo en mente actualizarlo en un futuro. 


Guía de instalación Python:
Windows
Puedes descargar Python para Windows desde el sitio web https://www.python.org/downloads/release/python-343/. Después de descargar el archivo *.msi, debes ejecutarlo (haz doble clic en el archivo) y sigue las instrucciones. Es importante recordar la ruta (el directorio) donde se ha instalado Python.


Linux
Es muy posible que ya tengas Python instalado. Para verificar que ya lo tienes instalado (y qué versión es), abre una consola y tipea el siguiente comando:
$ python3 --version
Python 3.4.2
Si no tienes Python instalado o si quieres una versión diferente, puedes instalarlo como sigue:

Ubuntu
Tipea este comando en tu consola:
sudo apt install python3.4

Fedora
Usa este comando en tu consola:
sudo dnf install python3.4

openSUSE
Usa este comando en tu consola:
sudo zypper install python3






Bibliografía: 
https://es.wikipedia.org/wiki/Space_Invaders
https://es.wikipedia.org/wiki/Python
https://codigofacilito.com/cursos/Python
http://www.python.org.ar/wiki/AprendiendoPython
http://docs.python.org.ar/tutorial/3/index.html
http://docs.python.org.ar/tutorial/pdfs/TutorialPython2.pdf
https://tutorial.djangogirls.org/es/python_installation/
https://www.python.org/downloads/release/python-343/
https://github.com/pablongar/The-Resistance 
https://github.com/lukalpda/The-Resistance 

