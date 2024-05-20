# This project includes tictactoe functions

"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    xCounter = 0
    oCounter = 0
    
    for xAxis in board:
        for yAxis in xAxis:
            if yAxis == X:
                xCounter += 1

            elif yAxis == O:
                oCounter += 1

    if xCounter == oCounter:
        return X
    
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    myActions = set() # i created new set

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY: # if cell is empty 
                myActions.add((i, j)) # add this action to myActions
    return myActions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = [] # i created new board

    for row in board:
        newBoard.append(row[:])  # copy board 
    i = action[0]
    j = action[1]

    if newBoard[i][j] is not EMPTY:
        raise Exception("Problem occured. Please check function (result funtion)")
    
    newBoard[i][j] = player(board)
    return newBoard



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # xAxis check
    for xAxis in board:
        if xAxis[0] == xAxis[1] == xAxis[2]:
            if xAxis[0] is not EMPTY:
                return xAxis[0]

    # yAxis check
    for yAxis in range(3):
        if board[0][yAxis] == board[1][yAxis] == board[2][yAxis]:
            if board[0][yAxis] is not EMPTY:
                return board[0][yAxis]

    # cross check
    if board[0][0] == board[1][1] == board[2][2]:
        if  board[0][0] is not EMPTY:
            return board[0][0]
        
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] is not EMPTY:
            return board[0][2]

    else:
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # check if there is a winner
    if winner(board):
        return True
    
    # check empty cell
    for xAxis in board:
        for yAxis in xAxis:
            if yAxis is EMPTY:
                return False
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerSide = winner(board)
    
    if winnerSide == X:
        return 1
    elif winnerSide == O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    currentPlayer = player(board)
    
    if currentPlayer == X:
        bestValue = float('-inf') # mathematical minus infinity
    else:
        bestValue = float('inf') 
    
    # if there is no action (no bestValue)
    bestAction = None

    for action in actions(board):
        resultBoard = result(board, action)
        if currentPlayer == O:
            value = minValue(resultBoard)
        else:
            value = maxValue(resultBoard)
        
        if currentPlayer == X:
            if value > bestValue:
                bestValue = value
                bestAction = action
        else:
            if value < bestValue:
                bestValue = value
                bestAction = action

    return bestAction

def minValue(board):
    if terminal(board):
        return utility(board)
    
    minValue = float('inf')
    for action in actions(board):
        resultBoard = result(board, action)
        maxResult = maxValue(resultBoard)
        minValue = min(minValue, maxResult)
    
    return minValue

def maxValue(board):
    if terminal(board):
        return utility(board)
    
    maxValue = float('-inf')
    for action in actions(board):
        resultBoard = result(board, action)
        minResult = minValue(resultBoard)
        maxValue = max(maxValue, minResult)
    
    return maxValue
