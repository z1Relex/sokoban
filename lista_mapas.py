class Mapas:

    def nivel1(self):
        self.mapa =[
            [3,3,3,3,3,4,4],
            [3,0,4,4,3,4,4],
            [3,4,3,1,3,3,3],
            [3,4,1,4,2,2,3],
            [3,3,3,3,3,3,3]
        ]

        self.personaje_columna  = 1
        self.personaje_fila = 1
        self.imprimir_mapa()

    def nivel2(self):
        self.mapa =[
            [4,4,4,4,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4],
            [4,4,4,4,3,4,4,4,3,4,4,4,4,4,4,4,4,4,4],
            [4,4,4,4,3,1,4,4,3,4,4,4,4,4,4,4,4,4,4],
            [4,4,3,3,3,4,4,1,3,3,4,4,4,4,4,4,4,4,4],
            [4,4,3,4,4,1,4,1,4,3,4,4,4,4,4,4,4,4,4],
            [3,3,3,4,3,4,3,3,4,3,4,4,4,3,3,3,3,3,3],
            [3,4,4,4,3,4,3,3,4,3,3,3,3,3,4,4,2,2,3],
            [3,4,1,4,4,1,4,4,4,4,4,4,4,4,4,4,2,2,3],
            [3,3,3,3,3,4,3,3,3,4,3,0,3,3,4,4,2,2,3],
            [4,4,4,4,3,4,4,4,4,4,3,3,3,3,3,3,3,3,3],
            [4,4,4,4,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4]
        ]

        self.personaje_columna  = 11
        self.personaje_fila = 8
        self.imprimir_mapa()

    def nivel3(self):
        self.mapa =[
            [3,3,3,3,3,3,3,3,3,3,3,3,4,4],
            [3,2,2,4,4,3,4,4,4,4,4,3,3,3],
            [3,2,2,4,4,3,4,1,4,4,1,4,4,3],
            [3,2,2,4,4,3,1,3,3,3,3,4,4,3],
            [3,2,2,4,4,4,4,0,4,3,3,4,4,3],
            [3,2,2,4,4,3,4,3,4,4,1,4,3,3],
            [3,3,3,3,3,3,4,3,3,1,4,1,4,3],
            [4,4,3,4,1,4,4,1,4,1,4,1,4,3],
            [4,4,3,4,4,4,4,3,4,4,4,4,4,3],
            [4,4,3,3,3,3,3,3,3,3,3,3,3,3]
        ]

        self.personaje_columna  = 7
        self.personaje_fila = 4
        self.imprimir_mapa()

        self.personaje_columna  = 9
        self.personaje_fila = 3
        self.imprimir_mapa()
