# Tarea X: Nombre de la tarea :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

# El logo_2 debe de estar en la carpeta clientes. 
# La carpeta simple debe de estar en la carpeta servidor.
# Si un jugador esta en su turno y apreta una carta y no ocurre nada, la carta no es válida.
# Hay 0.5 segundos entre la reparticion de cada carta, esto para que no se topen los mensajes enviados ya que en un principio son muchos y superan la velocidad del servidor.(Tambien crea un efecto de reparticion de cartas :) )
# Debido a aquel tiempo de espera, si un jugador esta en su turno debe esperar un tiempo entre cada accion que hace para esperar la respuesta del servidor. Por ejemplo, apretar el boton robar carta, esperar 2 segundos y volver a apretarlo.
# Si hay 2 cartas identicas en la mano de un jugador y se desea jugar una de ellas se jugara la que este primero en el orden, esto solo es algo estetico, no afecta la funcionalidad del juego.
# Cuando se acumulan cartas +2 en el pozo y un jugador debe llevarselas solo tiene que apretar el boton robar una vez y se lleva todas las acumuladas.
# Luego de que un jugador se lleva el pozo acumulado debido a las cartas +2, el jugador con el turno siguiente puede jugar cualquier carta que sea del mismo color del ultimo +2 jugado.


### Cosas implementadas y no implementadas :white_check_mark: :x:

* <Protocolo>: Hecha completa
* <Correcto uso de sockets>: Hecha completa
* <Conexión>: Hecha completa
* <Manejo de clientes>: falto desconectar multiples clientes de forma esperada e inesperada de forma correcta.
* <Roles>: Hecha completa
* <Consistencia>: Hecha completa, no fue necesario usar locks.
* <Logs>: Hecha completa
* <Codificacion cartas>: Hecha completa
* <Decodificacion cartas>: Hecha completa
* <Integracion>: Hecha completa
* <Modelacion>: Hecha completa
* <General>: Hecha completa
* <Ventana de Inicio>: Hecha completa
* <Sala de Espera>: Hecha completa
* <Sala de Juego>: Falto que el servidor responda correctamente a gritar DCC4 e implementar el modo espectador.
* <Fin de la partida>: Sin hacer
* <Repartir cartas>: Hecha completa
* <Jugar carta>: Hecha completa
* <Robar Carta>: Hecha completa
* <Gritar DCC4>: Sin hacer
* <Termino del juego>: Sin hacer
* <Parametros JSON>: Hecha completa
* <Generador de mazos>: Hecha completa
* <Bonus>: Sin Hacer


## Ejecución :computer:
El módulo principal de la tarea a ejecutar son   ```servidor/main.py``` y ```cliente/main.py``` . Primero se debe ejecutar el servidor. 
## Librerías :books:
### Librerías externas utilizadas
*import threading
*import json
*import random
*import string
*import base64
*import sys
*from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QPushButton
*from PyQt5.QtCore import Qt, pyqtSignal, QObject
*from PyQt5.QtGui import QPixmap, QCursor, QTransform
*from PyQt5.QtWidgets import QApplication
*import time
1. ```librería_1```: ```función() / módulo```
2. ```librería_2```: ```función() / módulo``` (debe instalarse)
3. ...

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```librería_1```: Contiene a ```ClaseA```, ```ClaseB```, (ser general, tampoco es necesario especificar cada una)...
2. ```librería_2```: Hecha para <insertar descripción **breve** de lo que hace o qué contiene>
3. ...

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

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
1. \<Ayudantía 10>: este hace \<conexion servido-cliente> y está implementado en el archivo <servidor/main.py> y <cliente/cliente.py>  en las líneas <37 -71> y <9-60> respectivamente.



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
