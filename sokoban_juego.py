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
import msvcrt

class Sokoban(Mapas, Movimientos):
    mapa = []
    personaje_columna = 0
    personaje_fila = 0
    Nivel = 0
    contador_he = 0

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
              6: " ✔"}

        for fila in self.mapa:
        # Reemplazar cada número en la fila por su emoji correspondiente
            fila_emojis = [emojis[celda] for celda in fila]
            print(''.join(fila_emojis))
    
    def limpiar_terminal(self):
        os.system("cls" if os.name == "nt" else "clear")

    def seleccion_nivel(self):
        self.contador_he = 0
        self.limpiar_terminal()
        if self.Nivel == 0:
            print("Bienvenido a Sokoban!")
            while True:
                try:
                    self.Nivel = int(input("Introduce el nivel deseado (1-4) y pulsa Enter para continuar:"))
                    # Obtener el método correspondiente al nivel
                    metodo_nivel = getattr(self, f'nivel{self.Nivel}', None)
                    # Si el método existe, llamarlo y salir del bucle
                    if metodo_nivel is not None:
                        self.limpiar_terminal()
                        metodo_nivel()
                        break
                    else:
                        self.limpiar_terminal()
                        print(f"El nivel {self.Nivel} no existe.")
                except ValueError:
                    self.limpiar_terminal()
                    print("Por favor, introduce un número.")
        else:
            metodo_nivel = getattr(self, f'nivel{self.Nivel}', None)
            metodo_nivel()

    def jugar(self):
        jugar.seleccion_nivel()
        while True:
            hay_cajas = False
            for fila in self.mapa:
                if 1 in fila:
                    hay_cajas = True
                    print(f"Posición actual : {self.personaje_fila, self.personaje_columna}")
                    print("Usa W,A,S,D para moverte por el mapa." "\n" "Usa Q para utilizar tu habilidad especial." "\n" "Usa R para reiniciar el nivel." "\n" "Usa X para salir al menú.")
                    self.movimientos_juego()
            if not hay_cajas:
                break
        while True:
            if jugar.Nivel != 4:
                print("Nivel completado! Pulsa L para continuar o X para salir al menu.")
                tecla_final = msvcrt.getch()
                tecla_comp = tecla_final.decode()
                if tecla_comp.lower() == "x":
                    self.Nivel = 0
                    break
                elif tecla_comp.lower() == "l":
                    self.Nivel += 1
                    break 
                else:
                    self.limpiar_terminal()
                    self.imprimir_mapa()                  
            else:
                print("Nivel completado! Gracias por jugar! Pulsa X para salir al menú.")
                tecla_final = msvcrt.getch()
                tecla_comp = tecla_final.decode()
                if tecla_comp.lower() == "x":
                    self.Nivel = 0
                    break
                else:
                    self.limpiar_terminal()
                    self.imprimir_mapa()

                


jugar = Sokoban()

while True:
    jugar.jugar()
