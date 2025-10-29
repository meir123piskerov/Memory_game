from game_functions.game_utils import *
from data.io import *


while True:
    border_x = int(input("enter x border"))
    border_y = int(input("enter y border"))
    if border_y > 10 and border_x > 10:
        print("bord to high! ,trt again")
        continue
    else:
        game = init_game(border_x, border_y)

        hidden_matrix = print_matrix(create_matrix(game,symbols_and_letters(game)))
        users_matrix = user_matrix(game)
        print_matrix(users_matrix)
        colon_x = int(input("enter colon x"))
        row_x = int(input("enter row x"))
        colon_y = int(input("enter colon y"))
        row_y = int(input("enter row y"))
        if hidden_matrix[colon_x][row_x] == hidden_matrix[colon_y][row_y]:
            users_matrix[colon_x][row_x] = hidden_matrix[colon_y][row_y]


