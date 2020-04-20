from random import randint, choice 
import p 
import Tarea1
import Tarea1c
def crear_magizoologo_docencio(nombre):
    alim = choice([Tarea1c.TartaDeMelaza(), Tarea1c.HigadoDeDragon(), Tarea1c.BuñueloDeGusarajo()])
    n_magico = randint(p.DOCENCIO_NUMERO_MAGICO_MIN, p.DOCENCIO_NUMERO_MAGICO_MAX)
    dest = randint(p.DOCENCIO_DESTREZA_MIN, p.DOCENCIO_DESTREZA_MAX)
    e_total = randint(p.DOCENCIO_ENERGIA_MIN, p.DOCENCIO_ENERGIA_MAX)
    respons = randint(p.DOCENCIO_RESPONSABILIDAD_MIN, p.DOCENCIO_RESPONSABILIDAD_MAX)

    return Tarea1.MagizoologoDocencio(nombre, "Docencio", [], [alim], p.SICKLES_INICIALES, \
        p.LICENCIA, n_magico, dest, e_total, respons, p.HABILIDAD_ESPECIAL_USADA)

def crear_magizoologo_tareo(nombre):
    alim = choice([Tarea1c.TartaDeMelaza(), Tarea1c.HigadoDeDragon(), Tarea1c.BuñueloDeGusarajo()])
    n_magico = randint(p.TAREO_NUMERO_MAGICO_MIN, p.TAREO_NUMERO_MAGICO_MAX)
    dest = randint(p.TAREO_DESTREZA_MIN, p.TAREO_DESTREZA_MAX)
    e_total = randint(p.TAREO_ENERGIA_MIN, p.TAREO_ENERGIA_MAX)
    respons = randint(p.TAREO_RESPONSABILIDAD_MIN, p.TAREO_RESPONSABILIDAD_MAX)

    return Tarea1.MagizoologoTareo(nombre, "Tareo", [], [alim], p.SICKLES_INICIALES, \
        p.LICENCIA, n_magico, dest, e_total, respons, p.HABILIDAD_ESPECIAL_USADA)

def crear_magizoologo_hibrido(nombre):
    alim = choice([Tarea1c.TartaDeMelaza(), Tarea1c.HigadoDeDragon(), Tarea1c.BuñueloDeGusarajo()])
    n_magico = randint(p.HIBRIDO_NUMERO_MAGICO_MIN, p.HIBRIDO_NUMERO_MAGICO_MAX)
    dest = randint(p.HIBRIDO_DESTREZA_MIN, p.HIBRIDO_DESTREZA_MAX)
    e_total = randint(p.HIBRIDO_ENERGIA_MIN, p.HIBRIDO_ENERGIA_MAX)
    respons = randint(p.HIBRIDO_RESPONSABILIDAD_MIN, p.HIBRIDO_RESPONSABILIDAD_MAX)

    return Tarea1.MagizoologoHibrido(nombre, "Hibrido", [], [alim], p.SICKLES_INICIALES, \
         p.LICENCIA, n_magico, dest, e_total, respons, p.HABILIDAD_ESPECIAL_USADA)
def crear_augurey(nombre):
    nivel_magico = randint(p.AUGUREY_NIVEL_MAGICO_MIN, p.AUGUREY_NIVEL_MAGICO_MAX)
    prob_esc = p.AUGUREY_PROB_ESCAPAR
    prob_enfer =  p.AUGUREY_PROB_ENFERMAR
    salud  = randint(p.AUGUREY_SALUD_MIN, p.AUGUREY_SALUD_MAX)
    agres = p.AGRESIVIDAD_AUGUREY
    criatura = Tarea1.Augurey(nombre, "Augurey", nivel_magico, salud, salud, prob_esc, prob_enfer,\
         p.ESTADO_SALUD, p.NIVEL_HAMBRE, p.SIN_COMER, agres, p.NIVEL_CLEPTO_A_H, p.CRIATURA_ESCAPO)
    return criatura

def crear_niffler(nombre):
    nivel_magico = randint(p.NIFFLER_NIVEL_MAGICO_MIN, p.NIFFLER_NIVEL_MAGICO_MAX)
    prob_esc = p.NIFFLER_PROB_ESCAPAR
    prob_enfer =  p.NIFFLER_PROB_ENFERMAR
    salud  = randint(p.NIFFLER_SALUD_MIN, p.NIFFLER_SALUD_MAX)
    agres = p.AGRESIVIDAD_NIFFLER
    cleptomania = randint(p.NIFFLER_CLEPTOMANIA_MIN, p.NIFFLER_CLEPTOMANIA_MAX)
    criatura = Tarea1.Niffler(nombre, "Niffler", nivel_magico, salud, salud, prob_esc, prob_enfer,\
         p.ESTADO_SALUD, p.NIVEL_HAMBRE, p.SIN_COMER, agres, cleptomania, p.CRIATURA_ESCAPO)
    return criatura


def crear_erkling(nombre):
    nivel_magico = randint(p.ERKLING_NIVEL_MAGICO_MIN, p.ERKLING_NIVEL_MAGICO_MAX)
    prob_esc = p.ERKLING_PROB_ESCAPAR
    prob_enfer = p.ERKLING_PROB_ENFERMAR
    salud  = randint(p.ERKLING_SALUD_MIN, p.ERKLING_SALUD_MAX)
    agres = p.AGRESIVIDAD_ERKLING
    criatura = Tarea1.Erkling(nombre, "Erkling", nivel_magico, salud, salud, prob_esc, prob_enfer,\
         p.ESTADO_SALUD, p.NIVEL_HAMBRE, p.SIN_COMER, agres, p.NIVEL_CLEPTO_A_H, p.CRIATURA_ESCAPO)
    return criatura