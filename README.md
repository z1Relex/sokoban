# sokoban
Implementación de Sokoban versión retro en Python.

## 0. Objetivo

Programar el juego Sokoban en una versión retro para consola.

## 1. Reglas del juego

El juego Sokoban consiste en acomodar cajas en puntos determinados por las metas.

1. El personaje se puede mover hacia arriba, abajo, izquierda y derecha.
2. El personaje solo puede empujar 1 caja en cualquier sentido.
3. El personaje se moverá en un mapa predefinido.
4. Para terminar el nivel se tienen que acomodar totas las cajas sobre las metas.

## 2. Elementos del juego

### 2.0 Mapas de juego

Cada nivel del juego se colocará dentro de una array bidimensional, colocando numeros para representar los elementos de juego, a continuación se tiene un ejemplo básico de nivel.

mapa = []

### 2.1 Lista de elementos

- 0 - Personaje
- 1 - Cajas
- 2 - Metas
- 3 - Paredes
- 4 - Piso
- 5 - Personaje meta
- 6 - Caja meta

## 3. Controles

Para moverse y realizar acciones en el juego el usuario utilizará las siguientes letras.

- a -> Izquierda
- s -> Derecha
- w -> Arriba
- s -> Abajo
- q -> Habilidad especial
- u -> Deshacer el último movimiento
- Esc -> Salir del nivel

## 4. Funciones a implementar

| Método |Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
|  | Cargar el siguiente nivel. | Por hacer | - | | - |
|  | Repetir el juego hasta terminar el nivel. | Por hacer | - | | - |
| imprimir_mapa | Imprimir mapa.| Hecho | 03/03 |
| limpiar_terminal | Limpiar la terminal.| Hecho | 03/03 |
|  | Leer el movimiento. | Hecho | 03/03 |
|  | Evaluar el movimiento del usuario. | Hecho | 03/03 |

## Derecha

| Método | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| movimiento1 | Personaje, piso  | Hecho | [0,4] | [4,0] | 03/03 |
| movimiento5 | Personaje, meta  | Hecho | [0,2] | [4,5] | 03/03 |
| movimiento9 | Personaje_meta, piso | Hecho | [5,4] | [2,0] | 03/03 |
| movimiento13 | Personaje, caja, piso | Hecho | [0,1,4] | [4,0,1] | 03/03 |
| movimiento17 | Personaje_meta, caja, piso | Hecho | [5,1,4] | [2,0,1] | 03/03 |
| movimiento21 | Personaje, caja,  meta | Hecho | [0,1,2] | [4,0,6] | 03/03 |
| movimiento25. | Personaje, caja_meta, piso | Hecho | [0,6,4] | [4,5,1] | 04/03 |
|  | Personaje, caja_meta, meta | Por hacer | [] | [] | - |
|  | Personaje_meta, meta | Por hacer | [] | [] | - |
|  | Personaje_meta, caja, meta | Por hacer | [] | [] | - |
|  | Personaje_meta, caja_meta, piso | Por hacer | [] | [] | - |
|  | Personaje_meta, caja_meta, meta | Por hacer | [] | [] | - |

## Izquierda

| Método | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| movimiento2 | Personaje, piso  | Hecho | [0,4] | [4,0] | 03/03 |
| movimiento6 | Personaje, meta  | Hecho | [0,2] | [4,5] | 03/03 |
| movimiento10 | Personaje_meta, piso | Hecho | [5,4] | [2,0] | 03/03 |
| movimiento14 | Personaje, caja, piso | Hecho | [0,1,4] | [4,0,1] | 03/03 |
| movimiento18 | Personaje_meta, caja, piso | Hecho | [5,1,4] | [2,0,1] | 03/03 |
| movimiento22 | Personaje, caja,  meta | Hecho | [0,1,2] | [4,0,6] | 03/03 |
| movimiento26. | Personaje, caja_meta, piso | Hecho | [0,6,4] | [4,5,1] | 04/03 |
|  | Personaje, caja_meta, meta | Por hacer | [] | [] | - |
|  | Personaje_meta, meta | Por hacer | [] | [] | - |
|  | Personaje_meta, caja, meta | Por hacer | [] | [] | - |
|  | Personaje_meta, caja_meta, piso | Por hacer | [] | [] | - |
|  | Personaje_meta, caja_meta, meta | Por hacer | [] | [] | - |

## Arriba

| Método | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| movimiento3 | Personaje, piso  | Hecho | [0,4] | [4,0] | 03/03 |
| movimiento7 | Personaje, meta  | Hecho | [0,2] | [4,5] | 03/03 |
| movimiento11 | Personaje_meta, piso | Hecho | [5,4] | [2,0] | 03/03 |
| movimiento15 | Personaje, caja, piso | Hecho | [0,1,4] | [4,0,1] | 03/03 |
| movimiento19 | Personaje_meta, caja, piso | Hecho | [5,1,4] | [2,0,1] | 03/03 |
| movimiento23 | Personaje, caja,  meta | Hecho | [0,1,2] | [4,0,6] | 03/03 |
| movimiento27. | Personaje, caja_meta, piso | Hecho | [0,6,4] | [4,5,1] | 04/03 |
|  | Personaje, caja_meta, meta | Por hacer | [] | [] | - |
|  | Personaje_meta, meta | Por hacer | [] | [] | - |
|  | Personaje_meta, caja, meta | Por hacer | [] | [] | - |
|  | Personaje_meta, caja_meta, piso | Por hacer | [] | [] | - |
|  | Personaje_meta, caja_meta, meta | Por hacer | [] | [] | - |

## Abajo

| Método | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| movimiento4 | Personaje, piso  | Hecho | [0,4] | [4,0] | 03/03 |
| movimiento8 | Personaje, meta  | Hecho | [0,2] | [4,5] | 03/03 |
| movimiento12 | Personaje_meta, piso | Hecho | [5,4] | [2,0] | 03/03 |
| movimiento16 | Personaje, caja, piso | Hecho | [0,1,4] | [4,0,1] | 03/03 |
| movimiento20 | Personaje_meta, caja, piso | Hecho | [5,1,4] | [2,0,1] | 03/03 |
| movimiento24 | Personaje, caja,  meta | Hecho | [0,1,2] | [4,0,6] | 03/03 |
| movimiento28. | Personaje, caja_meta, piso | Hecho | [0,6,4] | [4,5,1] | 04/03 |
|  | Personaje, caja_meta, meta | Por hacer | [] | [] | - |
|  | Personaje_meta, meta | Por hacer | [] | [] | - |
|  | Personaje_meta, caja, meta | Por hacer | [] | [] | - |
|  | Personaje_meta, caja_meta, piso | Por hacer | [] | [] | - |
|  | Personaje_meta, caja_meta, meta | Por hacer | [] | [] | - |

