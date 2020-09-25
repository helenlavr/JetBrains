def game_board():
    board = []
    for square in range(0, 9):
        board.append(' ')
    return board


def print_game_board(board):  # board = input cells
    print('-' * 9)
    for i in range(0, len(board), 3):
        print('|', *board[i: i + 3], '|')
    print('-' * 9)


def winner(board):
    done = False
    row = [board[:3], board[3:6], board[6:]]
    column = [board[:7:3], board[1:8:3], board[2::3]]
    diagonal = [board[0::4], board[2:7:2]]

    check_win = row + column + diagonal
    count_x = board.count('X')
    count_o = board.count('O')

    if (['X', 'X', 'X'] in check_win and ['O', 'O', 'O'] in check_win) or abs(count_x-count_o > 1):
        print('Impossible')
        done = True
    elif ['X', 'X', 'X'] in check_win:
        print('X wins')
        done = True
    elif ['O', 'O', 'O'] in check_win:
        print('O wins')
        done = True
    elif board.count(' ') > 0:
        print('Game not finished')
        done = False
    else:
        print('Draw')
        done = True
    return done


def game_done(board):
    done = False
    row = board[:3], board[3:6], board[6:]
    column = board[:7:3], board[1:8:3], board[2::3]
    diagonal = board[0::4], board[2:7:2]

    check_win = row + column + diagonal
    count_x = board.count('X')
    count_o = board.count('O')
    if (['X', 'X', 'X'] in check_win and ['O', 'O', 'O'] in check_win) or abs(count_x-count_o > 1):
        done = True
    elif ['X', 'X', 'X'] in check_win:
        done = True
    elif ['O', 'O', 'O'] in check_win:
        done = True
    elif board.count(' ') > 0:
        done = False
    else:
        done = True
    return done


coordinates = ['1 3', '2 3', '3 3', '1 2', '2 2', '3 2', '1 1', '2 1', '3 1']


def check(user_coordinate, board):
    if not user_coordinate.split()[0].isdigit() or not user_coordinate.split()[1].isdigit():
        print('You should enter numbers!')
        return False
    elif int(user_coordinate.split()[0]) > 3 or int(user_coordinate.split()[1]) > 3:
        print('Coordinates should be from 1 to 3!')
        return False
    elif board[coordinates.index(user_coordinate)] != ' ':  # this is not working. fml
        print('This cell is occupied! Choose another one!')
        return False
    else:
        return None


def next_turn(tur):
    if tur == 'X':
        return 'O'
    else:
        return 'X'


def main():
    new_game_board = game_board()
    print_game_board(new_game_board)
    turn = 'X'

    while game_done(new_game_board) is False:
        user_coor_input = input('Enter coordinate: ')

        while check(user_coor_input, new_game_board) is False:
            user_coor_input = input('Enter coordinate: ')
            print(check(user_coor_input, new_game_board))

        if turn == 'X':
            new_game_board[coordinates.index(user_coor_input)] = 'X'
        else:
            new_game_board[coordinates.index(user_coor_input)] = 'O'
        print_game_board(new_game_board)
        turn = next_turn(turn)

        if winner(new_game_board):
            break


main()

