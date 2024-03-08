"""

Sokoban 

0 - Personaje
1 - Cajas
2 - Metas
3 - Paredes
4 - Piso
5 - Personaje-meta
6 - Caja-meta 

"""

import os
from lista_mapas import Mapas
from lista_movimientos import Movimientos

class Sokoban(Mapas, Movimientos):
    mapa = []
    personaje_columna = 0
    personaje_fila = 0
    Nivel = 0

    def __init__ (self):
        pass
    
    def imprimir_mapa(self):
    # Crear un diccionario que mapee cada número a un emoji
        emojis = {0: "🚶",
              1: "📦", 
              2: "🏳 ",
              3: "⬜",
              4: "  ",
              5: "🚩",
              6: " 🏁"}

        for fila in self.mapa:
        # Reemplazar cada número en la fila por su emoji correspondiente
            fila_emojis = [emojis[celda] for celda in fila]
            print(''.join(fila_emojis))
    
    def limpiar_terminal(self):
        os.system("cls" if os.name == "nt" else "clear")

    def elegir_nivel(self):
        if self.Nivel == 1:
            jugar.nivel1()
        elif self.Nivel == 2:
            jugar.nivel2()
        elif self.Nivel == 3:
            jugar.nivel3()

    def jugar(self):
        while True:
            hay_cajas = False
            for fila in self.mapa:
                if 1 in fila:
                    hay_cajas = True
                    print(f"Posición actual : {self.personaje_fila, self.personaje_columna}")
                    print("Usa W,A,S,D para moverte por el mapa. Usa Q para utilizar tu habilidad especial.")
                    print("Usa R para reiniciar el nivel.")
                    print("Usa Z para salir al menú.")
                    self.movimientos_juego()
            if not hay_cajas:
                break

                


jugar = Sokoban()


print("Bienvenido a Sokoban!")

while True:
    try:
        jugar.Nivel = int(input("Elige el nivel deseado:"))
        if jugar.Nivel in [1, 2, 3]:
            break
        else:
            print("Por favor, introduce un nivel válido (1, 2, 3).")
    except ValueError:
        print("Por favor, introduce un número.")

jugar.elegir_nivel()

while True:
    jugar.jugar()
    break

if jugar.Nivel != 3:
    print("Nivel completado! Pulsa Enter para continuar o X para salir al menu.")
else:
    print("Nivel completado! Gracias por jugar.")
