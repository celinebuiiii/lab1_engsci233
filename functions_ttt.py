def initialise_board():
    list_board = ['.'] * 9
    return list_board


def display_board(list_board):
    print(list_board[0], list_board[1], list_board[2])
    print(list_board[3], list_board[4], list_board[5])
    print(list_board[6], list_board[7], list_board[8])


def get_current_turn_number(list_board):
    count = 1
    empty_pos = '.'
    for i in list_board:
        if i is not empty_pos:
            count += 1
    return count


def get_current_player(list_board):
    player_1 = 0
    player_2 = 0
    current_player = 'X'
    for i in list_board:
        if i == 'X':
            player_1 += 1
        elif i == 'O':
            player_2 += 1
    if player_1 == 0 or player_2 > player_1:
        current_player = 'X'
    return current_player


def play_turn(list_board, r, c):
    current = get_current_player(list_board)

    if r == 3:
        if c == 3:
            a = 3
        elif c == 2:
            a = 1
        else:
            a = -1
        i = r * c + (r - a) - 1
    elif r == 2:
        i = r * c + (r - c + 1) - 1
    else:
        i = r * c + (r - 1) - 1

    if list_board[i] != '.':
        bool_val = False
        return list_board, bool_val
    else:
        bool_val = True
        list_board[i] = current
        return list_board, bool_val


def check_win(list_board):
    bool_val = False
    winner = None

    rows_list = [0, 3, 6]
    for r in rows_list:
        right_i1 = r + 1
        right_i2 = r + 2

        if list_board[r] is list_board[right_i1] and list_board[r] is list_board[right_i2] and list_board[r] != '.':
            bool_val = True
            winner = list_board[r]

    cols_list = [0, 1, 2]
    for c in cols_list:
        down_i1 = c + 3
        down_i2 = c + 6

        if list_board[c] is list_board[down_i1] and list_board[c] is list_board[down_i2] and list_board[c] != '.':
            bool_val = True
            winner = list_board[c]

    if list_board[0] is list_board[4] and list_board[0] is list_board[8] and list_board[0] != '.':
        bool_val = True
        winner = list_board[0]

    if list_board[2] is list_board[4] and list_board[2] is list_board[6] and list_board[2] != '.':
        bool_val = True
        winner = list_board[2]

    return bool_val, winner


def check_draw(list_board):
    draw = False
    outcome, winner = check_win(list_board)
    if outcome is False:
        draw = True
    return draw


def play_game():
    board = initialise_board()
    current_turn = get_current_turn_number(board)
    if_win, winner = check_win(board)

    while current_turn < 10 and if_win is False:
        display_board(board)
        print("Current turn: ", + current_turn)
        current_player = get_current_player(board)
        print("Current player: ", current_player)

        input_r = int(input('Enter row number: '))
        input_c = int(input('Enter column number: '))

        board, valid_play = play_turn(board, input_r, input_c)
        if valid_play is True:
            if_win, winner = check_win(board)
            current_turn = get_current_turn_number(board)

    if current_turn == 10:
        if_draw = check_draw(board)
        if if_draw is True:
            print("Draw!")

    print('Winner: ', winner)
    print("Final board: ")
    display_board(board)


