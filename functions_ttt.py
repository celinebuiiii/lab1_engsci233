def initialise_board():
    """
        Initialise empty board at start of game as a 1D list
        No input required.

        Returns
        -----
        list_board : a list var to represent the board
        Notes
        -----
        List variable list_board has to contain 9 items of '.'
        in order to create a 3x3 tic tac toe board.
        No other pre- or post-conditions required.
    """

    list_board = ['.'] * 9
    return list_board


def display_board(list_board):
    """
        Print board to command window.
        No output variables.

        Arguments
        -----
        list_board : a list var to represent the board
        Notes
        -----
        The printed board must be a 3x3 square.
    """
    print(list_board[0], list_board[1], list_board[2])
    print(list_board[3], list_board[4], list_board[5])
    print(list_board[6], list_board[7], list_board[8])


def get_current_turn_number(list_board):
    """
        Go through list_board and count any X or O
        to find the current turn number.

        Arguments
        -----
        list_board : a list variable to represent the board
        Returns
        -----
        count : an integer var to
                indicate the current turn number

        Notes
        -----
        (pre-con 1) list_board must be a 1D list of length 9.
        (post-con 1) Count cannot be < 1 or > 10
    """
    count = 1
    empty_pos = '.'
    for i in list_board:
        if i is not empty_pos:
            count += 1
    return count


def get_current_player(list_board):
    """
        Go through list_board and compare
        numbers of X and 0 to find current player.

        Arguments
        -----
        list_board : a list var to represent the board
        Returns
        -----
        current_player : a string var for the current player

        Notes
        -----
        (pre-con 1) list_board must be a 1D list of length 9.
    """
    player_x = 0
    player_o = 0
    current_player = 'X'
    for i in list_board:
        if i == 'X':
            player_x += 1
        elif i == 'O':
            player_o += 1
    if player_x == 0 or player_o > player_x:
        current_player = 'X'
    return current_player


def play_turn(list_board, r, c):
    """
        Take inputs of row and column numbers from player,
        check if player's move is valid,
        then change the board accordingly to the move made.

        Arguments
        -----
        list_board : a list var to represent the board
        r : int var representing row number
        c : int var representing column number

        Returns
        -----
        list_board : a list var to represent the board
        bool_val : True if player's move is valid
                   False if player's move is invalid

        Notes
        -----
        (pre-con 1) r must be within 1-3 inclusive
        (pre-con 2) c must be within 1-3 inclusive
    """
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
    """
        Check if a player wins after a move is made.

        Arguments
        -----
        list_board : a list var to represent the board

        Returns
        -----
        winner : a string var to represent the winner
        bool_val : True if a player has won
                   False otherwise
    """
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
    """
        Check if the game concludes in a draw.

        Arguments
        -----
        list_board : a list var to represent the board

        Returns
        -----
        draw : True if all possible moves have been made but no winner
               False if a winning move has been made
    """
    draw = False
    outcome, winner = check_win(list_board)
    if outcome is False:
        draw = True
    return draw


def play_game():
    """
        Play the game from start to finish.
        No inputs or outputs required.
    """
    # might be an error in here somewhere
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


