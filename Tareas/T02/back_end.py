import p
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from random import randint
from threading import Thread, Timer
import entidades
class SenalesBackEnd(QObject):
    senal_actualizar_estadisticas = pyqtSignal()
    senal_terminar_juego = pyqtSignal()

class Logica(QObject): 
    senal_mapa_cargado = pyqtSignal(list)
    senal_movimiento_posible =pyqtSignal(bool, str)
    senal_llegada_cliente = pyqtSignal()
    senal_bocadillo_creado = pyqtSignal()
    senal_terminar_ronda = pyqtSignal(list)
    senal_terminar_ronda_ventana_principal = pyqtSignal()
    senal_resultado_revisar = pyqtSignal(str, str)
    senal_actualizar_estadisticas_vp = pyqtSignal(list)
    def __init__(self, senal_actualizar_estadisticas, senal_terminar_juego, *args):
        super().__init__(*args)
        self.mapa = []
        self.juego_en_curso = False
        self.senal_actualizar_estadisticas = senal_actualizar_estadisticas
        self.senal_actualizar_estadisticas.connect(self.actualizar_estadisticas)
        self.senal_terminar_juego = senal_terminar_juego
        self.senal_terminar_juego.connect(self.terminar_ronda_)
        self.DCCafe =entidades.DCCafe(self.senal_actualizar_estadisticas,self.senal_terminar_juego)
        self.tiempo = entidades.RelojInterno(self.DCCafe)
        
        
        
        
        
    def cargar_entidades(self,mesero,mesas,cocinas):
        self.DCCafe.empleados.append(mesero)
        j = 0
        k = 0 
        for i in self.mapa:
            if i[0] == "mesa":
                i.append(mesas[j])
                j += 1
            if i[0] == "chef":
                i.append(cocinas[k])
                k += 1

        for mesa in mesas:
            self.DCCafe.mesas.append(mesa)
        contador = 0
        for cocina in cocinas:
            cocina.platos_preparados = int(self.platos_preparados[contador])
            contador += 1
            self.DCCafe.empleados.append(cocina)
        self.DCCafe.dinero_total = int(self.datos_iniciales[0])
        self.DCCafe.puntos_reputacion = int(self.datos_iniciales[1])
        self.DCCafe.ronda = int(self.datos_iniciales[2])
       
        
    # Continuar con una partida guardada
    def cargar_juego(self):
        with open(p.RUTA_MAPA_CSV, 'rt', encoding="utf-8") as archivo:
            lineas_mapa = archivo.readlines()
        lineas_limpias = []
        cantidad_mesas = 0
        for linea in lineas_mapa:
            a=linea.strip().split(",")
            a[1] = int(a[1])
            a[2] = int(a[2])
            
            if a[0] == "mesero":
                self.mapa.append(["mesero",[a[1],a[1]+p.LARGO_MESERO],[a[2],a[2]+ p.ANCHO_MESERO]])
                a.append(p.MSRO_ABAJO_2)
            if a[0] == "mesa":
                
                self.mapa.append(["mesa",[a[1],a[1] + p.LARGO_MESA],[a[2], a[2] + p.ANCHO_MESA]])
                a.append(p.RUTA_MESA)
                
                cantidad_mesas += 1
            if a[0] == "chef":
                
                self.mapa.append(["chef",[a[1],a[1] + p.LARGO_COCINA],[a[2], a[2]+p.ANCHO_COCINA]])
                a.append(p.RUTA_COCINA)
                
            lineas_limpias.append(a)
        with open(p.RUTA_DATOS, 'rt', encoding="utf-8") as archivo_datos:
            lineas_datos = archivo_datos.readlines()
        lineas_limpias_datos = []
        for linea in lineas_datos:
            b=linea.strip().split(",")
            lineas_limpias_datos.append(b)
        self.platos_preparados = lineas_limpias_datos[1]
        self.datos_iniciales = lineas_limpias_datos[0]
        self.senal_mapa_cargado.emit([lineas_limpias, lineas_limpias_datos])
        for i in range(cantidad_mesas):
            self.senal_bocadillo_creado.emit()
