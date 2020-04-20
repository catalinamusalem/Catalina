from abc import ABC, abstractmethod
from random import randint, choice, random
import p
import Tarea1
import crear
import Tarea1c
def abrir_archivos():
    with open(p.PATH_CRIATURAS, 'rt', encoding="utf-8") as archivo:
        lineas_criaturas = archivo.readlines()
    with open(p.PATH_MAGIZOOLOGOS, 'rt', encoding="utf-8") as archivo:
        lineas_magizoologos = archivo.readlines()
    criaturas = []
    magizoologos = []
    for i in lineas_criaturas:
        a = i.split(",")
        if a[1] == "Niffler":
            b = Tarea1.Niffler(a[0], a[1], a[2], a[7], a[8], a[3], a[4], a[5], a[9], a[11], a[10],\
                 a[12], a[6])
        if a[1] == "Erkling":
            b = Tarea1.Erkling(a[0], a[1], a[2], a[7], a[8], a[3], a[4], a[5], a[9], a[11], a[10],\
                 a[12], a[6])
        if a[1] == "Augurey":
            b = Tarea1.Augurey(a[0], a[1], a[2], a[7], a[8], a[3], a[4], a[5], a[9], a[11], a[10],\
                 a[12], a[6])
        criaturas.append(b)

    for i in lineas_magizoologos:
        a = i.split(",")
        c = a[3].split(";")
        criaturas_como_clase = []
        d = a[4].split(";")
        alimentos_como_clase = []
        for j in d:
            if j == "Tarta de Melaza":
                alimentos_como_clase.append(Tarea1c.TartaDeMelaza())
            elif j == "Buñuelo de Gusarajo":
                alimentos_como_clase.append(Tarea1c.BuñueloDeGusarajo())
            else:
                alimentos_como_clase.append(Tarea1c.HigadoDeDragon())

        for j in criaturas:
            for k in c:
                if j.nombre == k:
                    criaturas_como_clase.append(j)
        a[3] = criaturas_como_clase
        a[4] = alimentos_como_clase
        if a[1] == "Docencio":
            b = Tarea1.MagizoologoDocencio(a[0], a[1], a[3], a[4], a[2], a[5], a[6], a[7], a[8],\
                 a[9], a[10])
        if a[1] == "Tareo":
            b = Tarea1.MagizoologoTareo(a[0], a[1], a[3], a[4], a[2], a[5], a[6], a[7], a[8],\
                 a[9], a[10])
        if a[1] == "Híbrido":
            b = Tarea1.MagizoologoHibrido(a[0], a[1], a[3], a[4], a[2], a[5], a[6], a[7], a[8],\
                 a[9], a[10])
        magizoologos.append(b)
    return [criaturas, magizoologos]

def escribir_archivos(path_magizoologos, path_criaturas, criaturas, magizoologos):
    x = open(path_magizoologos, "w", encoding="utf-8")
    y = open(path_criaturas, "w", encoding="utf-8")
    for mago in magizoologos:
        criaturas = []
        alimentos = []
        
        for criatura in mago.criaturas:
            criaturas.append(criatura.nombre)
        for alimento in mago.alimentos:
            alimentos.append(alimento.nombre)

        c = ";".join(criaturas)
        d = ";".join(alimentos)
        a = [mago.nombre, mago.tipo, mago.sickles, c, d, mago.licencia, mago.nivel_magico,\
             mago.destreza, mago.energia_total, mago.responsabilidad, \
            mago.habilidad_especial_usada]
        print(*a, sep = "," , file = x)
        for criatura in mago.criaturas:
            b = [criatura.nombre, criatura.tipo, criatura.nivel_magico, criatura.prob_escape,\
                 criatura.prob_enfermar, criatura.estado_salud, criatura.estado_escape, \
                     criatura.salud_total, criatura.salud_actual, criatura.nivel_hambre, \
                         criatura.nivel_agresividad, criatura.sin_comer,criatura.nivel_cleptomania]
            print(*b, sep = "," , file = y)
    x.close()
    y.close()

