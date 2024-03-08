class Movimientos:
    #Imprime el mapa de nuevo si el personaje choca con una pared
    def movimiento0(self):
        self.limpiar_terminal()
        self.imprimir_mapa()

# PERSONAJE, PISO
        
    #Derecha 
    def movimiento1(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1 ] = 0
        self.personaje_columna  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()
    
    #Izquierda 
    def movimiento2(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1 ] = 0
        self.personaje_columna  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Arriba 
    def movimiento3(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.personaje_fila  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Abajo 
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

#PERSONAJE, CAJA-META, META

    #Derecha
    def movimiento29(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1 ] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2 ] = 6
        self.personaje_columna  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()
    
    #Izquierda
    def movimiento30(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1 ] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2 ] = 6
        self.personaje_columna  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Arriba
    def movimiento31(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
        self.personaje_fila  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Abajo
    def movimiento32(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
        self.personaje_fila  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()

#PERSONAJE-META, META
        
    #Derecha
    def movimiento33(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1 ] = 5
        self.personaje_columna  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()
    
    #Izquierda
    def movimiento34(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1 ] = 5
        self.personaje_columna  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Arriba
    def movimiento35(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.personaje_fila  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Abajo
    def movimiento36(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.personaje_fila  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()

#PERSONAJE-META, CAJA, META

    #Derecha
    def movimiento37(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1 ] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2 ] = 6
        self.personaje_columna  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()
    
    #Izquierda
    def movimiento38(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1 ] = 0
        self.mapa[self.personaje_fila][self.personaje_columna - 2 ] = 6
        self.personaje_columna  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Arriba
    def movimiento39(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
        self.personaje_fila  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Abajo
    def movimiento40(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
        self.personaje_fila  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()

#PERSONAJE-META, CAJA-META, PISO

    #Derecha
    def movimiento41(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1 ] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2 ] = 1
        self.personaje_columna  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()
    
    #Izquierda
    def movimiento42(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1 ] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2 ] = 1
        self.personaje_columna  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Arriba
    def movimiento43(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
        self.personaje_fila  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Abajo
    def movimiento44(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
        self.personaje_fila  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()

#PERSONAJE-META, CAJA-META, META

    #Derecha
    def movimiento45(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1 ] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2 ] = 6
        self.personaje_columna  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()
    
    #Izquierda
    def movimiento46(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1 ] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2 ] = 6
        self.personaje_columna  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Arriba
    def movimiento47(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
        self.personaje_fila  -= 1
        self.limpiar_terminal()
        self.imprimir_mapa()

    #Abajo
    def movimiento48(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
        self.personaje_fila  += 1
        self.limpiar_terminal()
        self.imprimir_mapa()


    def movimientos_juego(self):
        movimiento = input()
        if movimiento.lower() == "d":
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
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
                self.movimiento29()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
                self.movimiento33()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
                self.movimiento37()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
                self.movimiento41()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
                self.movimiento45()
            else:
                self.movimiento0()

        elif movimiento.lower() == "a":
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
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
                self.movimiento30()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2:
                self.movimiento34()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
                self.movimiento38()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
                self.movimiento42()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
                self.movimiento46()            
            else:
                self.movimiento0()  

        elif movimiento.lower() == "w":
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
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
                self.movimiento31()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2:
                self.movimiento35()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
                self.movimiento39()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
                self.movimiento43()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
                self.movimiento47()
            else:
                self.movimiento0()

        elif movimiento.lower() == "s":
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
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
                self.movimiento32()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2:
                self.movimiento36()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
                self.movimiento40()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
                self.movimiento44()
            elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
                self.movimiento48()
            else:
                self.movimiento0()
        elif movimiento.lower() == "r":
            self.elegir_nivel()
        else:
            self.limpiar_terminal()
            self.imprimir_mapa()
            print("Movimiento inválido.")
