# Tarea 2: DCCafé :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:
La tarea hace todo lo pedido en el enunciado. Hay que tener en consideracion que la combinacion de teclas F I N solo puede ser usada cuando haya llegado por lo menos un cliente al juego. Tambien hay que considerar que las sprites del chef entregadas tienen un margen transparente muy ancho por lo que el mesero choca con ellas  y no directo con el meson para entregarles las ordenes.


### Cosas implementadas y no implementadas :white_check_mark: :x:
1.- VENTANA INICIO
* Se visualiza correctamente: Hecho completo (ventana_inicio.py, 20)
* Crear o cargar partida: Hecho completo ( ventana_inicio.py, 41, 45)
* Se cargan correctamente los datos de una partida guardada:  Hecho completo ( back_end.py, 59)
* Se reinician correctamente los datos de una partida: Hecho completo ( back_end.py, 166)

2.- VENTANA JUEGO
* Se visualizan correctamente las tres áreas del juego: Hecho completo (ventana_principal.py, 94)
* Se visualizan correctamente las estadísticas del juego: Hecho completo (ventana_principal.py, 100)
* Se carga el mapa correctamente respetando las dimensiones:  Hecho completo (ventana_principal.py, 121)
* Información de la ronda, clientes y dinero se actualizan a lo largo del juego: Hecho completo (ventana_principal.py, 283) (back_end.py, 350)
* Se pueden comprar objetos de forma correcta: Hecho completo (ventana_principal.py, 16, 43, 165, 177) (back_end.py, 110, 155)
* Se muestran todos los elementos que se pueden comprar en la tienda junto a sus precios: Hecho completo (ventana_principal.py, 127) 
* Las mesas y el chef se pueden eliminar haciendo click. Se impide que el jugador se quede sin elementos en el mapa: Hecho completo (ventana_principal.py, 253) (back_end.py, 312)
* Los clientes aparecen sentados en las mesas: Hecho completo (ventana_principal.py, 264)(back_end.py, 268, 273)
* La ronda termina cuando ya no quedan clientes: Hecho completo (ventana_principal.py, 304)(back_end.py, 281)(entidades.py, 267)
* Se visualiza una ventana con los resultados y botones: Hecho completo (ventana_post_ronda.py, 39)
* Se puede continuar, guardar y salir: (ventana_post_ronda.py, 88, 90, 93)
* Las estadisticas post-ronda son correctas y reflejan el resultado de la ronda: Hecho completo (ventana_post_ronda.py, 27)(back_end.py, 351)
* Si la reputación llega a 0, el juego se termina: Hecho completo (ventana_post_ronda.py, 35)
3.- ENTIDADES
a) Jugador
* El movimiento del jugador es fluido, continuo y animado: Hecho completo (back_end.py, 208) (ventana_principal.py, 257)(entidades2.py, 142 )
* Movimiento respeta colisiones no especiales: Hecho completo (back_end.py, 96)
* Movimiento respeta colisión especial con chef y clientes: Hecho completo (back_end.py, 96, 258)
* El jugador cambia de sprite al cambiar de estado: Hecho completo(entidades2.py, 32)
b) Chef 
* El chef cambia de estado cuando corresponde:Hecho completo (entidades2.py, 226)
* Sube de nivel según la cantidad de bocadillos que haya preparado: Hecho completo (entidades2.py, 232)
* Implementa la probabilidad de equivocarse correctamente: Hecho completo (entidades2.py, 206)
* El chef cambia de sprite según su estado: esperando, cocinando, terminado: Hecho completo (entidades2.py, 244)
c) Bocadillos
* El tiempo de preparación cambia según la fórmula establecida: Hecho completo (entidades2.py, 213)
* La calidad del bocadillo cambia según la fórmula establecida: Hecho completo (entidades.py, 24)
d) Clientes
* Los clientes cambian de estado cuando corresponde: Hecho completo (entidades.py, 160, 65)
* Los clientes desaparecen después de recibir su bocadillo o una vez que se acabe el tiempo de espera: Hecho completo (entidades.py, 160, 87)
* Los clientes cambian de sprite dependiendo de su estado de ánimo: Hecho completo (entidades.py, 160,65)
e) DCCafé
* Calcula correctamente los clientes por ronda:  Hecho completo (entidades.py, 246)
* Calcula correctamente la reputación:  Hecho completo (entidades.py, 242)
4.- TIEMPO 
* Los procesos internos del DCCafé respetan el reloj del juego:  Hecho completo (entidades.py, 130)
* Esta implementado el botón Pausa y la letra P:  Hecho completo (ventana_principal.py, 294, 237)
5.- FUNCIONALIDADES EXTRA
* MON :  Hecho completo (ventana_principal.py, 245) (back_end.py, 296)
* FIN :  Hecho completo (ventana_principal.py, 241) (back_end.py, 305)
* RTG :  Hecho completo (ventana_principal.py, 249) (back_end.py, 299)


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```mapa.csv``` en ```la misma carpeta en que se encuentre ejecutando p.py```
2. ```datos.csv``` en ```la misma carpeta en que se encuentre ejecutando p.py```



## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```sys```: ```función() / módulo```
2. ```Pyqt5.QtWidgets```: ```QLabel, QWidget, QLineEdit,QHBoxLayout, QVBoxLayout, QPushButton,from PyQt5.QtWidgets import QApplication```  (debe instalarse)
3. ``` PyQt5.QtCore```: ```Qt, pyqtSignal, QTimer, QMimeData, QObject``` (debe instalarse)
4. ```PyQt5.QtGui```: ```QPixmap, QDrag, QPainter, QCursor``` (debe instalarse)
5. ```time```: ```perf_counter, sleep```
6. ```threading```: ```Thread, Event, Timer```
7.- ```random```: ```randint```


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```p.py```: Contiene todos los parametros del programa
2. ```ventana_inicio.py```: Contiene la ventana para ingresas al juego
3. ```ventana_principal.py```: Contiene la ventana de pre ronda y la de juego 
4. ```ventana_post_ronda.py```: Contiene la ventana que aparece cuando se termina de jugar una ronda
5. ```entidades```: Contiene las entidades Bocadillo, Mesa, Cliente, DCCafe, RelojInterno
6. ```entidades2```:  Contiene las entidades Jugador y chef
7. ```back_end.py```: Contiene todo la parte funcional de las ventanas 
8. ```main.py```: Aqui se realiza todas las conexiones de señales entre ventanas
## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. El mesero puede pasar por atras de los clientes ya que estos estan sentados sobre las mesas

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://www.youtube.com/watch?v=9CJV-GGP22c>: en este me base para hacer \<drag and drop> y está implementado en el archivo <ventana_principal.py> en las líneas <16 -62> 



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
