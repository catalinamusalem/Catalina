# Tarea 1: DCCriaturas Fantásticas :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<El programa funciona bien, tiene todas las funcionalidades pedidas. 
Se puede cambiar de usuario en una misma partida. 
Los archivos se actualizan cada vez que se cambia de menu o cuando ocurre un cambio mayor como lo es pasar de dia, adoptar criatura o crear magizoologo.


### Cosas implementadas y no implementadas :white_check_mark: :x:

Programacion orientada a objetos:
1. Diagrama: completo
2. Definicion de clases, atributos y metodos:
a. Magizoologos: implementado
b. DCCriaturas: implementado
c. Alimentos: implementado
d. DCC: implementado
3. Relaciones entre clases:
a. Clases abstractas: implementado
b. Agregacion y composición: implementado

Partidas:
1. Crear partida:
a. Nombres válidos y únicos: implementado
b. Elegir magizoologo y criatura: implementado
c. Instanciar magizoologo: implementado
d. Error de ingreso: implementado
2. Cargar partida:
a. Cargar magizoologo existente: implementado
b. Poblar sistema: implementado
c. Error de ingreso: implementado
3. Guardar archivos: implementado 

Acciones:
1. Cuidar DCCriaturas:
a. Alimentar: implementado
b. Efectos alimentos: implementado
c. Ataque criaturas: implementado
d. Escape criaturas: implementado
e. Criaturas enfermas: implementado
f. Habilidad especial: implementado
g. Descuentos de energia: implementado
h. Notificacion de energia insuficiente: implementado

2. DCC:
a. Adoptar criatura: implementado
b. Comprar alimentos: implementado
c. Cobro de Sickles: implementado
d. Datos magizoologos y criaturas: implementado
3. Pasar al día siguiente:
a. Habilidades especiales de cada criatura: implementado
b. Actualizacion de puntos: implementado
c. Actualizacion estado de hambre: implementado
d. Actualizacion estado de salud: implementado
e. Actualizacion escape criaturas: Actualizacion estado de hambre: implementado
f. Pago de sickles: implementado
g. Multas: implementado

Consola:
1. Menu de inicio: implementado
2. Menu de acciones: implementado
3. Menu dccriaturas: implementado
4. Menu DCC: implementado
5. Pasar dia:  implementado
6. Robustez: implementado

Manejo de archivos:
1. Archivos csv:  implementado
2. Parametros:  implementado








## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se deben crear los siguientes archivos y directorios adicionales:
1. ```magizoologos.csv``` en ```Catalinamusalem-iic2233-2020-1/Tareas/T01/```
2. ```criaturas.csv``` en ```Catalinamusalem-iic2233-2020-1/Tareas/T01/```



## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```abc```: ```ABC, abstractmethod```
2. ```random```: ```randint, choice, random``` 


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. main.py: es el modulo principal donde se lleva a cabo todo el control de menus y manejo de archivos.
2. p.py: son los parametros que se usan en los otros modulos
3. crear.py: aqui estan las funciones que crean los objetos de las clases que se usan en el resto de los modulos.
4. Tarea1.py: aqui se encuentran las definiciones de todas las clases del programa.
5. Tarea1c.py: este modulo es la continuacion de Tarea1.py para no exceder la extension de lineas maxima.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:
1. Al momento de crear un magizoologo si el usuario no ingresa un tipo de magizoologo válido se asumira que es Híbrido.
2. Al momento de crear un magizoologo si el usuario no ingresa un tipo de criatura válida se asumira que adopta un Augurey.
3. Los magizoologos cuando son creados tienen nivel de aprobacion 60, ya que no han hecho nada para ser evaluados, al pasar el primer dia se les asigna su nivel correspondiente.
4. Cuando un magizoologo compra alimentos o criaturas si no ingresa una opcion válida al momento de elegir que tipo quiere se le entregara la primera opcion.







-------








## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
