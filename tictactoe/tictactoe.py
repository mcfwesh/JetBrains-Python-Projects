
cells = "_________"


def print_grid(cells):
    return(("""
        ---------------
        | {_1} {_2} {_3} |
        | {_4} {_5} {_6} |
        | {_7} {_8} {_9} |
        ---------------
        """).format(_1=cells[0], _2=cells[1], _3=cells[2], _4=cells[3], _5=cells[4], _6=cells[5], _7=cells[6], _8=cells[7], _9=cells[8]))


def game(board):
    permutations = [board[2:9:3], board[0:9:3], board[1:8:3],
                    board[0:9:4], board[2:7:2], board[0:3], board[3:6], board[6:9]]

    if ["X", "X", "X"] in permutations:
        return "X wins"
    if ["O", "O", "O"] in permutations:
        return "O wins"


def update_board():
    digits = ["1", "2", "3"]
    board = [cell for cell in cells]
    game_round = 1

    while game_round <= 10 and not game(board):
        move = input("Enter a move ").split()

        if not all(i.isdigit() for i in move):
            print("You should enter numbers!")
        elif not all(i in digits for i in move):
            print("Coordinates should be from 1 to 3!")
        else:
            i = int(move[1]) + 2
            j = int(move[0]) - 1
            index = (j * 3 + i) - 3
            for i, cell in enumerate(board):

                if i == index and (cell == "X" or cell == "O"):
                    print("This cell is occupied! Choose another one!")
                else:
                    if i == index:
                        if game_round % 2:
                            board[i] = 'X'
                            print(print_grid(board))
                        else:
                            board[i] = 'O'
                            print(print_grid(board))

        game_round += 1
        print(game_round)
        if game(board):
            print(game(board))
            break
        else:
            continue
    else:
        print('Draw')


print(print_grid(cells))
update_board()
