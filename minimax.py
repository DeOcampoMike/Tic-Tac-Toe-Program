from checkwinner import check_winner
from variable import *

def minimax(minimaxboard, depth, is_maximizing):
    import variable
    import twoplayer
    import Tileset

    if check_winner(Tileset.board, twoplayer.label2)and Tileset.currplayer == "O":
        return float('inf')

    elif check_winner(Tileset.board, twoplayer.label2) and Tileset.currplayer == "X":
        return float('-inf')
    
    elif check_winner(Tileset.board, twoplayer.label2) and variable.turn == 9:
        return 0

    if is_maximizing:
        best_score = -1000
        for row in range(3):
            for column in range(3):
                if minimaxboard[row][column] == "":  
                    minimaxboard[row][column] = "X"
                    score = minimax(minimaxboard, depth + 1, False)
                    minimaxboard[row][column] = ""  
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for row in range(3):
            for column in range(3):
                if minimaxboard[row][column] == "":
                    minimaxboard[row][column] = "O" 
                    score = minimax(minimaxboard, depth + 1, True)
                    minimaxboard[row][column] = ""  
                    best_score = min(score, best_score)
        return best_score
    
    

def best_move():
    import Tileset
    best_score = -1000
    best_move = (-1, -1)  # Initialize to an invalid position
    for row in range(3):
        for column in range(3):
            if Tileset.board[row][column]["text"] == "":  # Check if the cell is empty
                Tileset.board[row][column]["text"] = "O"  # Simulate AI move
                score = minimax(Tileset.board, 0, False)
                Tileset.board[row][column]["text"] = ""  # Undo the move

                if score > best_score:  # If this move is better, update best_move
                    best_score = score
                    best_move = (row, column)

    return best_move  # Return the best move found (always a tuple)
