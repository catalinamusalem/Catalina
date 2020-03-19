from collections import namedtuple, deque


def cargar_animes(path):
    animes= namedtuple("animes", ["nombre", "rating", "estudio", "genero"])
    diccionario1=dict()
    # Abrimos el archivo de animes
    with open(path, 'r', encoding="utf-8") as file:
        # Leemos las lineas
        for line in file.readlines():
            # Las separamos por coma
            anime = line.strip().split(",")
            # Separamos los generos por slash
            anime[3] = anime[3].split("/")
            arreglo=set(anime[3])
            anime[3]=list(arreglo)
            
            i = (animes(*anime))
            diccionario1[i.nombre]=(int(i.rating),str(i.estudio),i.genero)
            

    return(diccionario1)
cargar_animes("animes.csv")
print(diccionario1)

def cargar_consultas(path):
    cola = deque()
    # Abrimos el archivo de animes
    with open(path, 'r', encoding="utf-8") as file:
        # Leemos las lineas
        for line in file.readlines():
            # Los separamos por coma
            consulta = line.strip().split(";")
            argumentos=consulta[1].split("/")
            tupla=(consulta[0],argumentos)
            cola.append(tupla)
    
        

    return cola


