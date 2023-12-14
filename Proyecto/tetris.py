from enum import Enum

class Movement(Enum):
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    ROTATE = 4

def tetris():# 0    1     2    3     4    5     6    7     8    9
    screen=[["🔳","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],#0
            ["🔳","🔳","🔳","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],#1
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],#2
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],#3
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],#4
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],#5
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],#6
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],#7
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],#8
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],#9
        ]
    print_screen(screen)
    rotation = 0
    while True:
        input_key = input("D = down, L = left, R = right, U = rotate: ")

        if input_key == "D" :
            (screen, rotation) = move_pieces(screen, Movement.DOWN, rotation)
        elif input_key == "L" :
            (screen, rotation) = move_pieces(screen, Movement.LEFT, rotation)
        elif input_key == "R" :
            (screen, rotation) = move_pieces(screen, Movement.RIGHT, rotation)
        elif input_key == "U" :
            (screen, rotation) = move_pieces(screen, Movement.ROTATE, rotation)
        else:
            print("Invalid input. Use D, L, R, or U")



def print_screen(screen: list):
    print("".join(["".join(row) + "\n" for row in screen]))

def move_pieces(screen: list, movement: Movement, rotation: int) -> (list, int):
    rotation_item = 0
    new_rotation = 0
    rotate_direction = [
        [(1, 1), (0, 0), (-2, 0), (-1, -1)],
        [(0, 1), (-1, 0), (0, -1), (1, -2)],
        [(0, 2), (1, 1), (-1, 1), (-2, 0)],    
        [(0, 1), (1, 0), (2, -1), (1, -2)]
        ]

    if movement is Movement.ROTATE:
        new_rotation = 0  if rotation == 3 else rotation + 1
    
    new_screen = [["🔲" for _ in range(10)] for _ in range(10)]
    
    for row_index, row in enumerate(screen):
        for column_index, item in enumerate(row):
            if item == "🔳":
                new_row = row_index
                new_column = column_index

                if movement == Movement.DOWN:
                    new_row += 1

                elif movement == Movement.LEFT:
                    if new_column > 0 :
                        new_column -= 1
                    else:
                        print("Invalid direction")
                        return screen
                    
                elif movement == Movement.RIGHT:
                    if new_column < 9:
                        new_column += 1
                    else:
                        print("Invalid direction")
                        return screen
                    
                elif movement == Movement.ROTATE:
                    new_row = row_index  + rotate_direction[new_rotation][rotation_item][0]
                    new_column = column_index + rotate_direction[new_rotation][rotation_item][1]
                    rotation_item += 1
                    if rotation_item > 3:
                        rotation_item = 0   
                
                if new_row > 9 or new_column > 9 or new_column < 0:
                    print("Invalid direction")
                else: 
                    new_screen[new_row][new_column] = "🔳"

    def print_new_screen(new_screen: list):
        print("".join(["".join(row) + "\n" for row in new_screen]))    
    print_new_screen(new_screen)

    return new_screen, new_rotation
tetris()