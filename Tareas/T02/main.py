import sys
from PyQt5.QtWidgets import QApplication
import p
from ventana_principal import VentanaPrincipal, MisSenales
from ventana_inicio import VentanaInicio
from back_end import Logica, SenalesBackEnd
from entidades import Bocadillo, DCCafe
from ventana_post_ronda import VentanaPostRonda

if __name__ == "__main__":
    
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    
    a = QApplication(sys.argv)
    s_back_end = SenalesBackEnd()
    back_end = Logica(s_back_end.senal_actualizar_estadisticas, s_back_end.senal_terminar_juego)
    
    ventana_inicio = VentanaInicio()
    ventana_post_ronda = VentanaPostRonda()

    ventana_inicio.senal_cargar_mapa.connect(back_end.cargar_juego)
    ventana_inicio.senal_crear_partida.connect(back_end.juego_nuevo)
    senales_ventana_principal = MisSenales()
    ventana_principal = VentanaPrincipal()
    ventana_principal.recibir_señal(senales_ventana_principal.senal_crear_objeto)
    ventana_principal.senal_es_posible_poner_objeto.connect(back_end.revisar_vacio_tienda)
    ventana_principal.senal_cargar_entidades.connect(back_end.cargar_entidades)
    back_end.senal_mapa_cargado.connect(ventana_principal.cargar_juego)
    back_end.senal_bocadillo_creado.connect(ventana_principal.creacion_bocadillo)
    ventana_principal.senal_tecla_presionada.connect(back_end.mover_mesero)
    back_end.senal_movimiento_posible.connect(ventana_principal.mover_jugador)
    ventana_principal.senal_comenzar_juego.connect(back_end.jugar)
    back_end.senal_llegada_cliente.connect(ventana_principal.llegada_clientes)
    ventana_principal.senal_cliente_creado.connect(back_end.sentarse_clientes)
    ventana_principal.senal_agregar_bocadillo_mesa.connect(back_end.asociar_bocadillo_mesa)
    ventana_principal.senal_nueva_ronda.connect(back_end.nueva_ronda)
    back_end.senal_resultado_revisar.connect(ventana_principal.comprar_objeto_posible)
    back_end.senal_terminar_ronda.connect(ventana_post_ronda.datos)
    back_end.senal_actualizar_estadisticas_vp.connect(ventana_principal.actualizar_estadisticas)
    back_end.senal_terminar_ronda_ventana_principal.connect(ventana_principal.terminar_ronda)
    ventana_principal.senal_cargar_mesa.connect(back_end.cargar_elemento_comprado)
    ventana_principal.senal_cargar_cocina.connect(back_end.cargar_elemento_comprado)
    ventana_principal.senal_aumentar_dinero.connect(back_end.aumentar_dinero)
    ventana_principal.senal_aumentar_reputacion.connect(back_end.aumentar_reputacion)
    ventana_principal.senal_forzar_terminar_ronda.connect(back_end.forzar_terminar_ronda)
    ventana_principal.senal_eliminar_mesa.connect(back_end.eliminar_mesa)
    ventana_principal.senal_parar_juego.connect(back_end.pausa)
    ventana_post_ronda.senal_guardar_juego.connect(back_end.guardar_juego)
    ventana_post_ronda.senal_cerrar_juego.connect(ventana_principal.cerrar_juego)
    

    

    ventana_inicio.show()
    sys.exit(a.exec())
