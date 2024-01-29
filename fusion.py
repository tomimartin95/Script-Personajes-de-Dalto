
# imports
from creacion_personajes import Personaje
from lista_personajes import *
from añadir_personajes import lista_personajes

def fusionar_personajes():
    print("\n--------ELIJA PERSONAJES DOS PARA FUSIONAR--------\n")
    
    recorrer_lista_guardados()
    
    personaje_1 = int(input("Seleccione un personaje -> "))
    personaje_2 = int(input("Seleccione otro personaje -> "))
    
    for id in lista_personajes:
        if personaje_1 == id[0]:
            personaje_seleccionado_1 = Personaje(id[0], id[1], id[2], id[3])
            
        if personaje_2 == id[0]:
            personaje_seleccionado_2 = Personaje(id[0], id[1], id[2], id[3])
            
    fusion = personaje_seleccionado_1 + personaje_seleccionado_2
    
    
    print("\n---------FUSIÓN CONCRETADA---------\n")
    
    print(f'''        {fusion.nombre}\n
        ATAQUE = {round(((fusion.ataque)/2)*2)}
        DEFENSA = {round(((fusion.defensa)/2)*1.5)}
            \n
            ''')