
# Estructura de personaje
class Personaje():
    id = 0
    def __init__(self, id, nombre,ataque, defensa):
        Personaje.id += 1
        id = Personaje.id
        
        self.id = id
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
    
    def __add__(self, otro_pj):
        nuevo_id = self.id + otro_pj.id
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nuevo_ataque = round(((self.ataque+otro_pj.ataque)/2)**1.5)
        nueva_defensa = round(((self.defensa+otro_pj.defensa)/2)*1.5)
        return Personaje(nuevo_id, nuevo_nombre, nuevo_ataque, nueva_defensa)

    def presentacion(self):
        print(f''' \n {self.nombre} \n ---------------------------- \n ATAQUE = {self.ataque} \n DEFENSA = {self.defensa}''')