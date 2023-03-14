import pytest
from functions_ttt import *


def test_check_get_current_turn():
    # Check for random turn number
    board = ['O', 'X', '.', '.', '.', 'X', 'O', '.', '.']
    turn_number = get_current_turn_number(board)
    assert(turn_number == 5)


def test_check_get_current_player():
    # Check for getting correct player
    board = ['X', 'O', '.', '.', '.', '.', '.', '.', '.']
    player = get_current_player(board)
    assert(player == 'X')


def test_check_invalid_play_turn():
    board = ['O', 'X', '.', '.', '.', 'X', '.', '.', '.']
    row_num = 2
    col_num = 3
    new_board, if_valid = play_turn(board, row_num, col_num)
    assert(if_valid is False)


def test_check_game_win_tricky_board():
    # Diagonal win from player X
    board = ['O', 'O', 'X', 'O', 'X', 'X', 'X', '.', '.']
    is_win, player = check_win(board)
    assert(player == 'X')
    # PASSED IN 0.02s


def test_check_game_draw():
    # Player O made a winning move
    board = ['O', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'X']
    is_draw = check_draw(board)
    assert(is_draw is False)