#Revisar si hay algo en el espacio que se quiere mover la imagen
    def revisar_vacio(self,x,y,dimension):
        for i in range(x, x + dimension[0]):
            for j in range(y, y + dimension[1]):
                for objeto in self.mapa:
                    if i in range(objeto[1][0],objeto[1][1]):
                        if j in range(objeto[2][0],objeto[2][1]):
                            if objeto[0] == "mesero":
                                return objeto[0]
                            else:
                                self.choque(objeto)
                                return False
                                
        return True  
#Revisar vacio para tienda
    def revisar_vacio_tienda(self,x,y,dimension,tipo):
        resultado = "inicio"
        for objeto in self.mapa:
            if objeto[0] == "mesero":
                print(objeto)
                x = self.DCCafe.empleados[0].pos().x()
                y = self.DCCafe.empleados[0].pos().y()
                indice =self.mapa.index(objeto)
                self.mapa[indice] = ["mesero",[x,x + p.LARGO_MESERO],[y, y + p.ANCHO_MESERO]]
                

        for i in range(x, x + dimension[0]):
            for j in range(y, y + dimension[1]):
                for objeto in self.mapa:
                    if i in range(objeto[1][0],objeto[1][1]):
                        if j in range(objeto[2][0],objeto[2][1]):
                            resultado = "False"
                            return
        if x < p.LIMITE_X_INF:
            resultado = "False"
        if x + dimension[0] > p.LIMITE_X_SUP:
            resultado = "False"
        if y < p.LIMITE_Y_INF:
            resultado = "False"
        if y + dimension[0] > p.LIMITE_Y_SUP:
            resultado = "False"
        
        if resultado == "inicio":

            if tipo == "mesa": 
                if self.DCCafe.dinero_total > p.PRECIO_MESA and self.DCCafe.ronda != 0:
                    self.DCCafe.dinero_total -= p.PRECIO_MESA
                    resultado = "True"
                    self.mapa.append(["mesa",[x,x + p.LARGO_MESA],[y, y + p.ANCHO_MESA]])
                    
            if tipo == "chef":
                if self.DCCafe.dinero_total > p.PRECIO_COCINA and self.DCCafe.ronda != 0:
                    self.DCCafe.dinero_total -= p.PRECIO_COCINA
                    resultado = "True"
                    self.mapa.append(["chef",[x,x + p.LARGO_COCINA],[y, y + p.ANCHO_COCINA]])
            self.actualizar_estadisticas()
        self.senal_resultado_revisar.emit(resultado, tipo)

        

    def cargar_elemento_comprado(self, elemento):
        if self.mapa[-1][0] == "mesa":
            self.mapa[-1].append(elemento)
            self.DCCafe.mesas.append(elemento)
            self.senal_bocadillo_creado.emit()
        if self.mapa[-1][0] == "chef":
            self.mapa[-1].append(elemento)
            self.DCCafe.empleados.append(elemento)
           
        
