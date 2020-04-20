from abc import ABC, abstractmethod
from random import randint, choice, random
import p
import crear
import Tarea1c

class Magizoologo(ABC):
    def __init__(self, n, tipo, criat, alim, sick, lic, n_mag, dest, e_tot, respo, h_es):
        self.nombre = n
        self.criaturas = criat
        self.alimentos = alim
        self.__sickles = int(sick)
        self.licencia = lic
        self.nivel_de_aprobacion = int(p.NIVEL_APROBACION)
        self.nivel_magico = int(n_mag)
        self.destreza = int(dest)
        self.energia_total = int(e_tot)
        self.responsabilidad = int(respo)
        self.habilidad_especial_usada = str(h_es).strip()
        self.energia_actual = int(e_tot)
        self.tipo = tipo
    @property
    def sickles(self):
        return self.__sickles
    @sickles.setter
    def sickles(self, p):
        if p < 0:
            self.__sickles = 0
        else:
            self.__sickles = p
    def adoptar_criatura(self, criatura):
        if type(criatura) == Augurey:
            self.sickles -= p.PRECIO_AUGUREY
            self.criaturas.append(criatura)
            print("Augurey adoptado!!")
        if type(criatura) == Niffler:
            self.sickles -= p.PRECIO_NIFFLER
            self.criaturas.append(criatura)
            print("Niffler adoptado!!")
        if type(criatura) == Erkling:
            self.sickles -= p.PRECIO_ERKLING
            self.criaturas.append(criatura)
            print("Erkling adoptado!!")
    def comprar_alimentos(self, tipo_de_alimento):
        self.alimentos.append(tipo_de_alimento)
    def recuperar_criatura(self, criatura):
        if self.energia_actual > p.COSTO_ENERGETICO_RECUPERAR:
            self.energia_actual -= p.COSTO_ENERGETICO_RECUPERAR
            a = self.destreza + self.nivel_magico - criatura.nivel_magico
            b = self.destreza + self.nivel_magico + criatura.nivel_magico
            probabilidad_recuperar = min(1, max(0, a / b))
            probabilidad = random()
            if probabilidad <= probabilidad_recuperar:
                criatura.estado_escape = "False"
                print("Criatura recuperada!!")
            else:
                print("No fue posible recuperar la criatura")
        else:
            print("No tienes energía suficiente para realizar esta acción")
    def sanar_criatura(self, criatura):
        if self.energia_actual >= p.COSTO_ENERGETICO_SANAR:
            self.energia_actual -= p.COSTO_ENERGETICO_SANAR
            a = self.nivel_magico - criatura.salud_actual
            b = self.nivel_magico + criatura.salud_actual
            probabilidad_sanar = min(1, max(0, a / b))
            probabilidad = random()
            
            if probabilidad <= probabilidad_sanar:
                criatura.estado_salud = "False"
                print("La criatura ha sido sanada!!")
            else:
                print("No fue posible sanar a la criatura")
        else:
            print("No tienes energía suficiente para realizar esta acción")
    @abstractmethod
    def habilidad_especial(self):
        pass
    @abstractmethod
    def alimentar(self, criatura, alimento):
        pass
class MagizoologoDocencio(Magizoologo):
    def alimentar(self, criatura, alimento):
        if self.energia_actual >= p.COSTO_ENERGETICO_ALIMENTAR:
            if alimento in self.alimentos:
                if criatura in self.criaturas:
                    a = alimento.alimentar(criatura)
                    self.alimentos.remove(alimento)
                    self.energia_actual -= p.COSTO_ENERGETICO_ALIMENTAR
                    if a == "comio":
                        criatura.salud_total += p.AUMENTO_SALUD_DOCENCIO
            if criatura.ataque_mago == "True":
                self.energia_actual -= max(10, self.nivel_magico - criatura.nivel_magico)
                print("Has sido atacad@ por tu criatura")
        else:
            print("No tienes energía suficiente para realizar esta acción")
    def recuperar_criatura(self, criatura):
        if self.energia_actual > p.COSTO_ENERGETICO_RECUPERAR:
            self.energia_actual -= p.COSTO_ENERGETICO_RECUPERAR
            a = self.destreza + self.nivel_magico - criatura.nivel_magico
            b = self.destreza + self.nivel_magico + criatura.nivel_magico
            probabilidad_recuperar = min(1, max(0, a / b))
            probabilidad = random()
            if probabilidad <= probabilidad_recuperar:
                criatura.estado_escape = "False"
                criatura.salud_actual -= p.DESCUENTO_SALUD_DOCENCIO
                print("Criatura recuperada!!")
            else:
                print("No fue posible recuperar la criatura")
        else:
            print("No tienes energía suficiente para realizar esta acción")
    def habilidad_especial(self):
        if self.energia_actual > p.COSTO_ENERGETICO_HABILIDAD_ESPECIAL:
            if self.habilidad_especial_usada == "True":
                self.habilidad_especial_usada = "False"
                self.energia_actual -= p.COSTO_ENERGETICO_HABILIDAD_ESPECIAL
                for criatura in self.criaturas:
                    criatura.sin_comer = 0
                    criatura.nivel_hambre = "satisfecha"
            else:
                print("Ya usaste una vez tu habilidad especial")
        else:
            print("No tienes energía suficiente para realizar esta acción")
