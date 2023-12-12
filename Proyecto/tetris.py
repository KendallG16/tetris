from enum import Enum

class Movement(Enum):
    izquieda = 1
    derecha = 2
    abajo = 3
    rotar = 4

def tetris():
    screen = [["|","🔳","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
              ["|","🔳","🔳","🔳","🔲","🔲","🔲","🔲","🔲","🔳","🔲","|"],
              ["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
              ["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
              ["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
              ["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
              ["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
              ["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
              ["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
              ["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
    ]       
    print_tetris(screen)
    screen = move(screen, Movement.derecha)
    screen = move(screen, Movement.izquieda)
    screen = move(screen, Movement.derecha)
    screen = move(screen, Movement.izquieda)
    screen = move(screen, Movement.rotar)


    

def print_tetris(screen:list):
    print("\nPantall Tetris\n")
    for i in screen:
        print("".join(map(str, i[1:-1])))

def move(screen: list,movement : Movement) -> list:

    nueva_pantalla = [["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
                      ["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
                      ["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
                      ["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
                      ["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
                      ["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
                      ["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
                      ["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
                      ["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
                      ["|","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","|"],
    ]           

    for fila_actual, fila in enumerate(screen):
        for columna_actual, item in enumerate(fila):

            if item == "🔳": 
                limite = 0
                nueva_columna = 0
                nueva_fila = 0

                match movement:
                    case Movement.abajo:
                      nueva_fila = fila_actual + 1
                      nueva_columna = columna_actual

                    case Movement.izquieda:
                        if(columna_actual - 1) == 0:
                            return screen
                        else:
                            nueva_columna = columna_actual -1
                            nueva_fila = fila_actual
                    case Movement.derecha:
                        if(columna_actual + 1) == 11:
                            return screen
                        else:
                            nueva_columna = columna_actual + 1
                            nueva_fila = fila_actual

                    case Movement.rotar:
                        nueva_columna = reversed("🔳")
                        nueva_fila = fila_actual
                if nueva_fila > 9 or nueva_columna >11 or nueva_columna < 0:
                    print("nonse")
                else: 
                    nueva_pantalla[nueva_fila][nueva_columna] = "🔳"
    print_tetris(nueva_pantalla)
    return nueva_pantalla

tetris()