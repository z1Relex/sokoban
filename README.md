# sokoban
Implementación de Sokoban versión retro en Python.

## 0. Objetivo

Programar el juego Sokoban en una versión retro para consola.

## 1. Reglas del juego

El juego Sokoban consiste en acomodar cajas en puntos determinados por las metas.

1. El personaje se puede mover hacia arriba, abajo, izquierda y derecha.
2. El personaje solo puede empujar 1 caja en cualquier sentido.
3. El personaje se moverá en un mapa predefinido.
4. El personaje cuenta con una habilidad especial (1 uso por nivel) que le permite destruir las cajas ubicadas en su misma fila.
5. Para terminar el nivel, no debe haber ninguna caja restante en el mapa de juego.

## 2. Elementos del juego

### 2.0 Mapas de juego

Cada nivel del juego se colocará dentro de una array bidimensional, colocando números para representar los elementos de juego.

- Nivel 1
  [3,3,3,3,3,4,4],
  [3,0,4,4,3,4,4],
  [3,4,3,1,3,3,3],
  [3,4,1,4,2,2,3],
  [3,3,3,3,3,3,3]

- Nivel 2
  
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

- Nivel 3
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
  
### 2.1 Lista de elementos

- 0 - Personaje
- 1 - Cajas
- 2 - Metas
- 3 - Paredes
- 4 - Piso
- 5 - Personaje-meta
- 6 - Caja-meta

## 3. Controles

Para moverse y realizar acciones en el juego el usuario utilizará las siguientes letras.

- a -> Izquierda
- d -> Derecha
- w -> Arriba
- s -> Abajo
- q -> Habilidad especial
- r -> Reiniciar nivel
- x -> Salir del nivel

## 4. Funciones a implementar

| Método |Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| jugar  | Cargar el siguiente nivel. | Hecho | 08/03 |
| jugar | Repetir el juego hasta terminar el nivel. | Hecho | 08/03 |
| imprimir_mapa | Imprimir mapa.| Hecho | 03/03 |
| limpiar_terminal | Limpiar la terminal.| Hecho | 03/03 |
| movimientos_juego | Leer el movimiento. | Hecho | 03/03 |
| movimientos_juego | Evaluar el movimiento del usuario. | Hecho | 03/03 |
| seleccion_nivel | Cargar nivel / Reiniciar  | Hecho | 08/03 |

## Derecha

| Método | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| movimiento1 | Personaje, piso  | Hecho | [0,4] | [4,0] | 03/03 |
| movimiento5 | Personaje, meta  | Hecho | [0,2] | [4,5] | 03/03 |
| movimiento9 | Personaje_meta, piso | Hecho | [5,4] | [2,0] | 03/03 |
| movimiento13 | Personaje, caja, piso | Hecho | [0,1,4] | [4,0,1] | 03/03 |
| movimiento17 | Personaje_meta, caja, piso | Hecho | [5,1,4] | [2,0,1] | 03/03 |
| movimiento21 | Personaje, caja,  meta | Hecho | [0,1,2] | [4,0,6] | 03/03 |
| movimiento25 | Personaje, caja_meta, piso | Hecho | [0,6,4] | [4,5,1] | 04/03 |
| movimiento29 | Personaje, caja_meta, meta | Hecho | [0,6,2] | [4,5,6] | 04/03 |
| movimiento33 | Personaje_meta, meta | Hecho | [5,2] | [2,5] | 04/03 |
| movimiento37 | Personaje_meta, caja, meta | Hecho | [5,1,2] | [2,0,6] | 04/03 |
| movimiento41 | Personaje_meta, caja_meta, piso | Hecho | [5,6,4] | [2,5,1] | 04/03 |
| movimiento45 | Personaje_meta, caja_meta, meta | Hecho | [5,6,2] | [2,5,6] | 04/03 |

## Izquierda

