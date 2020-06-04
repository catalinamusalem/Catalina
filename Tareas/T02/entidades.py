import sys
from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from random import random
import p
from threading import Thread, current_thread, Event, Timer
from time import sleep
from math import floor

class Bocadillo(QLabel):
    
    def __init__(self, *args):
        super().__init__(*args)
        self.disponible = True
    def aparecer(self,x, y):
        self.move(x+ 10, y + 30)
        self.setPixmap((QPixmap(p.RUTA_BOCADILLO)).scaled(p.LARGO_BOCADILLO,p.ANCHO_BOCADILLO))
        self.show()
    def desaparecer(self):
        self.setPixmap(QPixmap())
    def calidad_pedido(self, nivel_chef, tiempo_espera ):
        probabilidad = max(0,((nivel_chef * (1-tiempo_espera * 0.05)/3)))
        numero = random()
        if numero < probabilidad:
            return True 
        else:
            return False
        
        

   


#class DCCafe(Qlabel):
    
class Clientes(QLabel):
    def __init__(self, *args):
        super().__init__(*args)
        self.estado_animo = "alegre"
        self.hora_llegada = -100
        self.recibio_plato = False
        self.sentado = False
        self.posicion_x = 0
        self.posicion_y = 0
        self.tipo_cliente()
        self.se_acaba_de_retirar= False
    
    def asociar_tiempo(self, tiempo):
        self.tiempo = tiempo

    def tipo_cliente(self): 
        
        numero = random()
        if numero <= p.PROB_RELAJADO:
            self.tipo = "relajado"

        else:
            self.tipo = "apurado"
    def sentarse(self, posx, posy,mesa):
        self.hora_llegada = self.tiempo.tiempo
        self.sentado = True
        self.posicion_x = posx
        self.posicion_y = posy -70
        self.move(posx,posy-70)
        self.setPixmap((QPixmap(p.RUTA_CLIENTE_ALEGRE)).scaled(p.LARGO_CLIENTE,p.ANCHO_CLIENTE))
        self.show()
        self.mesa = mesa
        
    def cambio_animo(self):
        
        if self.tipo == "relajado" and self.recibio_plato == False :
            self.estado_animo = "enojado"
            pixeles = QPixmap(p.RUTA_CLIENTE_ENOJADO)
            self.setPixmap((pixeles).scaled(p.LARGO_CLIENTE,p.ANCHO_CLIENTE))
            self.move(self.posicion_x,self.posicion_y)

        if self.tipo == "apurado" and self.recibio_plato == False :
            self.estado_animo = "enojado"
            pixeles = QPixmap(p.RUTA_CLIENTE_ENOJADO)
            self.setPixmap((pixeles).scaled(p.LARGO_CLIENTE,p.ANCHO_CLIENTE))
            self.move(self.posicion_x,self.posicion_y)

    def recibir_bocadillo(self,bocadillo):
        self.hora_recibio_bocadillo = self.tiempo.tiempo
        self.recibio_plato = True
        self.bocadillo = bocadillo
        self.tiempo_espera = self.hora_recibio_bocadillo - self.hora_llegada
        
    def propina(self ):
        return p.PROPINA
    def retirarse(self):
        self.propina()
        self.setPixmap(QPixmap())
        self.mesa.desocupar()
        self.sentado = False
        if self.recibio_plato == True:
            self.bocadillo.desaparecer()
    def forzar_salida(self):
         self.setPixmap(QPixmap())


        
class Mesa(QLabel):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usada = False
        self.tiene_comida = False 
        
        
        self.tiene_bocadillo = False #para ver si esta conectada a un bocadillo 
    def posicion(self,x,y):
        self.pos_x = x
        self.pos_y = y

    def ocupar(self,cliente):
        self.usada = True
        self.cliente = cliente 
    def desocupar(self):
        self.usada = False
        self.tiene_comida = False
    def choque(self, mesero):
        if mesero.lleva_comida == True and self.usada == True and self.tiene_comida == False:
            self.cliente.recibir_bocadillo(self.bocadillo)
            self.tiene_comida= True
            mesero.comida_entregada()
            self.bocadillo.aparecer(self.pos_x, self.pos_y)
            self.nivel_chef = mesero.nivel_chef
    def conectar(self,bocadillo):
        self.bocadillo = bocadillo
        self.tiene_bocadillo = True
    def desaparecer(self):
        self.setPixmap(QPixmap())

