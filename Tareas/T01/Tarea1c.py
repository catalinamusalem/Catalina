
from random import  random
import p
import Tarea1
################################ALIMENTOS###############################################
class TartaDeMelaza:
    def __init__(self):
        self.nombre = "Tarta de Melaza"
        self.efecto_salud = int(p.EFECTO_SALUD_MELAZA)
    def alimentar(self, criatura):
        criatura.salud_actual += self.efecto_salud
        criatura.nivel_hambre = "satisfecha"
        criatura.sin_comer = 0
        criatura.alimentarse()
        if criatura.tipo == "Niffler":
            probabilidad = random()
            if probabilidad <= p.PROBABILIDAD_TARTA_MELAZA:
                criatura.agresividad = "inofensiva"
        return "comio"
class HigadoDeDragon:
    def __init__(self):
        self.nombre = "Hígado de Dragón"
        self.efecto_salud = int(p.EFECTO_SALUD_HIGADO_DRAGON)
    def alimentar(self, criatura):
        criatura.salud_actual += self.efecto_salud
        criatura.estado_salud = "False"
        criatura.nivel_hambre = "satisfecha"
        criatura.alimentarse()
        criatura.sin_comer = 0
        return "comio"
class BuñueloDeGusarajo:
    def __init__(self):
        self.nombre = "Buñuelo de Gusarajo"
        self.efecto_salud = int(p.EFECTO_SALUD_BUÑUELO_DE_GUSARAJO)
    def alimentar(self, criatura):
        probabilidad = random()
        if probabilidad <= p.PROBABILIDAD_BUÑUELO_GUSARAJO:
            criatura.salud_actual += self.efecto_salud
            criatura.nivel_hambre = "satisfecha"
            criatura.sin_comer = 0
            return "comio"
        else:
            print("La criatura rechazó el alimento :(")
        criatura.alimentarse() 