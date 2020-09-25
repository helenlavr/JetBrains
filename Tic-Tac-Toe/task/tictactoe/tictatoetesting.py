coordinates = [13, 23, 33, 12, 22, 32, 11, 21, 31]
tie = 'Draw'
X = 'X'
O = 'O'


def ask_for_coordinates(question):
    """Ask for coordinates."""
    response = int("".join(input(question).split()))
    return response


def create_new_game_board():
    board = []
    for square in range(9):
        board.append(' ')
    return board


def game_board(field):
    print('-' * 9)
    print('|', field[0], field[1], field[2], '|')
    print('|', field[3], field[4], field[5], '|')
    print('|', field[6], field[7], field[8], '|')
    print('-' * 9)


def winner(board):
    ways_to_win = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (6, 4, 2))
    for row in ways_to_win:
        if board[row[0]] == board[row[1]] == board[row[2]] != empty:
            winner = board[row[0]]
            return winner
    if ' ' not in board:
        return tie
    return None


def congrat_winner(the_winner):
    if the_winner != tie:
        print(the_winner, 'wins')
    else:
        print(tie)

    if the_winner == X:
        print('X wins')

    elif the_winner == O:
        print('O wins')

    elif the_winner == tie:
        print(tie)


def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

""" 
def legal_move(move, marker):   # move: 11, 12, 13, etc marker: 'X' or 'O'
    moves = []
    for square in coordinates:
        if game_board()
    if move in coordinates:     # checks is move is valid
        trans_index = coordinates.index(move)
        print(trans_index)
        #for marker in field:
        if field[trans_index] != ' ':
            print('This cell is occupied! Choose another one!')
    elif move not in coordinates:
        print('Coordinates should be from 1 to 3!')
    else:
        print('You should enter numbers!')
    field[trans_index] = marker
"""





def main():
    turn = X
    board = create_new_game_board()
    game_board(board)

    while not winner(board):
        if turn == X:
            move = moves(board)
            board[move] = X
        else:
            move = moves(board)
            board[move] == O
        game_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner)



    """
    """
    while True:
        player_details = get_player_details(current_player)
        current_player = player_details[0]
        print("Player {}: Enter coordinates".format(current_player))
        input_slot = int("".join(input().split()))
        #game_board(field)
        move = legal_move(input_slot, player_details[1])
        game_board(move)
        count += 1
        winning = winning_game(player_details[1], current_player)
        if count == 9 and not winning:
            print('Drawn')
            tie = True
            game_board()
    """
main()