def menus(path_magizoologos, path_criaturas, criaturas, magizoologos):
    j = 0
    while j == 0:
        print("                                      ")
        print("*********** MENÚ DE INICIO ***********") 
        print("                                      ")   
        print("Bienvenid@ a DCCRIATURAS FANTÁSTICAS!!")
        print("Seleccione una opción:")
        print("[1] Crear Magizoólogo")
        print("[2] Cargar Magizoólogo")
        print("[3] Salir")
        opcion_menu_inicio = input("Indique su opción (1,2 o 3): ")
        if opcion_menu_inicio == "1" or opcion_menu_inicio == "2":
            nombre_de_usuario = input("Ingrese nombre de usuario: ")
            existe_mago = 0
            if nombre_de_usuario.isalnum() == False or len(nombre_de_usuario) == 0:
                opcion_menu_inicio = 4 #para hacer que no entre en los if siguientes
                print("El nombre de usuario solo debe incluir caractéres alfanumericos y debe \
tener a lo menos un caracter")
            for magico in magizoologos:
                if nombre_de_usuario.lower() == magico.nombre.lower():
                    existe_mago += 1
            if existe_mago == 1 and opcion_menu_inicio == "1":
                print("El nombre de usuario ingresado ya existe, intente con otro")
            if existe_mago == 0 and opcion_menu_inicio == "1":
                
                print("Bienvenid@ " + nombre_de_usuario)
                print("Seleccione el tipo de magizoólogo que quiere ser")
                print("[1] Docencio")
                print("[2] Tareo")
                print("[3] Híbrido")
                tipo_de_magizoologo = input("Indique su opción (1,2 o 3): ")
                if tipo_de_magizoologo == "1":
                    mago = crear.crear_magizoologo_docencio(nombre_de_usuario)
                    magizoologos.append(mago)
                elif tipo_de_magizoologo == "2":
                    mago = crear.crear_magizoologo_tareo(nombre_de_usuario)
                    magizoologos.append(mago)
                else:
                    mago = crear.crear_magizoologo_hibrido(nombre_de_usuario)
                    magizoologos.append(mago)
                print("Seleccione la criatura que quiere adoptar")
                print("[1] Niffler")
                print("[2] Erkling")
                print("[3] Augurey")
                adoptar_criatura = input("Indique su opción (1,2 o 3): ")
                existe_criatura = 1
                while existe_criatura == 1:
                    existe_criatura = 0
                    nombre_criatura = input("ingrese el nombre de la criatura ")
                    for criatura in criaturas:
                        if nombre_criatura.lower() == criatura.nombre.lower():
                            print("El nombre de criatura ingresado ya existe, intente con otro")
                            existe_criatura += 1
                if existe_criatura == 0:
                    if adoptar_criatura == "1":
                        criatura_creada = crear.crear_niffler(nombre_criatura)
                    elif adoptar_criatura == "2":
                        criatura_creada = crear.crear_erkling(nombre_criatura)
                    else:
                        criatura_creada = crear.crear_augurey(nombre_criatura)
                    mago.criaturas.append(criatura_creada)
                    criaturas.append(criatura_creada)
                j += 1
            escribir_archivos(p.PATH_MAGIZOOLOGOS, p.PATH_CRIATURAS, criaturas, magizoologos) 
            if existe_mago == 1 and opcion_menu_inicio == "2":
                for magico in magizoologos:
                    if nombre_de_usuario.lower() == magico.nombre.lower():
                        mago = magico
                print("Bienvenid@ " + mago.nombre)    
                
                j += 1
                
            if existe_mago == 0 and opcion_menu_inicio == "2":
                print("El usuario ingresado no se encuentra registrado, intente de nuevo")
            
        if opcion_menu_inicio == "3":
            escribir_archivos(p.PATH_MAGIZOOLOGOS, p.PATH_CRIATURAS, criaturas, magizoologos)
            break

        while j == 1:
            print("                                  ")   
            print("******** MENÚ DE ACCIONES ********") 
            print("                                  ")   
            print("Seleccione una opción:")
            print("[1] Menú cuidar DCCriaturas")
            print("[2] Menú DCC")
            print("[3] Pasar al día siguiente")
            print("[4] Volver atrás")
            print("[5] Salir")
            opcion_menu_acciones = input("Indique su opción (1,2,3,4 o 5): ")
            if opcion_menu_acciones == "1":
                j += 1
                while j == 2:
                    print("                                  ")   
                    print("***** MENÚ CUIDAR DCCRIATURAS *****") 
                    print("                                  ")  
                    print("Seleccione una opción:")
                    print("[1] Alimentar DCCriaturas")
                    print("[2] Recuperar DCCriaturas")
                    print("[3] Sanar DCCriaturas")
                    print("[4] Usar habilidad especial")
                    print("[5] Volver atrás")
                    print("[6] Salir")
                    opcion_menu_cuidar = input("Indique su opción (1,2,3,4,5 o 6): ")
                    if opcion_menu_cuidar == "1":
                        i = 1
                        criaturas_enjauladas = []
                        for criatura in mago.criaturas:
                            if criatura.estado_escape == "False":
                                criaturas_enjauladas.append(criatura)
                        if len(criaturas_enjauladas) == 0:
                            print("No tienes criaturas que alimentar")
                        elif len(mago.alimentos) == 0:
                            print("No tienes alimentos para tus criaturas")
                        else:
                            print("Seleccione la criatura que quiere alimentar")
                            for criatura in criaturas_enjauladas:
                                print("[" + str(i) + "] " + criatura.nombre)
                                i += 1
                            opcion_criatura = input("Indique el número de su opción: ")
                            if opcion_criatura.isdigit() == False or \
                                len(criaturas_enjauladas) < int(opcion_criatura):
                                opcion_criatura == "1"
                            i = 1
                            for alimento in mago.alimentos:
                                print("[" + str(i) + "] " + alimento.nombre)
                                i += 1
                            opcion_alimento = input("Indique el número de su opción: ")
                            if opcion_alimento.isdigit() == False or \
                                len(mago.alimentos) < int(opcion_alimento):
                                opcion_alimento == "1"
                            mago.alimentar(criaturas_enjauladas[int(opcion_criatura)-1], \
                                mago.alimentos[int(opcion_alimento)-1])
                    if opcion_menu_cuidar == "2":
                        i = 1
                        criaturas_escapadas = []
                        print("Seleccione la criatura que quiere recuperar")
                        for criatura in mago.criaturas:
                            if criatura.estado_escape == "True":
                                print("[" + str(i) + "] " + criatura.nombre)
                                criaturas_escapadas.append(criatura)
                                i += 1
                        if len(criaturas_escapadas) == 0:
                            print("No tiene criaturas que recuperar")
                        else:
                            opcion_criatura = input("Indique el número de su opción: ")
                            if opcion_criatura.isdigit() == False:
                                opcion_criatura = "1"
                            mago.recuperar_criatura(criaturas_escapadas[int(opcion_criatura)-1])
                    if opcion_menu_cuidar == "3":
                        i = 1
                        criaturas_enfermas = []
                        print("Seleccione la criatura que quiere sanar")
                        for criatura in mago.criaturas:
                            if criatura.estado_salud == "True":
                                print("[" + str(i) + "] " + criatura.nombre)
                                criaturas_enfermas.append(criatura)
                                i += 1
                        if len(criaturas_enfermas) == 0:
                            print("No tiene criaturas que sanar")
                        else:
                            opcion_criatura = input("Indique el número de su opción: ")
                            if opcion_criatura.isdigit() == False or int(opcion_criatura) > len(criaturas_enfermas):
                                opcion_criatura = "1"
                            mago.sanar_criatura(criaturas_enfermas[int(opcion_criatura)-1])
                    if opcion_menu_cuidar == "4":
                        mago.habilidad_especial()
                    if opcion_menu_cuidar == "5":
                        j = 1
                    if opcion_menu_cuidar == "6":
                        z = p.PATH_MAGIZOOLOGOS
                        escribir_archivos(z, p.PATH_CRIATURAS, criaturas, magizoologos)
                        break
                escribir_archivos(p.PATH_MAGIZOOLOGOS, p.PATH_CRIATURAS, criaturas, magizoologos)  
            if opcion_menu_acciones == "2":
                j = 3
                while j == 3:
                    print("                                  ")   
                    print("********* MENÚ DCC **********") 
                    print("                                  ")  
                    print("Seleccione una opción:")
                    print("[1] Adoptar DCCriatura")
                    print("[2] Comprar alimentos")
                    print("[3] Ver estado Magizoólogos y DCCriaturas")
                    print("[4] Volver atrás")
                    print("[5] Salir")
                    opcion_menu_dcc = input("Indique su opción (1,2,3,4 o 5): ")
                    usuario_dcc = Tarea1.DCC(mago)
                    if opcion_menu_dcc == "1":
                        print("Seleccione la DCCriatura que quiere adoptar")
                        print("[1] Augurey --> $" + str(p.PRECIO_AUGUREY))
                        print("[2] Niffler --> $" + str(p.PRECIO_NIFFLER))
                        print("[3] Erkling --> $" + str(p.PRECIO_ERKLING))
                        opcion_criatura = input("Indique su opcion (1,2 o 3): ")
                        existe_criatura = 1
                        while existe_criatura == 1:
                            existe_criatura = 0
                            nombre_criatura = input("ingrese el nombre de la criatura ")
                            for criatura in criaturas:
                                if nombre_criatura.lower() == criatura.nombre.lower():
                                    print("El nombre ingresado ya existe, intente con otro")
                                    existe_criatura += 1
                        if existe_criatura == 0:
                            if opcion_criatura == "1":
                                usuario_dcc.vender_criatura("augurey", nombre_criatura)
                                criaturas.append(mago.criaturas[-1])
                            elif opcion_criatura == "2":
                                usuario_dcc.vender_criatura("niffler", nombre_criatura)
                                criaturas.append(mago.criaturas[-1])
                            elif opcion_criatura == "3":
                                usuario_dcc.vender_criatura("erkling", nombre_criatura)
                                criaturas.append(mago.criaturas[-1])
                            else:
                                print("La opcion ingresada no es válida")
                            l = p.PATH_MAGIZOOLOGOS
                            escribir_archivos(l, p.PATH_CRIATURAS, criaturas, magizoologos)
                    if opcion_menu_dcc == "2":
                        print("Seleccione el alimento que quiere comprar")
                        print("[1] Tarta de Melaza --> $" + str(p.PRECIO_TARTA))
                        print("[2] Buñuelos de Gusarajo --> $" + str(p.PRECIO_BUÑUELOS))
                        print("[3] Hígado de Dragón --> $" + str(p.PRECIO_HIGADO))
                        opcion_alimento = input("Indique su opcion (1,2 o 3): ")
                        if opcion_alimento == "1":
                            usuario_dcc.vender_alimentos("tarta de melaza")
                        elif opcion_alimento == "2":
                            usuario_dcc.vender_alimentos("buñuelos de gusarajo")
                        elif opcion_alimento == "3":
                            usuario_dcc.vender_alimentos("Hígado de Dragón")
                        else:
                            print("La opcion ingresada no es válida")
                        l = p.PATH_MAGIZOOLOGOS
                        escribir_archivos(l, p.PATH_CRIATURAS, criaturas, magizoologos)
                    
                    if opcion_menu_dcc == "3":
                        print(f"Nombre: {mago.nombre}\nSickles: {mago.sickles}")
                        print(f"Energía actual:{mago.energia_actual}\nLicencia: {mago.licencia}") 
                        print(f"Nivel de aprobación: {mago.nivel_de_aprobacion}")
                        print(f"Nivel mágico: {mago.nivel_magico}\nDestreza: {mago.destreza}")
                        print(f"Responsabilidad: {mago.responsabilidad}\nAlimentos: ")
                        for alim in mago.alimentos:
                            print(alim.nombre + "--> Efecto salud: " + str(alim.efecto_salud))
                        print("Estado DCCriaturas")
                        for criatura in mago.criaturas:
                            print(f"Nombre: {criatura.nombre}")
                            print(f"Nivel mágico: {criatura.nivel_magico}")
                            print(f"Puntos de salud actual: {criatura.salud_actual}")
                            print(f"Estado de salud: {criatura.estado_salud}")
                            print(f"Nivel de hambre: {criatura.nivel_hambre}")
                            print(f"Nivel de agresividad: {criatura.nivel_agresividad}" )
                    if opcion_menu_dcc == "4":
                        j = 1   
                    if opcion_menu_dcc == "5":
                        l = p.PATH_MAGIZOOLOGOS
                        escribir_archivos(l, p.PATH_CRIATURAS, criaturas, magizoologos)
                        break
                
            if opcion_menu_acciones == "3":
                print("¡¡Has pasado al día siguiente!! \n***************************************")
                usuario_dcc = Tarea1.DCC(mago)
                usuario_dcc.fiscalizar_magizoologos()
                print("*************************************") 
                usuario_dcc.nivel_de_aprobacion()
                for multa in usuario_dcc.multas:
                    print(multa[0])
                usuario_dcc.pagar_magizoologos()
            if opcion_menu_acciones == "4":
                j = 0
            if opcion_menu_acciones == "5":
                escribir_archivos(p.PATH_MAGIZOOLOGOS, p.PATH_CRIATURAS, criaturas, magizoologos)
                break
            escribir_archivos(p.PATH_MAGIZOOLOGOS, p.PATH_CRIATURAS, criaturas, magizoologos)
    
menus(p.PATH_MAGIZOOLOGOS, p.PATH_CRIATURAS, abrir_archivos()[0], abrir_archivos()[1])