class MagizoologoTareo(Magizoologo):
    def alimentar(self, criatura, alimento):
        if self.energia_actual >= p.COSTO_ENERGETICO_ALIMENTAR:
            if alimento in self.alimentos:
                if criatura in self.criaturas:
                    a = alimento.alimentar(criatura)
                    self.alimentos.remove(alimento)
                    self.energia_actual -= p.COSTO_ENERGETICO_ALIMENTAR
                    probabilidad = random()
                    if a == "comio":
                        if probabilidad <= p.PROBABILIDAD_SALUD_TAREO:
                            criatura.salud_actual = criatura.salud_total
            if criatura.ataque_mago == "True":
                self.energia_actual -= max(10, self.nivel_magico - criatura.nivel_magico)
                print("Has sido atacad@ por tu criatura")       
        else:
            print("No tienes energía suficiente para realizar esta acción")    
    def habilidad_especial(self):
        if self.energia_actual > p.COSTO_ENERGETICO_HABILIDAD_ESPECIAL:
            if self.habilidad_especial_usada == "True":
                self.habilidad_especial_usada = "False"
                self.energia_actual -= p.COSTO_ENERGETICO_HABILIDAD_ESPECIAL
                for criatura in self.criaturas:
                    criatura.estado_escape = "False"
            else:
                print("Ya usaste una vez tu habilidad especial")
        else:
            print("No tienes energía suficiente para realizar esta acción")     
class MagizoologoHibrido(Magizoologo):
    def alimentar(self, criatura, alimento):
        if self.energia_actual >= p.COSTO_ENERGETICO_ALIMENTAR:
            if alimento in self.alimentos:
                if criatura in self.criaturas:
                    a = alimento.alimentar(criatura)
                    self.alimentos.remove(alimento)
                    self.energia_actual -= p.COSTO_ENERGETICO_ALIMENTAR
                    if a == "comio":
                        criatura.salud_actual += p.RECUPERAR_SALUD_HIBRIDO
            if criatura.ataque_mago == "True":
                self.energia_actual -= max(10, self.nivel_magico - criatura.nivel_magico)
                print("Has sido atacad@ por tu criatura")
        else:
            print("No tienes energía suficiente para realizar esta acción")
    def habilidad_especial(self):
        if self.energia_actual > p.COSTO_ENERGETICO_HABILIDAD_ESPECIAL:
            if self.habilidad_especial_usada == "True":
                self.habilidad_especial_usada = "False"
                self.energia_actual -= p.COSTO_ENERGETICO_HABILIDAD_ESPECIAL
                for criatura in self.criaturas:
                    criatura.estado_salud = "False"
            else:
                print("Ya usaste una vez tu habilidad especial")
        else:
            print("No tienes energía suficiente para realizar esta acción") 
