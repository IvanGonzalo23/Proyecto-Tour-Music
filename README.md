
# Tour Musical Mil Programadores Salteños Python 2023. 

Proyecto Integrador Final para el curso mil programadores salteños python 2023.

El programa consiste en la navegacion de lugares para eventos musicales contando con un mapa para la orientacion de los lugares. Aparte de eso cuenta con una interfaz moderna para los apasionados de la musica que quieran sentirse comodos, a la vez de que es un navegador, es un programa que funciona para un almanaque de eventos que ya asistio el usuario, eventos que el usuario considerara como favoritos y podra comentar su experiencia con el evento y al mismo tiempo podra ver las reseñas de los demas usuarios.

Este proyecto cuenta con un login donde se ira guardando los usuarios que vayan ingresando, al igual que podran crear mas usuarios


## Installation

## Tkinter

```bash
  pip install tk
```

## Customtkinter
```bash
    pip install customtkinter
```
## TkinterMapView
```bash
    pip3 install tkintermapview
```
    
## Package

## Vistas

Este directorio o paquete tiene en su interior las interfaces graficas con la cual interactuara el usuario cuando inicie el programa

* **ventana_login.py**: Esta ventana es un Frame que conecta con el archivo main.py, la vista de esta ventana viene de la clase Frame donde representa el login en la cual el usuario querra logearse, tiene dos botones, el primero boton sirve para ingresar a la ventana principal y el segundo boton sirve para cambiar a la ventana para crear usuarios.

* **ventana_crear.py**: Dentro de este archivo contiene el Frame en donde ira la interfaz para crear un usuario, la vista de este Frame viene de la clase Createuser, esta ventana cuenta con un modelo de clase donde manejara la informacion que se ingresara para la creacion del usuario, ademas de que se tiene una serie de condiciones que se debe cumplir para crear el usuario, como por ejemplo, poner mas de 8 caracteres en la contraseña, llenar todos los campos y poner un dominio valido en el correo. Para poder entrar a esta ventana se debe clickear el boton sign up de la ventana_login.py

* **ventana_principal.py**: El archivo ventana_principal.py es un Frame que contiene las botoneras y vistas principales que lleva el programa, cuenta con un listbox que mostrara los eventos ya asistidos por el usuario, y tres botones donde llevan a los diferentes frames del programa. El primer boton lleva al archivo ventana_eventos_disponibles.py, donde se muestra los eventos que no iniciaron todavia. El segundo boton sirve como buscador, en donde nos llevara a ventana_buscador.py para poder buscar el evento que quiere el usuario. El tercer boton es una version del archivo ventana_eventos_disponibles.py la diferencia que ventana_evento_historial muestra de manera general todos los eventos, tantos pasados como futuros. Por ultimo esta el boton para volver al anterior Frame.

* **ventana_eventos_disponibles.py**: Este archivo sirve para mostrar los eventos que estan disponibles sacandolos desde un json, la vista muestra un listbox con los eventos disponibles, estos estan remarcados con un color amarillo que resalta los nombres, esto esta en un frame ubicado de manera lateral, a lado de este frame esta el mapa hecho por tkintermapview, si el usuario le hace clic una vez al evento muestra donde esta ubicado en el mapa, si le hace doble clic mostrara una ventana con Toplevel para mostrar todos los detalles. Tambien cuenta con un boton para volver al anterior frame

* **ventana_buscador.py**: Este modulo cuenta con una ventana que sirve para buscador de eventos, contiene un modelo de clase para poder cargar los eventos y compararlos con los eventos ingresados. Cuenta con el boton de regreso para volver a la ventana anterior

* **ventana_historial.py**: Este archivo muestra todos los eventos existentes, con su mapa, clickeo doble para mas informacion y su boton para volver.

* **ventana_secundaria.py**: Este modulo contiene la segunda ventana que se usara para el programa, teniendo como vista un listbox para mostrar las reseñas que hicieron otros usuarios en donde si se le da un doble clic a cualquier reseña abrira una ventana para mostrar toda la informacion, y las tres botoneras principales que nos haran cambiar de frames. El primer boton nos lleva a la ventana de reseñas, donde en esta podremos elegir el evento y escribir sobre ella. El segundo boton nos llevaran al area de eventos favoritos que eligio el usuario. EL tercer boton nos traslada a la interfaz que servira para que el usuario elija su evento favorito.

* **ventana_reseña.py**: Esta interfaz nos permitira ver la vista para crear una reseña, cuenta con un combobox para elegir el evento, y un text para escribir la experiencia que tuvo el usuario con dicha eleccion, estos tienen un boton para guardar la reseña en un json y un boton para volver al frame anterior.

* **ventana_favoritos.py**: Esta ventana solo muestra mediante un listbox el evento favorito del usuario, cuenta con un boton para volver a la ventana anterior

* **ventana_agregar_favoritos.py**: Este archivo nos presesnta la vista para agregar los eventos favoritos para el usuario, tiene un listbox en donde si lo seleccionamos y hacemos clic en su boton para agregar se cambiara al color amarillo y a la vez se creara un json con el nombre del usuario y el evento seleccionado, cuando finalice el proceso tiene la opcion de seleccionar otro evento o salir de la ventana por el boton para volver.

* **__ init__.py**: Este archivo solo sirve para que python reconozca el directorio como un paquete y hacer la modulacion correctamente 

## Modelo

En esta carpeta contiene los archivos que manejan la informacion de los eventos y usuarios creados

* **clase_usuarios.py**: Cuenta con una estructura para craer usuarios y guardalos en un json, esta clase debe recibir de parametros la informacion que se vaya ingresar para asi poder crear el json con los diferentes usuarios.

* **clase_eventos_disponibles.py**: Este modelo sirve para cargar los eventos disponibles de un json ya existente para asi mostrarlos en la ventana que corresponda

* **clase_historial.py**: Este modelo carga el total de los eventos de un json existente para despues mostrarlo en la ventana que corresponde

* **__ init__.py**: Este archivo solo sirve para que python reconozca el directorio como un paquete y hacer la modulacion correctamente 

## Img

Este directorio solo contiene las imagenes que se usara en el programa

## Data

Contiene los datos que se iran creando y cargando mediante el uso de archivos json.

* **Usuarios.json**: Este json contiene los usuarios que se iran creando

* **eventos_disponibles.json**: Este archivo json preexistente tiene guardado los eventos disponibles 

* **historial_eventos.json**: Este json tiene el historial de eventos que hay en este formato 

* **reseñas.json**: Este archivo creado guarda las reseñas de los usuarios que iran creando

* **favoritos.json**: Guarda los eventos que escoge como favoritos el usuario

## Main.py

Este es el archivo padre del programa donde tiene como clase TourMusical, esta sirve para crear la ventana donde contendra todos los frames de las diferentes ventanas que se fueron mostrando, al igual que tiene las funciones para abrir las ventanas y crear la carpeta data si no existe


## Documentation

[Customtkinter Github](https://github.com/TomSchimansky/CustomTkinter)

[Pagina oficial de Customtkinter](https://customtkinter.tomschimansky.com/)

[Tkintermapview Github](https://github.com/TomSchimansky/TkinterMapView)

[Tkinter](https://docs.python.org/es/3/library/tkinter.html)

