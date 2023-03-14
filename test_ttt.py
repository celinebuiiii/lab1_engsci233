import pytest
from functions_ttt import *


def test_check_game_win_tricky_board():
    board = ['O', 'O', 'X', 'O', 'X', 'X', 'X', '.', '.']
    is_win, player = check_win(board)
    assert(player == 'X')
    # PASSED IN 0.02s

