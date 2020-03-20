import datetime
seguidores=[]
usuarios=[]
posts=[]
x=open("seguidores.csv", "r+")
y=open("usuarios.csv", "r+")
z=open("posts.csv", "r", encoding="utf-8")
lineasx =x.readlines()
lineasy =y.readlines()
lineasz =z.readlines()
for linea in lineasx:
    limpiar=linea.strip()
    lista=limpiar.split(",")
    seguidores.append(lista)
for linea in lineasy:
    limpiar=linea.strip()
    usuarios.append(limpiar)
for linea in lineasz:
    limpiar=linea.strip()
    lista=limpiar.split(",",2)
    posts.append(lista)
x.close()
y.close()
z.close()
j=1
nombredeusuario="a"
registrarusuario="b"
while j==1:
    print("Bienvenido a DCCahuin!!")
    print("Seleccione una opción")
    print("[1] Iniciar sesión")
    print("[2] Registrar usuario")
    print("[0] Salir")
    opcion=input("Indique su opción (0,1 o 2) ")
    opcion1=1
    if opcion=="1":
        nombre_de_usuario=input("Ingrese nombre de usuario: ")
        for i in usuarios:
            if nombre_de_usuario==i:
                print("Bienvenido " + nombre_de_usuario)
                j+=1
                y=open("usuarios.csv","w")
                for usua in usuarios:
                    print(usua,file=y)
                y.close()
                x=open("seguidores.csv", "w")
                for seg in seguidores:
                    print(*seg, sep = "," , file=x)
                x.close()
                while j==2:
                    print("Seleccione una opción")
                    print("[1] Menu de prograpost")
                    print("[2] Menu de seguidores")
                    print("[0] Salir")
                    opcion1=input("Indique su opción (0,1 o 2) ")
                    if opcion1=="1":
                        j+=1
                        while j==3:
                            print("Seleccione una opción")
                            print("[1] Crear un prograpost")
                            print("[2] Eliminar un prograpost")
                            print("[3] Ver prograposts creados por el usuario")
                            print("[4] Ver prograposts de los usuarios seguidos")
                            print("[5] Volver al menu de inicio")
                            opcion2=input("Indique su opción (0,1,2,3,4 o 5) ")
                            j+=1
                            while j==4:
                                if opcion2=="1":
                                    crear=input("Escriba el prograpost ")
                                    fech=datetime.date.today()
                                    fecha=fech.strftime('%Y/%m/%d')
                                    if len(crear)>140:
                                        print("El prograpost excede la cantidad máxima de caractéres")
                                        j-=1
                                    if len(crear)==0:
                                        print("No puedes crear un prograpost sin caractéres")
                                        j-=1
                                    if len(crear)!=0 and len(crear)<141:
                                        j-=1
                                        posts.append([nombre_de_usuario, fecha, crear])
                                        print("Prograpost creado!")
                                    z=open("posts.csv", "w", encoding="utf-8")  
                                    for pos in posts:
                                        print(str(pos[0]) + "," + str(pos[1]) + "," + str(pos[2]), file=z)
                                    z.close()
                                if opcion2=="2":
                                    eliminar=input("Escriba prograpost a eliminar ")
                                    fecha_eliminar=input\
                                                    ("Escriba fecha del prograpost a eliminar (yy/mm/dd) ")
                                    for i in posts:
                                        if str(i[0])==str(nombre_de_usuario) and \
                                           str(i[1])==str(fecha_eliminar) and str(i[2]==eliminar):
                                            posts.pop(posts.index(i))
                                            print("Prograpost eliminado")
                                            j-=1
                                    if j==4:
                                        print("No ha sido posible eliminarlo, intente de nuevo")
                                        j-=1
                                    z=open("posts.csv", "w", encoding="utf-8")  
                                    for pos in posts:
                                        print(str(pos[0]) + "," + str(pos[1]) + "," + str(pos[2]),\
                                              file=z)
                                    z.close()
                                if opcion2=="3":
                                    print("En que orden cronologico desea ver los prograpost")
                                    print("[1] Ascendente")
                                    print("[2] Descendente")
                                    orden=input("Indique su opción (1 o 2)")
                                    posts_propios=[]
                                    dates=[]
                                    posts_ordenados=[]
                                    for i in posts:
                                        if i[0]==nombre_de_usuario:
                                            posts_propios.append(i)
                                    for i in posts_propios:
                                        i[1]=i[1].split("/")
                                        i[1]=datetime.date(int(i[1][0]), int(i[1][1]), int(i[1][2]))
                                        dates.append(i[1])
                                    dates.sort()
                                    for i in dates:
                                        for v in posts_propios:
                                            if i==v[1]:
                                               v[1]=i.strftime('%Y/%m/%d')
                                               posts_ordenados.append(v)
                                    if orden=="1":
                                        for post in posts_ordenados:
                                            print(post)
                                    if orden=="2":
                                        for post in posts_ordenados[::-1]:
                                            print(post)
                                    j-=1
                                if opcion2=="4":
                                    print("En que orden cronologico desea ver los prograpost")
                                    print("[1] Ascendente")
                                    print("[2] Descendente")
                                    orden=input("Indique su opción (1 o 2)")
                                    post_seguidos=[]
                                    dates=[]
                                    posts_ordenados=[]
                                    for i in seguidores:
                                        if i[0]==nombre_de_usuario:
                                            for l in posts:
                                                for k in i[1:]:
                                                    if l[0]==k:
                                                        post_seguidos.append(l)
                                    for i in post_seguidos:
                                        i[1]=i[1].split("/")
                                        i[1]=datetime.date(int(i[1][0]), int(i[1][1]), int(i[1][2]))
                                        dates.append(i[1])
                                    dates.sort()
                                    for i in dates:
                                        for v in post_seguidos:
                                            if i==v[1]:
                                               v[1]=i.strftime('%Y/%m/%d')
                                               posts_ordenados.append(v)
                                    if orden=="1":
                                        for post in posts_ordenados:
                                            print(post)
                                    if orden=="2":
                                        for post in posts_ordenados[::-1]:
                                            print(post)
                                    j-=1
                                if opcion2=="5":
                                    j-=2
                                else:
                                    j=3   
                    if opcion1=="2":
                        j+=1
                        while j==3:
                            contador1=0
                            print("Seleccione una opción")
                            print("[1] Seguir a un usuario")
                            print("[2] Dejar de seguir a un usuario")
                            print("[3] Volver al menú anterior")
                            opcion3=input("Indique su opción (1,2 o 3) ")
                            if opcion3=="1":
                                seguir_usuario=input("Ingrese usuario a seguir ")
                                cantidad=usuarios.count(seguir_usuario)
                                if cantidad==0:
                                    print("No es posible seguir aquel usuario ya que no existe")
                                    contador1+=1
                                if seguir_usuario==nombre_de_usuario:
                                    contador1+=1
                                    print("No es posible seguirse a usted mismo")
                                for i in seguidores:
                                    if i[0]==nombre_de_usuario:
                                        if len(i)==1:
                                            print("hola")
                                            i.append(seguir_usuario)
                                            print("Usuario seguido exitosamente!")
                                            break
                                        for je in i[1:]:
                                            if je==seguir_usuario:
                                                contador1+=1
                                                print("usted ya sigue a este usuario")
                                        if contador1==0:
                                            i.append(seguir_usuario)
                                            print("Usuario seguido exitosamente!")
                                            break
                                x=open("seguidores.csv", "w")
                                for seg in seguidores:
                                    print(*seg, sep = "," , file=x)
                                x.close()
                            if opcion3=="2":
                                dejar_de_seguir=input("Ingrese usario al que quiere dejar de seguir")
                                contador_2=0
                                for i in seguidores:
                                    if i[0]==nombre_de_usuario:
                                        for ji in i[1:]:
                                            if ji==dejar_de_seguir:
                                                contador_2+=1
                                                i.remove(ji)
                                                print("Se a dejado de seguir a el usuario")
                                        if contador_2==0:
                                            print("Usted no sigue a el usuario o no existe")
                                x=open("seguidores.csv","w")
                                for seg in seguidores:
                                    print(*seg, sep = "," , file=x)
                                x.close()
                            if opcion3=="3":
                                j-=1
                    if opcion1=="0":
                        j=1
        if j==1 and opcion1!="0":
            print("Aquel usuario no existe, intente de nuevo")                                                  
    if opcion=="2":
        registrar_usuario=input("Ingrese nombre de usuario: ")
        k=0
        for i in usuarios:
            if registrar_usuario==i or len(registrar_usuario)<8:
                k+=1
        if k!=0:
            print("El nombre de usuario ya esta registrado o tiene menos de 8 caracteres")
        if k==0:
            usuarios.append(registrar_usuario)
            lista=[registrar_usuario]
            seguidores.append(lista)
            print("Se ha registrado con exito!")
            j+=1
            y=open("usuarios.csv","w")
            for i in usuarios:
                print(i,file=y)
            y.close()
        while j==2:
            print("Seleccione una opción")
            print("[1] Menu de prograpost")
            print("[2] Menu de seguidores")
            print("[0] Salir")
            opcion1=input("Indique su opción (0,1 o 2) ")
            if opcion1=="1":
                j+=1
                while j==3:
                    print("Seleccione una opción")
                    print("[1] Crear un prograpost")
                    print("[2] Eliminar un prograpost")
                    print("[3] Ver prograposts creados por el usuario")
                    print("[4] Ver prograposts de los usuarios seguidos")
                    print("[5] Volver al menu de inicio")
                    opcion2=input("Indique su opción (0,1,2,3,4 o 5) ")
                    j+=1
                    while j==4:
                        if opcion2=="1":
                            crear=input("Escriba el prograpost ")
                            fech=datetime.date.today()
                            fecha=fech.strftime('%Y/%m/%d')
                            if len(crear)>140:
                                print("El prograpost excede la cantidad máxima de caractéres")
                                j-=1
                            if len(crear)==0:
                                print("No puede crear un prograpost sin caractéres")
                                j-=1
                            if len(crear)!=0 and len(crear)<141:
                                j-=1
                                posts.append([registrar_usuario, fecha, crear])
                                print("Prograpost creado!")
                            z=open("posts.csv","w",encoding="utf-8")  
                            for pos in posts:
                                print(str(pos[0]) + "," + str(pos[1]) + "," + str(pos[2]), file=z)
                            z.close()
                        if opcion2=="2":
                            eliminar=input("Escriba prograpost a eliminar ")
                            fecha_eliminar=input("Escriba fecha del prograpost a eliminar (yy/mm/dd) ")
                            for i in posts:
                                if str(i[0])==str(registrar_usuario) and \
                                   str(i[1])==str(fecha_eliminar) and str(i[2]==eliminar):
                                    posts.pop(posts.index(i))
                                    print("Prograpost eliminado")
                                    j-=1
                            if j==4:
                                print("No ha sido posible eliminarlo, intente de nuevo")
                                j-=1
                            z=open("posts.csv", "w", encoding="utf-8")  
                            for pos in posts:
                                print(str(pos[0]) + "," + str(pos[1]) + "," + str(pos[2]), file=z)
                            z.close()
                        if opcion2=="3":
                            print("En que orden cronologico desea ver los prograpost")
                            print("[1] Ascendente")
                            print("[2] Descendente")
                            orden=input("Indique su opción (1 o 2)")
                            posts_propios=[]
                            dates=[]
                            posts_ordenados=[]
                            for i in posts:
                                if i[0]==registrar_usuario:
                                    posts_propios.append(i)
                            for i in posts_propios:
                                i[1]=i[1].split("/")
                                i[1]=datetime.date(int(i[1][0]), int(i[1][1]), int(i[1][2]))
                                dates.append(i[1])
                            dates.sort()
                            for i in dates:
                                for v in posts_propios:
                                    if i==v[1]:
                                       v[1]=i.strftime('%Y/%m/%d')
                                       posts_ordenados.append(v)
                            if orden=="1":
                                for post in posts_ordenados:
                                    print(post)
                            if orden=="2":
                                for post in posts_ordenados[::-1]:
                                    print(post)
                            j-=1
                        if opcion2=="4":
                            print("En que orden cronologico desea ver los prograpost")
                            print("[1] Ascendente")
                            print("[2] Descendente")
                            orden=input("Indique su opción (1 o 2)")
                            post_seguidos=[]
                            dates=[]
                            posts_ordenados=[]
                            for i in seguidores:
                                if i[0]==registrar_usuario:
                                    if len(i)>1:
                                        for l in posts:
                                            for ñ in i[1:]:
                                                if l[0]==ñ:
                                                    post_seguidos.append(l)
                                    if len(i)==1:
                                        print("No hay publicaciones que mostrar")
                            for i in post_seguidos:
                                i[1]=i[1].split("/")
                                i[1]=datetime.date(int(i[1][0]), int(i[1][1]), int(i[1][2]))
                                dates.append(i[1])
                            dates.sort()
                            for i in dates:
                                for v in post_seguidos:
                                    if i==v[1]:
                                       v[1]=i.strftime('%Y/%m/%d')
                                       posts_ordenados.append(v)
                            if orden=="1":
                                for post in posts_ordenados:
                                    print(post)
                            if orden=="2":
                                for post in posts_ordenados[::-1]:
                                    print(post)
                            j-=1
                        if opcion2=="5":
                            j-=2
            if opcion1=="2":
                j+=1
                while j==3:
                    contador1=0
                    print("Seleccione una opción")
                    print("[1] Seguir a un usuario")
                    print("[2] Dejar de seguir a un usuario")
                    print("[3] Volver al menú anterior")
                    opcion3=input("Indique su opción (1,2 o 3) ")
                    if opcion3=="1":
                        seguir_usuario=input("Ingrese usuario a seguir ")
                        cantidad=usuarios.count(seguir_usuario)
                        if cantidad==0:
                            print("No es posible seguir aquel usuario ya que no existe")
                            contador1+=1
                        if seguir_usuario==registrar_usuario:
                            contador1+=1
                            print("No es posible seguirse a usted mismo")
                        for i in seguidores:
                            if i[0]==registrar_usuario:
                                if len(i)==1:
                                    i.append(seguir_usuario)
                                    print("Usuario seguido exitosamente!")
                                    break
                                for je in i[1:]:
                                    if je==seguir_usuario:
                                        contador1+=1
                                        print("usted ya sigue a este usuario")
                                if contador1==0:
                                    i.append(seguir_usuario)
                                    print("Usuario seguido exitosamente!")
                                    break
                        x=open("seguidores.csv", "w")
                        for seg in seguidores:
                            print(*seg, sep = "," ,file=x)
                        x.close()  
                    if opcion3=="2":
                        dejar_de_seguir=input("Ingrese usario al que quiere dejar de seguir")
                        contador_2=0
                        for i in seguidores:
                            if i[0]==registrar_usuario:
                                for jj in i[1:]:
                                    if jj==dejar_de_seguir:
                                        contador_2+=1
                                        i.remove(jj)
                                        print("Se a dejado de seguir a el usuario")
                                        break
                                if contador_2==0:
                                    print("Usted no sigue a el usuario o no existe")
                        x=open("seguidores.csv", "w")
                        for seg in seguidores:
                            print(*seg, sep = "," ,file=x)
                        x.close()
                    if opcion3=="3":
                        j-=1
            if opcion1=="0":
                j=1
    if opcion=="0":
        break
        
                                                                                                                        
                                    

