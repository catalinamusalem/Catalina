

def verificar_rut(rut, datos_registrados):
    if "." in rut or "-" not in rut:
        # Levanta el error correspondiente
        raise ValueError("RUT viene con puntos o sin guión")
        

    if rut in datos_registrados.keys():
        return datos_registrados[rut]
    return

def permiso_clave_unica(rut, datos_registrados):
    if rut not in datos_registrados.keys():
        # Levanta el error correspondiente
         raise KeyError("No puedes solicitar clave única. Impostor!")


def permiso_asistencia_medica(hora):
    if not hora.isdigit():
        # Levanta el error correspondiente
        raise TypeError("El formato de la hora es incorrecto")
       


def permiso_servicios_basicos(persona, solicitud, comunas_cuarentena):

    if ((solicitud.salida not in comunas_cuarentena) and
        (solicitud.llegada not in comunas_cuarentena)):
        # Levanta el error correspondiente
        raise ValueError("La comuna no esta en cuarentena")

    elif solicitud.salida != persona.domicilio:
        # Levanta el error correspondiente
        raise ValueError("No esta saliendo desde su domicilio")


