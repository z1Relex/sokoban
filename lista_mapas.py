class Mapas:

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
            [3,4,2,2,2,4,2,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,2,3],
            [3,4,0,1,4,4,4,1,4,4,3],
            [3,4,4,2,2,4,4,4,4,4,3],
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
