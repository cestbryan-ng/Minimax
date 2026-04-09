"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_count, O_count = 0, 0
    for row in board:
        X_count += row.count(X)
        O_count += row.count(O)
    return O if X_count > O_count else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                available.add((i, j))
    return available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception(
            "Invalid action: the space is already occupied or outside the board"
        )

    board = deepcopy(board)
    player_, (i, j) = player(board), action
    board[i][j] = player_
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] is not None:
        player = board[1][1]
        return player
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] is not None:
        player = board[1][1]
        return player

    for row in board:
        if len(set(row)) == 1 and row[0] is not None:
            player = row[0]
            return player

    for column in zip(*board):
        if len(set(column)) == 1 and column[0] is not None:
            player = column[0]
            return player

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in (X, O):
        return True

    if len(actions(board)) == 0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1

    if winner(board) == "O":
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