#Crear una partida nueva 
    def juego_nuevo(self):
        objetos = []
        i = 0
        j = 0
        k = 0
        cantidad_mesas = 0
        while i < p.CHEF_INICIALES:
            x = randint(p.LIMITE_X_INF,p.LIMITE_X_SUP-p.LARGO_COCINA)
            y = randint(p.LIMITE_Y_INF,p.LIMITE_Y_SUP-p.ANCHO_COCINA)
            if self.revisar_vacio(x,y,[p.LARGO_COCINA, p.ANCHO_COCINA]) == True:
                objetos.append(["chef", x, y, p.RUTA_COCINA])
                self.mapa.append(["chef",[x,x + p.LARGO_COCINA],[y, y + p.ANCHO_COCINA]])
                i += 1
        while j < p.MESAS_INICIALES:
            x = randint(p.LIMITE_X_INF,p.LIMITE_X_SUP-p.LARGO_MESA)
            y = randint(p.LIMITE_Y_INF,p.LIMITE_Y_SUP-p.ANCHO_MESA)
            if self.revisar_vacio(x,y,[p.LARGO_MESA, p.ANCHO_MESA]) == True:
                objetos.append(["mesa", x, y, p.RUTA_MESA])
               
                self.mapa.append(["mesa",[x,x + p.LARGO_MESA],[y, y + p.ANCHO_MESA]])
                cantidad_mesas += 1
                j += 1
                
        
        while k == 0:
            x = randint(p.LIMITE_X_INF,p.LIMITE_X_SUP-p.LARGO_MESERO)
            y = randint(p.LIMITE_Y_INF,p.LIMITE_Y_SUP-p.ANCHO_MESERO)
            if self.revisar_vacio(x,y,[p.LARGO_MESERO, p.ANCHO_MESERO]) == True:
                objetos.append(["mesero", x, y, p.MSRO_ABAJO_2])
                self.mapa.append(["mesero",[x,x + p.LARGO_MESERO],[y, y + p.ANCHO_MESERO]])
                k += 1
        self.platos_preparados = []
        for i in range(p.CHEF_INICIALES):
            self.platos_preparados.append(0)
        self.datos_iniciales = [p.DINERO_INICIAL,p.REPUTACION_INICIAL,0]

        self.senal_mapa_cargado.emit([objetos,[self.datos_iniciales,self.platos_preparados]])
        for i in range(cantidad_mesas):
            self.senal_bocadillo_creado.emit()
        
    

    def mover_mesero(self, direccion, posicion):
        d = [p.LARGO_MESERO,p.ANCHO_MESERO]
        if direccion == "83":
            if  int(posicion[1]) + p.VEL_MOVIMIENTO + p.ANCHO_MESERO >= p.LIMITE_Y_SUP:
                revisar = False
            else:
                revisar =(self.revisar_vacio(int(posicion[0]),int(posicion[1])+p.VEL_MOVIMIENTO,d))
        elif direccion == "87":
            if int(posicion[1]) - p.VEL_MOVIMIENTO <= p.LIMITE_Y_INF:
                revisar = False
            else:
                revisar =(self.revisar_vacio(int(posicion[0]),int(posicion[1])-p.VEL_MOVIMIENTO,d))
        elif direccion == "65":
            if int(posicion[0]) - p.VEL_MOVIMIENTO <= p.LIMITE_X_INF:
                revisar = False
            else:
                revisar =(self.revisar_vacio(int(posicion[0])-p.VEL_MOVIMIENTO,int(posicion[1]),d))
        elif direccion == "68":
            if int(posicion[0]) + p.VEL_MOVIMIENTO + p.LARGO_MESERO >= p.LIMITE_X_SUP:
                revisar = False
            else:
                revisar =(self.revisar_vacio(int(posicion[0])+p.VEL_MOVIMIENTO,int(posicion[1]),d))
        
        if revisar == "mesero" or revisar == True:

            self.senal_movimiento_posible.emit(True, direccion)
        else:
            self.senal_movimiento_posible.emit(False,direccion)
    
    def asociar_bocadillo_mesa(self, bocadillo):
        
        for i in self.DCCafe.mesas:
            if i.tiene_bocadillo == False:
                i.conectar(bocadillo)
                break

    
    def jugar(self):

        self.juego_en_curso = True
        self.tiempo.run()
        self.actualizar_estadisticas()
        self.DCCafe.comenzar()
        
        self.llegada = QTimer()
        self.llegada.setInterval(p.LLEGADA_CLIENTES * (1/p.VELOCIDAD_RELOJ) * 1000)
        self.llegada.timeout.connect(self.llegada_clientes)
        self.llegada.start()
        self.guardar_juego()
        
    def choque(self, objeto):
        if self.juego_en_curso == True:
            objeto[3].choque(self.DCCafe.empleados[0])

    def pausa(self, estado):
        self.tiempo.pausar(estado)
        if estado == True:
            self.llegada.stop()
        else:
            self.llegada.start()
    def llegada_clientes(self):
        if len(self.DCCafe.clientes) < self.DCCafe.clientes_ronda():
            self.senal_llegada_cliente.emit()
        else:
            self.llegada.stop()
    def sentarse_clientes(self,cliente):
        cliente.asociar_tiempo(self.tiempo)
        self.DCCafe.clientes.append(cliente)
        self.DCCafe.lista_espera.append(cliente)
        self.DCCafe.avanzar_lista_espera()
        self.actualizar_estadisticas()
    

    def terminar_ronda_(self):
        if self.DCCafe.disponibilidad == False:
            self.actualizar_estadisticas()
            self.tiempo.stop()
            self.DCCafe.calcular_reputacion()
            dato_a = self.DCCafe.ronda
            dato_b = self.DCCafe.puntos_reputacion
            dato_c = self.DCCafe.dinero_total
            dato_d = self.DCCafe.pedidos_exitosos
            dato_e = self.DCCafe.pedidos_totales
            datos = [dato_a, dato_b, dato_c ,dato_d, dato_e - self.DCCafe.pedidos_exitosos]
            self.senal_terminar_ronda.emit(datos)
            self.senal_terminar_ronda_ventana_principal.emit()
    
    def aumentar_dinero(self):
        self.DCCafe.dinero_total += p.DINERO_TRAMPA
        print(self.DCCafe.dinero_total)
    def aumentar_reputacion(self):
        if self.DCCafe.puntos_reputacion + p.REPUTACION_TRAMPA > p.REPUTACION_MAXIMA:
            self.DCCafe.puntos_reputacion = p.REPUTACION_MAXIMA
        else:
            self.DCCafe.puntos_reputacion += p.REPUTACION_TRAMPA 

    def forzar_terminar_ronda(self):
        self.llegada.stop()
        self.DCCafe.disponibilidad = False
        for chef in self.DCCafe.empleados[1::]:
            chef.terminar_ronda()
        for cliente in self.DCCafe.clientes:
            cliente.forzar_salida()
        self.terminar_ronda_()
    def eliminar_mesa(self, x, y):
        if self.DCCafe.ronda != 0:
            if len(self.DCCafe.mesas) > 1:
                for objeto in self.mapa:
                    if objeto[0] == "mesa":
                        if x in range(objeto[1][0],objeto[1][1]):
                            if y in range(objeto[2][0],objeto[2][1]):
                                a = self.mapa.index(objeto)
                                self.mapa.pop(a)
                                
                                for mesa in self.DCCafe.mesas:
                                    if mesa == objeto[3]:
                                        mesa.desaparecer()
                                        b = self.DCCafe.mesas.index(objeto[3])
                                        self.DCCafe.mesas.pop(b)
            if len(self.DCCafe.empleados) > 2:
                for objeto in self.mapa:
                    if objeto[0] == "chef":
                        if x in range(objeto[1][0],objeto[1][1]):
                            if y in range(objeto[2][0],objeto[2][1]):
                                a = self.mapa.index(objeto)
                                self.mapa.pop(a)
                                
                                for chef in self.DCCafe.empleados[1::]:
                                    if chef == objeto[3]:
                                        chef.desaparecer()
                                        b = self.DCCafe.empleados.index(objeto[3])
                                        self.DCCafe.empleados.pop(b)



    
    def nueva_ronda(self):
        self.DCCafe.comenzar()
        self.llegada.start()
        self.tiempo.run()
        self.actualizar_estadisticas()
    
    def actualizar_estadisticas(self):
        reputacion = self.DCCafe.puntos_reputacion
        dinero = self.DCCafe.dinero_total
        ronda = self.DCCafe.ronda
        atendidos =  self.DCCafe.pedidos_exitosos
        perdidos = self.DCCafe.pedidos_perdidos
        proximos = self.DCCafe.clientes_ronda() - self.DCCafe.pedidos_totales
        self.estadisticas = [reputacion, dinero, ronda, atendidos, perdidos, proximos]
        
        self.senal_actualizar_estadisticas_vp.emit(self.estadisticas)

    def guardar_juego(self):
        print(self.DCCafe.empleados[0].pos())
        x = open(p.RUTA_MAPA_CSV, "w", encoding="utf-8")
        y = open(p.RUTA_DATOS, "w", encoding="utf-8")
        for objeto in self.mapa:
            if objeto[0] == "mesero":
                a = [objeto[0], self.DCCafe.empleados[0].pos().x(), self.DCCafe.empleados[0].pos().y()]
                print(*a, sep = "," , file = x)
            else:
                a = [objeto[0],objeto[1][0],objeto[2][0]]
                print(*a, sep = "," , file = x)
        datos_dccafe = [self.DCCafe.dinero_total,self.DCCafe.puntos_reputacion, self.DCCafe.ronda]
        datos_chef = []
        for chef in self.DCCafe.empleados[1::]:
            datos_chef.append(chef.platos_preparados)
        datos = [datos_dccafe,datos_chef]
        for linea in datos:
            print(*linea, sep = "," , file = y)
        x.close()
        y.close()
        



        



        
        
                

        







        
        
        
        




    



            

        