############################DCC#############################################################
class DCC:
    def __init__(self, magico):
        self.magizoologo = magico
        self.multas = []
        self.pago_multas = 0
    def vender_criatura(self, criatura, nombre_criatura):
        if self.magizoologo.licencia == "True":
            if criatura.lower() == "augurey" and self.magizoologo.sickles >= p.PRECIO_AUGUREY:
                self.magizoologo.adoptar_criatura(crear.crear_augurey(nombre_criatura))
            elif criatura.lower() == "niffler" and self.magizoologo.sickles >= p.PRECIO_NIFFLER:
                self.magizoologo.adoptar_criatura(crear.crear_niffler(nombre_criatura))
            elif criatura.lower() == "erkling" and self.magizoologo.sickles >= p.PRECIO_ERKLING:
                self.magizoologo.adoptar_criatura(crear.crear_erkling(nombre_criatura))
            else:
                print("No tienes Sickles suficientes")
        else:
            print("Debes tener tu licencia para poder adoptar")
    def vender_alimentos(self, tipo_de_alimento):
        if tipo_de_alimento.lower() == "tarta de melaza" and \
            self.magizoologo.sickles >= p.PRECIO_TARTA:
            self.magizoologo.comprar_alimentos(Tarea1c.TartaDeMelaza())
            self.magizoologo.sickles -= p.PRECIO_TARTA
        elif tipo_de_alimento.lower() == "buñuelo de gusarajo" and \
            self.magizoologo.sickles >= p.PRECIO_BUÑUELOS:
            self.magizoologo.comprar_alimentos(Tarea1c.BuñueloDeGusarajo())
            self.magizoologo.sickles -= p.PRECIO_BUÑUELOS
        elif tipo_de_alimento.lower() == "hígado de dragón" and \
            self.magizoologo.sickles >= p.PRECIO_HIGADO:
            self.magizoologo.comprar_alimentos(Tarea1c.HigadoDeDragon())
            self.magizoologo.sickles -= p.PRECIO_HIGADO
        else:
             print("No tienes Sickles suficientes")
    def nivel_de_aprobacion(self):
        criat_sanas = 0
        criat_retenidas = 0
        cr_tot = len(self.magizoologo.criaturas)
        for i in self.magizoologo.criaturas:
            if i.estado_salud == "False":
                criat_sanas += 1
            if i.estado_escape == "False":
                criat_retenidas += 1
        nivel_aprobacion = min(100, max(0, 100 * (criat_sanas + criat_retenidas) / (2 * cr_tot)))
        print(f"Nivel de aprobación: {int(nivel_aprobacion)}")
        if nivel_aprobacion <= 60:
            if self.magizoologo.licencia == "True":
                print("Has perdido tu licencia :(")
            else: 
                print("No recuperaste tu licencia :(")
            self.magizoologo.licencia = "False"
        else:
            if self.magizoologo.licencia == "True":
                print("Continuas con tu licencia!!")
            else:
                print("Recuperaste tu licencia!!")
            self.magizoologo.licencia = "True"
        self.magizoologo.nivel_de_aprobacion = int(nivel_aprobacion)
    def pagar_magizoologos(self):
        pago = (self.magizoologo.nivel_de_aprobacion * 4) + (len(self.magizoologo.alimentos) * 15)\
             + (self.magizoologo.nivel_magico * 3)
        self.magizoologo.sickles += pago
        print(f"El DCC te ha pagado {int(pago)} Sickles")
        print(f"Se te han descontado {self.pago_multas} Sickles en multas")
        if self.magizoologo.sickles <= self.pago_multas: 
            self.magizoologo.sickles += multa[0][1]
            print("No tienes Sickles suficientes para pagar las multas, pierdes tu licencia")
            self.magizoologo.licencia = "False"
        self.magizoologo.sickles -=self.pago_multas
        print(f"Tu saldo actual es de {int(self.magizoologo.sickles)} Sickles") 
    def fiscalizar_magizoologos(self):
        self.multas = []
        self.pago_multas = 0
        print("Resumen de los eventos de hoy")
        for criatura in self.magizoologo.criaturas:
            a = criatura.nivel_hambre
            criatura.pasar_dia(self.magizoologo)
            b = criatura.nivel_hambre
            if a == "satisfecha" and b == "hambrienta":
                print(f"{criatura.nombre} paso a estar hambrienta!!")
            c = criatura.estado_escape
            criatura.escaparse(self.magizoologo)
            d = criatura.estado_escape
            if c == "False" and d == "True":
                print(f"{criatura.nombre} se escapo!!")
                probabilidad = random()
                if probabilidad <= p.PROBABILIDAD_MULTA_ESCAPE:
                    k = [f"Has recibido una multa porque {criatura.nombre} escapó", p.MULTA_ESCAPE]
                    self.multas.append(k)
                    self.pago_multas += p.MULTA_ESCAPE
            e = criatura.estado_salud
            criatura.enfermarse(self.magizoologo)
            f = criatura.estado_salud
            if e == "False" and f == "True":
                print(f"{criatura.nombre} se enfermo!!")
                probabilidad = random()
                if probabilidad <= p.PROBABILIDAD_MULTA_ENFERMEDAD:
                    a_pagar = p.MULTA_ENFERMEDAD
                    k = [f"Has recibido una multa porque {criatura.nombre} se enfermó", a_pagar] 
                    self.multas.append(k)
                    self.pago_multas += p.MULTA_ENFERMEDAD
            if criatura.salud_actual == p.MINIMO_SALUD_ACTUAL:
                q =  p.MULTA_SALUD_BAJA
                k = [f"Has recibido una multa porque {criatura.nombre} llegó al mínimo de salud",q]
                self.multas.append(k)
                self.pago_multas += p.MULTA_SALUD_BAJA
        self.magizoologo.energia_actual = self.magizoologo.energia_total   
   

