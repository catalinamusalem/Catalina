import datetime

seguidores=[]
usuarios=[]
posts=[]
x=open("seguidores.csv","r+")
y=open("usuarios.csv","r+")
z=open("posts.csv","r",encoding="utf-8")

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
        nombredeusuario=input("Ingrese nombre de usuario: ")
        for i in usuarios:
            if nombredeusuario==i:
                print("Bienvenido "+nombredeusuario)
                j+=1
                y=open("usuarios.csv","w")
                for usua in usuarios:
                    print(usua,file=y)
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
                                        print("No puedes crear un prograpost sin caractéres")
                                        j-=1
                                    if len(crear)!=0 and len(crear)<141:
                                        j-=1
                                        posts.append([nombredeusuario,fecha,crear])
                                        print("Prograpost creado!")
                                    z=open("posts.csv","w",encoding="utf-8")  
                                    for pos in posts:
                                        print(str(pos[0])+","+str(pos[1])+","+str(pos[2]),file=z)
                                    z.close()
                                if opcion2=="2":
                                    eliminar=input("Escriba prograpost a eliminar ")
                                    fechaeliminar=input("Escriba fecha del prograpost a eliminar (yy/mm/dd) ")
                                    for i in posts:
                                        
                                        if str(i[0])==str(nombredeusuario) and str(i[1])==str(fechaeliminar) and str(i[2]==eliminar):
                                            posts.pop(posts.index(i))
                                            print("Prograpost eliminado")
                                            j-=1
                                    if j==4:
                                        print("No ha sido posible eliminarlo, intente de nuevo")
                                        j-=1
                                    z=open("posts.csv","w",encoding="utf-8")  
                                    for pos in posts:
                                        print(str(pos[0])+","+str(pos[1])+","+str(pos[2]),file=z)
                                    z.close()
                                if opcion2=="3":
                                    print("En que orden cronologico desea ver los prograpost")
                                    print("[1] Ascendente")
                                    print("[2] Descendente")
                                    orden=input("Indique su opción (1 o 2)")
                                    postspropios=[]
                                    dates=[]
                                    postsordenados=[]
                                    for i in posts:
                                        if i[0]==nombredeusuario:
                                            postspropios.append(i)
                                    for i in postspropios:
                                        i[1]=i[1].split("/")
                                        i[1]=datetime.date(int(i[1][0]),int(i[1][1]),int(i[1][2]))
                                        dates.append(i[1])
                                    dates.sort()
                                    for i in dates:
                                        for v in postspropios:
                                            if i==v[1]:
                                               v[1]=i.strftime('%Y/%m/%d')#https://stackoverflow.com/questions/10624937/convert-datetime-object-to-a-string-of-date-only-in-python
                                               postsordenados.append(v)
                                    if orden=="1":
                                        for post in postsordenados:
                                            print(post)
                                    if orden=="2":
                                        for post in postsordenados[::-1]:
                                            print(post)
                                    j-=1
                                if opcion2=="4":
                                    print("En que orden cronologico desea ver los prograpost")
                                    print("[1] Ascendente")
                                    print("[2] Descendente")
                                    orden=input("Indique su opción (1 o 2)")
                                    postseguidos=[]
                                    dates=[]
                                    postsordenados=[]
                                    for i in seguidores:
                                        if i[0]==nombredeusuario:
                                            for l in posts:
                                                for k in i[1:]:
                                                    if l[0]==k:
                                                        postseguidos.append(l)
                                    for i in postseguidos:
                                        i[1]=i[1].split("/")
                                        i[1]=datetime.date(int(i[1][0]),int(i[1][1]),int(i[1][2]))
                                        dates.append(i[1])
                                    dates.sort()
                                    for i in dates:
                                        for v in postseguidos:
                                            if i==v[1]:
                                               v[1]=i.strftime('%Y/%m/%d')
                                               postsordenados.append(v)
                                    if orden=="1":
                                        for post in postsordenados:
                                            print(post)
                                    if orden=="2":
                                        for post in postsordenados[::-1]:
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
                                seguirusuario=input("Ingrese usuario a seguir ")
                                cantidad=usuarios.count(seguirusuario)
                                if cantidad==0:
                                    print("No es posible seguir aquel usuario ya que no existe")
                                    contador1+=1
                                if seguirusuario==nombredeusuario:
                                    contador1+=1
                                    print("No es posible seguirse a usted mismo")
                                    
                                for i in seguidores:
                                    if i[0]==nombredeusuario:
                                        if len(i)==1:
                                            i.append(seguirusuario)
                                            print("Usuario seguido exitosamente!")
                                            break
                                        for je in i[1:]:
                                            if je==seguirusuario:
                                                contador1+=1
                                                print("usted ya sigue a este usuario")
                                        if contador1==0:
                                            i.append(seguirusuario)
                                            print("Usuario seguido exitosamente!")
                                            break
                                x=open("seguidores.csv","w")
                                for seg in seguidores:
                                    print(*seg, sep = "," ,file=x)
                                x.close()
                            if opcion3=="2":
                                dejardeseguir=input("Ingrese usario al que quiere dejar de seguir")
                                for i in seguidores:
                                    if i[0]==nombredeusuario:
                                        for ji in i[1:]:
                                            if ji==dejardeseguir:
                                                i.remove(ji)
                                                print("Se a dejado de seguir a el usuario")
                                                
                                            else:
                                                print("Usted no sigue a el usuario o no existe")
                                x=open("seguidores.csv","w")
                                for seg in seguidores:
                                    print(*seg, sep = "," ,file=x)
                                x.close()
                            if opcion3=="3":
                                j-=1
          
                    if opcion1=="0":
                        j=1
        if j==1 and opcion1!="0":
            print("Aquel usuario no existe, intente de nuevo")##############################################################
                        
      
                                                   
    if opcion=="2":
        registrarusuario=input("Ingrese nombre de usuario: ")
        k=0
        
        for i in usuarios:
            if registrarusuario==i or len(registrarusuario)<8:
                k+=1
        if k!=0:
            print("El nombre de usuario ya esta registrado o tiene menos de 8 caracteres")
        if k==0:
            usuarios.append(registrarusuario)
            list=[registrarusuario]
            seguidores.append(list)
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
                                posts.append([registrarusuario,fecha,crear])
                                print("Prograpost creado!")
                            z=open("posts.csv","w",encoding="utf-8")  
                            for pos in posts:
                                print(str(pos[0])+ ","+ str(pos[1])+ ","+str(pos[2]),file=z)
                            z.close()
                        if opcion2=="2":
                            eliminar=input("Escriba prograpost a eliminar ")
                            fechaeliminar=input("Escriba fecha del prograpost a eliminar ")
                            for i in posts:
                                
                                if str(i[0])==str(registrarusuario) and str(i[1])==str(fechaeliminar) and str(i[2]==eliminar):
                                    posts.pop(posts.index(i))
                                    print("Prograpost eliminado")
                                    j-=1
                            if j==4:
                                print("No ha sido posible eliminarlo, intente de nuevo")
                                j-=1
                            z=open("posts.csv","w",encoding="utf-8")  
                            for pos in posts:
                                print(str(pos[0])+","+str(pos[1])+","+str(pos[2]),file=z)
                            z.close()
                        if opcion2=="3":
                            print("En que orden cronologico desea ver los prograpost")
                            print("[1] Ascendente")
                            print("[2] Descendente")
                            orden=input("Indique su opción (1 o 2)")
                            postspropios=[]
                            dates=[]
                            postsordenados=[]
                            for i in posts:
                                if i[0]==registrarusuario:
                                    postspropios.append(i)
                            for i in postspropios:
                                i[1]=i[1].split("/")
                                i[1]=datetime.date(int(i[1][0]),int(i[1][1]),int(i[1][2]))
                                dates.append(i[1])
                            dates.sort()
                            for i in dates:
                                for v in postspropios:
                                    if i==v[1]:
                                       v[1]=i.strftime('%Y/%m/%d')
                                       postsordenados.append(v)
                            if orden=="1":
                                for post in postsordenados:
                                    print(post)
                            if orden=="2":
                                for post in postsordenados[::-1]:
                                    print(post)
                            j-=1
                        if opcion2=="4":
                            print("En que orden cronologico desea ver los prograpost")
                            print("[1] Ascendente")
                            print("[2] Descendente")
                            orden=input("Indique su opción (1 o 2)")
                            postseguidos=[]
                            dates=[]
                            postsordenados=[]
                            for i in seguidores:
                                if i[0]==registrarusuario:
                                    if len(i)>1:
                                        for l in posts:
                                            for ñ in i[1:]:
                                                if l[0]==ñ:
                                                    postseguidos.append(l)
                                    if len(i)==1:
                                        print("No hay publicaciones que mostrar")
                            for i in postseguidos:
                                i[1]=i[1].split("/")
                                i[1]=datetime.date(int(i[1][0]),int(i[1][1]),int(i[1][2]))
                                dates.append(i[1])
                            dates.sort()
                            for i in dates:
                                for v in postseguidos:
                                    if i==v[1]:
                                       v[1]=i.strftime('%Y/%m/%d')
                                       postsordenados.append(v)
                            if orden=="1":
                                for post in postsordenados:
                                    print(post)
                            if orden=="2":
                                for post in postsordenados[::-1]:
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
                        seguirusuario=input("Ingrese usuario a seguir ")
                        cantidad=usuarios.count(seguirusuario)
                        if cantidad==0:
                            print("No es posible seguir aquel usuario ya que no existe")
                            contador1+=1
                        if seguirusuario==registrarusuario:
                            contador1+=1
                            print("No es posible seguirse a usted mismo")
                        
                        for i in seguidores:
                            if i[0]==registrarusuario:
                                if len(i)==1:
                                    i.append(seguirusuario)
                                    print("Usuario seguido exitosamente!")
                                    break
                                for je in i[1:]:
                                    if je==seguirusuario:
                                        contador1+=1
                                        print("usted ya sigue a este usuario")
                                if contador1==0:
                                    i.append(seguirusuario)
                                    print("Usuario seguido exitosamente!")
                                    break
                        x=open("seguidores.csv","w")
                        for seg in seguidores:
                            print(*seg, sep = "," ,file=x)
                        x.close()
                       
                    if opcion3=="2":
                        dejardeseguir=input("Ingrese usario al que quiere dejar de seguir")
                        for i in seguidores:
                            if i[0]==registrarusuario:
                                for jj in i[1:]:
                                    if jj==dejardeseguir:
                                        i.remove(jj)
                                        print("Se a dejado de seguir a el usuario")
                                        break
                                    else:
                                        print("Usted no sigue a el usuario o no existe")
                        x=open("seguidores.csv","w")
                        for seg in seguidores:
                            print(*seg, sep = "," ,file=x)
                        x.close()
                    if opcion3=="3":
                        j-=1
            if opcion1=="0":
                j=1
    
        
    if opcion=="0":
        break
                                                                                                                        
                                    

