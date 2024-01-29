
#!  - PROGRAMA DE CREACION, FUSIÓN Y MODIFICACIÓN DE PERSONAJES -
#!                   CURSO POO EN PYTHON DE DALTO


# imports
from añadir_personajes import añadir
from lista_personajes import recorrer_lista_guardados
from fusion import fusionar_personajes

def menu():
    
    while True:
        opcion = int(input("\n\n      - - - - - - - - -\n       INGRESE OPCIÓN\n      - - - - - - - - -\n [1] Crear personaje nuevo \n [2] Fusionar personajes \n [3] Mostrar listado de personajes \n [4] Salir \n\n -> "))
        print("\n")
    
        if opcion == 1:
            añadir()
                
        elif opcion == 2:
            fusionar_personajes()
        
        elif opcion == 3:
            print("\n---------LISTA DE PERSONAJES---------\n")
            recorrer_lista_guardados()
        
        elif opcion == 4:
            print("Finalizando programa...")
            break
        
        else:
            print("\n----------------------------------\nOpción invalida. Vuelva a intentar\n----------------------------------\n")

menu()