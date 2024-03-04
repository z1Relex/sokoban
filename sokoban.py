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


class Sokoban:
    mapa = []
    personaje_columna = 0
    personaje_fila = 0

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
        
    def nivel1(self):
        self.mapa =[
            [3,3,3,3,3,3,3,3,3,3,3],
            [3,4,4,4,4,4,4,4,2,4,3],
            [3,4,0,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,2,4,3],
            [3,3,3,3,3,3,3,3,3,3,3]
        ]

        self.personaje_columna  = 2
        self.personaje_fila = 2
        self.imprimir_mapa()

    def nivel2(self):
        self.mapa =[
            [3,3,3,3,3,3,3,3,3,3,3],
            [3,4,4,4,4,4,4,4,2,4,3],
            [3,4,4,4,4,4,4,1,4,4,3],
            [3,4,2,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,2,3],
            [3,4,0,4,4,4,4,1,4,4,3],
            [3,4,4,4,2,4,4,4,4,4,3],
            [3,3,3,3,3,3,3,3,3,3,3]
        ]

        self.personaje_columna  = 2
        self.personaje_fila = 6
        self.imprimir_mapa()

    def nivel3(self):
        self.mapa =[
            [3,3,3,3,3,3,3,3,3,3,3],
            [3,4,4,4,4,2,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,0,3],
            [3,4,4,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,4,3],
            [3,4,4,2,4,4,4,4,4,4,3],
            [3,4,4,4,4,2,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,2,4,4,3],
            [3,4,4,4,4,4,4,4,4,4,3],
            [3,4,2,4,4,4,4,4,4,4,3],
            [3,3,3,3,3,3,3,3,3,3,3]
        ]

        self.personaje_columna  = 9
        self.personaje_fila = 3
        self.imprimir_mapa()




    #Imprime el mapa de nuevo si el personaje choca con una pared
    def movimiento0(self):
        self.limpiar_terminal()
        self.imprimir_mapa()

# PERSONAJE, PISO
        
    #Derecha personaje, pasillo
    def movimiento1(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1 ] = 0
        self.personaje_columna  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()
    
    #Izquierda personaje, pasillo
    def movimiento2(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1 ] = 0
        self.personaje_columna  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Arriba personaje, pasillo
    def movimiento3(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.personaje_fila  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Abajo personaje, pasillo
    def movimiento4(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.personaje_fila  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()

# PERSONAJE, META    
        
    #Derecha
    def movimiento5(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1 ] = 5
        self.personaje_columna  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()
    
    #Izquierda
    def movimiento6(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1 ] = 5
        self.personaje_columna  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Arriba
    def movimiento7(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.personaje_fila  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Abajo
    def movimiento8(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.personaje_fila  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()

#PERSONAJE-META, PISO
        
    #Derecha
    def movimiento9(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1 ] = 0
        self.personaje_columna  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()
    
    #Izquierda
    def movimiento10(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1 ] = 0
        self.personaje_columna  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Arriba
    def movimiento11(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.personaje_fila  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Abajo
    def movimiento12(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.personaje_fila  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()

#PERSONAJE-CAJA-PISO

    #Derecha
    def movimiento13(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1 ] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2 ] = 1
        self.personaje_columna  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()
    
    #Izquierda
    def movimiento14(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1 ] = 0
        self.mapa[self.personaje_fila][self.personaje_columna - 2 ] = 1
        self.personaje_columna  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Arriba
    def movimiento15(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
        self.personaje_fila  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Abajo
    def movimiento16(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
        self.personaje_fila  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()

#PERSONAJE-META, CAJA, PISO

    #Derecha
    def movimiento17(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1 ] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2 ] = 1
        self.personaje_columna  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()
    
    #Izquierda
    def movimiento18(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1 ] = 0
        self.mapa[self.personaje_fila][self.personaje_columna - 2 ] = 1
        self.personaje_columna  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Arriba
    def movimiento19(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
        self.personaje_fila  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Abajo
    def movimiento20(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
        self.personaje_fila  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()

#PERSONAJE, CAJA, META

    #Derecha
    def movimiento21(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1 ] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2 ] = 6
        self.personaje_columna  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()
    
    #Izquierda
    def movimiento22(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1 ] = 0
        self.mapa[self.personaje_fila][self.personaje_columna - 2 ] = 6
        self.personaje_columna  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Arriba
    def movimiento23(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
        self.personaje_fila  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Abajo
    def movimiento24(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
        self.personaje_fila  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()

#PERSONAJE, CAJA-META, PISO

    #Derecha
    def movimiento25(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1 ] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2 ] = 1
        self.personaje_columna  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()
    
    #Izquierda
    def movimiento26(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1 ] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2 ] = 1
        self.personaje_columna  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Arriba
    def movimiento27(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
        self.personaje_fila  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Abajo
    def movimiento28(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
        self.personaje_fila  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()






    def jugar(self):
        print(f"Posicion actual : {self.personaje_fila, self.personaje_columna}")
        movimiento = input("Introduce tu movimiento.")

        if movimiento == "d":
            if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
                self.movimiento1()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
                self.movimiento5()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
                self.movimiento9()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
                self.movimiento13()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
                self.movimiento17()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
                self.movimiento21()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
                self.movimiento25()
            else:
                self.movimiento0()

        elif movimiento == "a":
            if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4:
                self.movimiento2()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2:
                self.movimiento6()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4:
                self.movimiento10()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
                self.movimiento14()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
                self.movimiento18()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
                self.movimiento22()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
                self.movimiento26()
            else:
                self.movimiento0()  

        elif movimiento == "w":
            if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
                self.movimiento3()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2:
                self.movimiento7()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
                self.movimiento11()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
                self.movimiento15()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
                self.movimiento19()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
                self.movimiento23()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
                self.movimiento27()
            else:
                self.movimiento0()

        elif movimiento == "s":
            if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
                self.movimiento4()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2:
                self.movimiento8()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
                self.movimiento12()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
                self.movimiento16()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
                self.movimiento20()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
                self.movimiento24()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
                self.movimiento28()
            else:
                self.movimiento0()
        else:
            self.limpiar_terminal()
            self.imprimir_mapa()
            print("Movimiento invalido.")


jugar = Sokoban()
print("Bienvenido a Sokoban!")

while True:
    try:
        Nivel = int(input("Elige el nivel deseado:"))
        if Nivel in [1, 2, 3]:
            break
        else:
            print("Por favor, introduce un nivel válido (1, 2, 3).")
    except ValueError:
        print("Por favor, introduce un número.")

if Nivel == 1:
    jugar.nivel1()
elif Nivel == 2:
    jugar.nivel2()
elif Nivel == 3:
    jugar.nivel3()

while True:
    jugar.jugar()
