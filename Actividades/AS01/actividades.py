class Actividad():
    # Acá debes crear el constructor de la clase Actividad
    def __init__(self, nombre,felicidad,estres):
        self.nombre=nombre
        self.felicidad=felicidad
        self.estres=estres


class Hobby(Actividad):
    # Acá debes crear el constructor de la clase hobby.
    def __init__(self,nombre,felicidad,estres):
    	super().__init__(nombre,felicidad,estres)
    def __str__(self):
     	return "Hobby - "+ self.nombre + " - felicidad: " + str(self.felicidad) + " - Estres: " + str(self.estres) 


class Deber(Actividad):
    # Acá debes crear el constructor de la clase Deber.
    def __init__(self,nombre,felicidad,estres):
    	super().__init__(nombre,felicidad,estres)
    def __str__(self):
     	return "Deber - "+ self.nombre + " - felicidad: " + str(self.felicidad) + " - Estres: " + str(self.estres) 
