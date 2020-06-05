# Tarea 2: DCCafé :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

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
* Los clientes aparecen sentados en las mesas: 





* <Nombre item pauta<sub>1</sub>>: Hecha completa
* <Nombre item pauta<sub>2</sub>>: Me faltó hacer <insertar qué cosa faltó>
    * <Nombre subitem pauta<sub>2.1</sub>>: Hecha completa 
    * <Nombre subitem pauta<sub>2.2</sub>>: Me faltó hacer <insertar qué cosa faltó>
    * ...
* <Nombre item pauta<sub>3</sub>>: Me faltó hacer <insertar qué cosa faltó>
* ...
* <Nombre item pauta<sub>n</sub>>: Me faltó hacer <insertar qué cosa faltó>
* <Nombre item pauta<sub>1</sub>>: Hecha completa
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```archivo.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```archivo.ext``` en ```ubicación```
2. ```directorio``` en ```ubicación```
3. ...


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

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
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