class RelojInterno():
    def __init__(self, cafe,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocidad = p.VELOCIDAD_RELOJ
        self.__tiempo = 0
        self.senal = False
        self.reloj = QTimer()
        self.reloj.setInterval((1/p.VELOCIDAD_RELOJ) * 1000)
        self.reloj.timeout.connect(self.run)
        self.clientes= []
        self.DCCafe = cafe
        
    @property
    def tiempo(self):
        return self.__tiempo
    @tiempo.setter
    def tiempo(self, p):
        self.__tiempo = p
    def pausar(self,senal):
        if senal == True:
            self.reloj.stop()
        else:
            self.reloj.start()
        for chef in self.DCCafe.empleados[1::]:
            chef.pausar()    
    
    def run(self):
        self.reloj.start()  
        self.tiempo += 1  
        
        for i in self.DCCafe.clientes:
           
            if i.tipo == "relajado":
                if self.tiempo == i.hora_llegada + (1/self.velocidad)*(p.TIEMPO_ESPERA_RELAJADO/2):
                    i.cambio_animo()

            if i.tipo == "apurado":
                if self.tiempo == i.hora_llegada + (1/self.velocidad)*(p.TIEMPO_ESPERA_APURADO/2):
                    i.cambio_animo()
            if i.tipo == "relajado": 
                if self.tiempo == i.hora_llegada+(1/self.velocidad)*(p.TIEMPO_ESPERA_RELAJADO):
                    i.retirarse()
                    self.DCCafe.actualizar()
                    self.DCCafe.calidad_pedido(i)
                    self.DCCafe.avanzar_lista_espera()
                    if i.recibio_plato == True:
                        self.DCCafe.pedidos_exitosos += 1
                        self.DCCafe.pago_clientes += p.PRECIO_BOCADILLO
                        self.DCCafe.dinero_total += p.PRECIO_BOCADILLO
                    else:
                        self.DCCafe.pedidos_perdidos += 1
                
            if i.tipo == "apurado":
                if self.tiempo == i.hora_llegada +(1/self.velocidad)*(p.TIEMPO_ESPERA_APURADO):
                    i.retirarse()
                    self.DCCafe.actualizar()
                    self.DCCafe.calidad_pedido(i)
                    self.DCCafe.avanzar_lista_espera()
                    if i.recibio_plato == True:
                        self.DCCafe.pedidos_exitosos += 1
                        self.DCCafe.pago_clientes += p.PRECIO_BOCADILLO
                        self.DCCafe.dinero_total += p.PRECIO_BOCADILLO
                    else:
                        self.DCCafe.pedidos_perdidos += 1
            
        print(self.tiempo)    
    def stop(self):
        self.reloj.stop()
    


        
        

class DCCafe():
    
    def __init__(self, senal_actualizar_estadisticas,senal_terminar_juego,*args, **kwargs):
        self.ganancias_ronda = 0
        self.pago_clientes = 0
        self.propina_clientes = 0
        self.pedidos_exitosos = 0
        self.pedidos_totales = 0
        self.empleados = []
        self.clientes = []
        self.mesas = []
        self.puntos_reputacion = 5
        self.__dinero_total = p.DINERO_INICIAL
        self.ronda = 0
        self.disponibilidad = False
        self.lista_espera = []
        self.senal_actualizar_estadisticas = senal_actualizar_estadisticas
        self.senal_terminar_juego = senal_terminar_juego
        self.pedidos_perdidos = 0
   
    def comenzar(self):
        self.disponibilidad = True
        self.clientes= []
        self.ganancias_ronda = 0
        self.pago_clientes = 0
        self.propina_clientes = 0
        self.pedidos_exitosos = 0
        self.pedidos_totales = 0
        self.pedidos_perdidos = 0
        self.tiempo_de_preparacion()
        self.ronda += 1
        self.empleados[0].lleva_comida = False
        self.senal_actualizar_estadisticas.emit()   
        

    
    def calcular_reputacion(self):
        puntos = self.puntos_reputacion
        a = max(0,min(5,(puntos + floor(4*(self.pedidos_exitosos/self.pedidos_totales)-2))))
        self.puntos_reputacion = a
    def clientes_ronda(self):
        
        return  5*(1+ self.ronda)
    def tiempo_de_preparacion(self):
        for chef in self.empleados[1::]:
            chef.tiempo_de_preparacion(self.puntos_reputacion)
    def avanzar_lista_espera(self):
        clientes_sentados = 0
        for cliente in self.lista_espera:
            for mesa in self.mesas:
                if mesa.usada == False:
                    mesa.ocupar(cliente)
                    self.pedidos_totales += 1
                    #cliente.hora_llegada = tiempo
                    self.lista_espera.pop(0)
                    cliente.sentarse(mesa.pos_x,mesa.pos_y, mesa)
                    return " "
                    break
        for cliente in self.clientes:   
            if cliente.sentado == True:
                clientes_sentados += 1
        if self.lista_espera == [] and clientes_sentados == 0:
            if self.clientes_ronda() == self.pedidos_totales:
                self.disponibilidad = False
                self.senal_terminar_juego.emit()
                for chef in self.empleados[1::]:
                    chef.terminar_ronda()
        self.senal_actualizar_estadisticas.emit()     
    def calidad_pedido(self,cliente):
        bocadillo = cliente.mesa.bocadillo
        if cliente.recibio_plato == True:
            if bocadillo.calidad_pedido(cliente.mesa.nivel_chef, cliente.tiempo_espera) == True:
                self.propina_clientes += p.PROPINA
                self.dinero_total += p.PROPINA
    
    def actualizar(self):
        self.senal_actualizar_estadisticas.emit()  

       





            
    
            
        
    






        


        
            
            
            




    