#################################CRIATURAS#################################
class DCCriaturas(ABC):
    def __init__(self, n, tipo, n_mag, s_tot, s_act, esc, enf, salud, ham, comer, agres, n_c, e):
        self.nombre = n
        self.nivel_magico = int(n_mag)
        self.salud_total = int(s_tot)
        self.__salud_actual = int(s_act)
        self.prob_escape = float(esc)
        self.prob_enfermar = float(enf)
        self.estado_salud = salud
        self.nivel_hambre = str(ham)
        self.sin_comer = int(comer)
        self.nivel_agresividad = str(agres)
        self.nivel_cleptomania = int(n_c)
        self.estado_escape = (e)
        self.ataque_mago = "False"
        self.tipo = tipo
    @property
    def salud_actual(self):
        return self.__salud_actual
    @salud_actual.setter
    def salud_actual(self, p):
        if p > self.salud_total:
            self.__salud_actual = self.salud_total
        elif p <= 1:
            self.__salud_actual = 1
        else:
            self.__salud_actual = p
    def alimentarse(self):
        if self.nivel_hambre == "satisfecha":
            efecto_hambre = p.EFECTO_HAMBRE_SATISFECHA
        else:
            efecto_hambre = p.EFECTO_HAMBRE_HAMBRIENTA
        if self.nivel_agresividad == "inofensiva":
            efecto_agresividad = p.EFECTO_AGRESIVIDAD_INOFENSIVA
        if self.nivel_agresividad == "arisca":
            efecto_agresividad = p.EFECTO_AGRESIVIDAD_ARISCA
        if self.nivel_agresividad == "peligrosa":
            efecto_agresividad = p.EFECTO_AGRESIVIDAD_PELIGROSA
        probabilidad_ataque = min(1, (efecto_hambre + efecto_agresividad) / 100)
        probabilidad = random()
        if probabilidad <= probabilidad_ataque:
            self.ataque_mago = "True"
        else:
            self.ataque_mago = "False"
    def escaparse(self, magico):
        if self.nivel_hambre == "satisfecha":
            ef_hambre = p.EFECTO_HAMBRE_SATISFECHA_ESCAPARSE
        else:
            ef_hambre = p.EFECTO_HAMBRE_HAMBRIENTA_ESCAPARSE
        p_escaparse = min (1, self.prob_escape + max(0, (ef_hambre - magico.responsabilidad)/ 100))
        probabilidad = random()
        if probabilidad <= p_escaparse:
            self.estado_escape = "True"  
    def enfermarse(self, magico):
        a = (self.salud_total - self.salud_actual) / self.salud_total
        b = magico.responsabilidad / 100 
        probabilidad_enfermarse = min(1, self.prob_enfermar + max(0, a-b))
        probabilidad = random()
        if probabilidad <= probabilidad_enfermarse:
            self.estado_salud = "True"
            print(f"{self.nombre} perdió salud por enfermedad")
        else:
            self.estado_salud = "False"
class Augurey(DCCriaturas):
    def pasar_dia(self, magico):
        self.sin_comer += 1
        if self.sin_comer == 3:
            self.nivel_hambre = "hambrienta"
        if self.nivel_hambre == "hambrienta":
            self.salud_actual -= p.DESCUENTO_CRIATURA_HAMBRIENTA
        if self.estado_salud == "True":
            self.salud_actual -= p.DESCUENTO_ESTADO_SALUD
        if self.nivel_hambre == "satisfecha" and self.estado_salud == "False" and \
            self.salud_actual == self.salud_total:
            alim = choice([TartaDeMelaza(), HigadoDeDragon(), BuñueloDeGusarajo()])
            magico.alimentos.append(alim)
class Niffler(DCCriaturas):   
    def pasar_dia(self, magico):
        self.sin_comer += 1
        if self.sin_comer == 2:
            self.nivel_hambre = "hambrienta"
        if self.estado_salud == "True":
            self.salud_actual -= p.DESCUENTO_ESTADO_SALUD
        cleptomania = self.nivel_cleptomania * 2
        if self.nivel_hambre == "hambrienta":
            self.salud_actual -= p.DESCUENTO_CRIATURA_HAMBRIENTA
        if self.nivel_hambre == "satisfecha":
            magico.sickles += cleptomania
        else:
            magico.sickles -= cleptomania
class Erkling(DCCriaturas):
    def pasar_dia(self, magico):
        self.sin_comer += 1
        if self.sin_comer == 2:
            self.nivel_hambre = "hambrienta"
        if self.estado_salud == "True":
            self.salud_actual -= p.DESCUENTO_ESTADO_SALUD
        if self.nivel_hambre == "hambrienta":
            self.salud_actual -= p.DESCUENTO_CRIATURA_HAMBRIENTA
            if len(magico.alimentos) >= 1:
                a = choice(magico.alimentos)
                magico.alimentos.remove(a)
                self.sin_comer = 0
                self.nivel_hambre == "satisfecha"


