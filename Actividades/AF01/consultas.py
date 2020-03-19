from collections import defaultdict


def cantidad_animes_genero(animes):
    cantidad=dict()
    for ani in animes:
        for a in ani[1]:
            if a not in cantidad:
                cantidad[ani]=1
            else:
                cantidad[ani]+=1
    return cantidad
    



def generos_distintos(anime, animes):
    a=set(anime.genero)
    b=set()
    for j in animes:
        b=j.genero
        for k in b:
            b.append(k)
    diferencia=b-a
    return diferencia


def promedio_rating_genero(animes):
    promedio=dict()
    for anime in animes:
        anime.rating

    return promedio
    
