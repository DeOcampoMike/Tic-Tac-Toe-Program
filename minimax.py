from checkwinner import check_winner
from variable import *

def minimax(minimaxboard, depth, is_maximizing):
    import variable
    import Tileset

    if Tileset.currplayer == "O":
        return float('inf')
        

    elif Tileset.currplayer == "X":
        return float('-inf')
    
    elif variable.turn == 9:
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
    best_move = (-1, -1)  
    for row in range(3):
        for column in range(3):
            if Tileset.board[row][column]["text"] == "":  
                Tileset.board[row][column]["text"] = "O"  
                score = minimax(Tileset.board, 0, False)
                Tileset.board[row][column]["text"] = ""  

                if score > best_score: 
                    best_score = score
                    best_move = (row, column)

    return best_move  
