from copy import deepcopy
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Parameters explained
# position:  will stand for the current position which is board object
# depth: how far is the tree extending, this will be a recursive call and will decrement
# max_player: boolean value are we maxing or minning, so true = max
# game: is the game object 

def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')   #implicitly -inf will be the lowest to compare
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]  #recursive call
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move 
    else: 
        minEval = float('+inf')   #implicitly -inf will be the lowest to compare
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]  #recursive call
            minEval = max(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move 



def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

def get_all_moves(board, color, game):
    moves = []    #going to store the new board like [[board, piece], [new_board, piece]]
    
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        #(row, col):[pieces]
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board  = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board) 

    return moves 