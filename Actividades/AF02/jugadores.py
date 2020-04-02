from abc import ABC, abstractmethod
import random


class Jugador(ABC):

	def __init__(self, nombre, equipo, especialidad, energia,**kwargs):
		self.nombre=nombre
		self.equipo=equipo
		self.especialidad=especialidad
		self.energia=int(energia)
		self.inteligencia=3
		self.audacia=3
		self.trampa=3
		self.nerviosismo=3

# Completar


	def __str__(self):
		if self.equipo == 'ayudante':
			return f'Ayudante {self.nombre} ({self.especialidad})'
		return f'Alumno(a) {self.nombre} ({self.especialidad})'

	def __repr__(self):
		return (f'({type(self).__name__}) {self.nombre}: '
				f'equipo={self.equipo}|'
				f'energia={self.energia}|'
				f'inteligencia={self.inteligencia}|'
				f'audacia={self.audacia}|'
				f'trampa={self.trampa}|'
				f'nerviosismo={self.nerviosismo}')

	@abstractmethod
	def enfrentar(self, tipo_de_juego, enemigo):

	# Completar
		pass


# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorMesa(Jugador):

	def __init__(self, nombre, equipo, especialidad, energia,**kwargs):
		super().__init__(nombre, equipo, especialidad, energia,**kwargs)
		self.nerviosismo=min(self.energia, random.randint(0, 3))


	# Completar 
	# ¡Aprovecha herencia!


	def jugar_mesa(self, enemigo):
		if enemigo.nerviosismo>self.nerviosismo:
			print("ganó "+ self.nombre)
			return True
		else:
			print("ganó "+ enemigo.nombre)
			return False
	def enfrentar(self, tipo_de_juego,enemigo):
		print(self.equipo + " " +self.nombre+ " " +"("+ self.especialidad+") : ¡Desafio a "+ enemigo.nombre+" ("+ enemigo.especialidad+") a un juego de mesa!")

		return self.jugar_mesa(enemigo)




# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorCartas(Jugador):

	def __init__(self, nombre, equipo, especialidad, energia,**kwargs):
		super().__init__(nombre, equipo, especialidad, energia,**kwargs)

		self.inteligencia=self.energia*2.5
# Completar 
# ¡Aprovecha herencia!



	def jugar_cartas(self, enemigo):
# Completar
		if enemigo.inteligencia< self.inteligencia:
			print("ganó "+ self.nombre)
			return True
		else:
			print("ganó "+ enemigo.nombre)
			return False
	def enfrentar(self, tipo_de_juego, enemigo):
		print(self.equipo + " " +self.nombre+ " " +"("+ self.especialidad+") : ¡Desafio a "+ enemigo.nombre+" ("+ enemigo.especialidad+") a un juego de cartas!")
		return self.jugar_cartas(enemigo)


# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorCombate(Jugador):

	def __init__(self, nombre, equipo, especialidad, energia,**kwargs):
		super().__init__(nombre, equipo, especialidad, energia,**kwargs)
		self.audacia=max(self.energia, random.randint(3, 5))
# Completar 
# ¡Aprovecha herencia!



	def jugar_combate(self, enemigo):
		if enemigo.audacia< self.audacia:
			print("ganó "+ self.nombre)
			return True
		else:
			print("ganó "+ enemigo.nombre)
			return False

	def enfrentar(self, tipo_de_juego, enemigo):
		print(self.equipo + " " +self.nombre+ " " +"("+ self.especialidad+") : ¡Desafio a "+ enemigo.nombre+" ("+ enemigo.especialidad+") a un combate!")
		return self.jugar_combate(enemigo)





# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorCarreras(Jugador):

	def __init__(self, nombre, equipo, especialidad, energia,**kwargs):
# Completar 
# ¡Aprovecha herencia!
		super().__init__(nombre, equipo, especialidad, energia,**kwargs)
		self.trampa=self.energia*3



	def jugar_carrera(self, enemigo):
# Completar
		if enemigo.trampa< self.trampa:
			print("ganó "+ self.nombre)
			return True
		else:
			print("ganó "+ enemigo.nombre)
			return False

	def enfrentar(self, tipo_de_juego, enemigo):
		print(self.equipo + " " +self.nombre+ " " +"("+ self.especialidad+") : ¡Desafio a "+ enemigo.nombre+" ("+ enemigo.especialidad+") a una carrera!")
		return self.jugar_carrera(enemigo)



# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorInteligente(JugadorCartas, JugadorMesa):

	def __init__(self, nombre, equipo, especialidad, energia,**kwargs):
		super().__init__(nombre, equipo, especialidad, energia,**kwargs)
		self.audacia=3
		self.trampa=3
		self.nerviosismo=min(self.energia, random.randint(0, 3))
		self.inteligencia=self.energia*2.5
# Completar 
# ¡Aprovecha herencia!




# Completar la siguiente clase.
# Puedes agregarle herencia.
# Puedes agregar métodos incluso.
class JugadorIntrepido(JugadorCarreras, JugadorCombate):

	def __init__(self, nombre, equipo, especialidad, energia, **kwargs):
# Completar 
# ¡Aprovecha herencia!
		super().__init__(nombre, equipo, especialidad, energia,**kwargs)
		self.nerviosismo=3
		self.inteligencia=3
		self.audacia=max(self.energia, random.randint(3, 5))
		self.trampa=self.energia*3

