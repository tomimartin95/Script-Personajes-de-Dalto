
# imports
from creacion_personajes import Personaje

# Lista de personajes creados
lista_personajes = list()


def añadir():
    creacion_personaje = Personaje(id = Personaje.id, nombre = input("NOMBRE: ").upper(), ataque = int(input("PUNTOS DE ATAQUE: ")), defensa = int(input("PUNTOS DE DEFENSA: ")))
    
    lista_personajes.append((creacion_personaje.id, creacion_personaje.nombre, creacion_personaje.ataque, creacion_personaje.defensa))
    
    print("\n--------------------------------\nPersonaje creado correctamente!\n--------------------------------\n")