
# imports
from añadir_personajes import lista_personajes


def recorrer_lista_guardados():
    for personajes_guardados in lista_personajes:
        print(f'{personajes_guardados[0]} -> {personajes_guardados[1]} [{personajes_guardados[2]}/{personajes_guardados[3]}]')