| Método | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| movimiento2 | Personaje, piso  | Hecho | [4,0] | [0,4] | 03/03 |
| movimiento6 | Personaje, meta  | Hecho | [2,0] | [5,4] | 03/03 |
| movimiento10 | Personaje_meta, piso | Hecho | [4,5] | [0,2] | 03/03 |
| movimiento14 | Personaje, caja, piso | Hecho | [4,1,0] | [1,0,4] | 03/03 |
| movimiento18 | Personaje_meta, caja, piso | Hecho | [4,1,5] | [1,0,2] | 03/03 |
| movimiento22 | Personaje, caja,  meta | Hecho | [2,1,0] | [6,0,4] | 03/03 |
| movimiento26 | Personaje, caja_meta, piso | Hecho | [4,6,0] | [1,5,4] | 04/03 |
| movimiento30 | Personaje, caja_meta, meta | Hecho | [2,6,0] | [6,5,4] | 04/03 |
| movimiento34 | Personaje_meta, meta | Hecho | [2,5] | [5,2] | 04/03 |
| movimiento38 | Personaje_meta, caja, meta | Hecho | [2,1,5] | [6,0,2] | 04/03 |
| movimiento42 | Personaje_meta, caja_meta, piso | Hecho | [4,6,5] | [1,5,2] | 04/03 |
| movimiento46 | Personaje_meta, caja_meta, meta | Hecho | [2,6,5] | [6,5,2] | 04/03 |

## Arriba

| Método | Función | Kanban | Inicio (abajo-arriba) | Fin (abajo-arriba) | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| movimiento3 | Personaje, piso  | Hecho | [0,4] | [4,0] | 03/03 |
| movimiento7 | Personaje, meta  | Hecho | [0,2] | [4,5] | 03/03 |
| movimiento11 | Personaje_meta, piso | Hecho | [5,4] | [2,0] | 03/03 |
| movimiento15 | Personaje, caja, piso | Hecho | [0,1,4] | [4,0,1] | 03/03 |
| movimiento19 | Personaje_meta, caja, piso | Hecho | [5,1,4] | [2,0,1] | 03/03 |
| movimiento23 | Personaje, caja,  meta | Hecho | [0,1,2] | [4,0,6] | 03/03 |
| movimiento27 | Personaje, caja_meta, piso | Hecho | [0,6,4] | [4,5,1] | 04/03 |
| movimiento31 | Personaje, caja_meta, meta | Hecho | [0,6,2] | [4,5,6] | 04/03 |
| movimiento35 | Personaje_meta, meta | Hecho | [5,2] | [2,5] | 04/03 |
| movimiento39 | Personaje_meta, caja, meta | Hecho | [5,1,2] | [2,0,6] | 04/03 |
| movimiento43 | Personaje_meta, caja_meta, piso | Hecho | [5,6,4] | [2,5,1] | 04/03 |
| movimiento47 | Personaje_meta, caja_meta, meta | Hecho | [5,6,2] | [2,5,6] | 04/03 |

## Abajo

| Método | Función | Kanban | Inicio (arriba-abajo) | Fin (arriba-abajo) | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| movimiento4 | Personaje, piso  | Hecho | [0,4] | [4,0] | 03/03 |
| movimiento8 | Personaje, meta  | Hecho | [0,2] | [4,5] | 03/03 |
| movimiento12 | Personaje_meta, piso | Hecho | [5,4] | [2,0] | 03/03 |
| movimiento16 | Personaje, caja, piso | Hecho | [0,1,4] | [4,0,1] | 03/03 |
| movimiento20 | Personaje_meta, caja, piso | Hecho | [5,1,4] | [2,0,1] | 03/03 |
| movimiento24 | Personaje, caja,  meta | Hecho | [0,1,2] | [4,0,6] | 03/03 |
| movimiento28 | Personaje, caja_meta, piso | Hecho | [0,6,4] | [4,5,1] | 04/03 |
| movimiento32 | Personaje, caja_meta, meta | Hecho | [0,6,2] | [4,5,6] | 04/03 |
| movimiento36 | Personaje_meta, meta | Hecho | [5,2] | [2,5] | 04/03 |
| movimiento40 | Personaje_meta, caja, meta | Hecho | [5,1,2] | [2,0,6] | 04/03 |
| movimiento44 | Personaje_meta, caja_meta, piso | Hecho | [5,6,4] | [2,5,1] | 04/03 |
| movimiento48 | Personaje_meta, caja_meta, meta | Hecho | [5,6,2] | [2,5,6] | 04/03 |

## Funciones especiales

| Método | Función | Kanban | Descripción | Fecha terminación |
| --- | --- | --- | --- | --- |
| movimiento99 | Habilidad especial  | Hecho | Destrucción de cajas en la misma fila | 08/03 |





