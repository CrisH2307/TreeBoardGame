# Main Author: Sean Muniz, Cris Huynh
# Main Reviewer: Cris Hunyh

from overflow import *
from s_q import * 

# This function duplicates and returns the board. You may find this useful
def copy_board(board):
        current_board = []
        height = len(board)
        for i in range(height):
            current_board.append(board[i].copy())
        return current_board

# this function is your evaluation function for the board
def evaluate_board (board, player):
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0

    p1_score = 0
    p2_score = 0

    for r in range(rows):
        for c in range(cols):

                # add a score for player 1 if cell is more than 0
            if board[r][c] >= 0: 
                p1_score += board[r][c]

                # add a score player -1 if cell is less than 0
            elif board[r][c] <= 0: 
                p2_score += abs(board[r][c])

    # if player 2 has lost, make player 1's score 100
    if p2_score == 0:
        p1_score = 100
    
    # same from top but vice versa
    elif p1_score == 0: 
        p2_score = 100

    # the above conditions must be done since the winning score should be the same
    # for both players 

    # return the score depending on the player 
    if player == 1: 
        return p1_score
    else:
        return p2_score
            
class GameTree:
    class Node:
        def __init__(self, board, depth, player,score, tree_height = 4):
            self.board = copy_board(board)
            self.depth = depth
            self.player = player
            self.tree_height = tree_height
            self.children = []
            self.score = score

    def __init__(self, board, player, tree_height = 4):
        self.player = player
        self.board = copy_board(board)
        self.tree_height = tree_height
        self.root = self.Node(board, 0, player, tree_height)
        # This will store all the moves into a list
        all_moves = [self.root]
        # store overflow steps
        a_queue = Queue()
        while all_moves: 
            curr = all_moves.pop()
            # funtion finishes if the height is 0. 
            if curr.tree_height == 0: 
                return 
            # generate all valid moves
            for r in range(len(curr.board)):
                for c in range(len(curr.board[r])):
                    new_board = copy_board(curr.board)
                    if player == 1 and curr.board[r][c] >= 0: 
                        new_board[r][c] += player

                        # check if the board overflows
                        # this will also modify the board
                        result = overflow(new_board, a_queue)

                    elif player == -1 and curr.board[r][c] <= 0: 
                        new_board[r][c] += player
                        # check if the board overflows
                        # this will also modify the board
                        result = overflow(new_board, a_queue)
                    # create a child node only if the move is valid. 
                    # if the move is valid, it will not be the same as the root. 
                    next_player = -curr.player 
                    if curr.board[r][c] != new_board[r][c]:
                        # check to see if there is a winner. If there is we exit this function. 
                        score = evaluate_board(new_board, curr.player)
                        child_node = self.Node(new_board, curr.depth +1, next_player,score, curr.tree_height - 1)
                        curr.children.append(child_node)
                        all_moves.append(child_node)
            for move in all_moves: 
                if move.score == 100:
                    return

    def get_move(self):
        height = len(self.board)
        width = len(self.board[0])
        p1_best_score = 0
        p1_pos = (0,0)
        p2_best_score = 0
        p2_pos = (0,0)
        row_cntr = -1
        row = 0
        col = -1

        all_moves = [self.root]

        while all_moves: 
            
            curr = all_moves.pop(0)

            if row_cntr == height:
                row += 1
            if col == width: 
                col = 0

            if self.player == 1: 
                if curr.score > p1_best_score: 
                    p1_best_score = curr.score
                    p1_pos = (row, col)
            elif self.player == -1: 
                if curr.score > p2_best_score:
                    p2_best_score = curr.score
                    p2_pos = (row, col)
        
            for child in curr.children: 
                all_moves.append(child)
            
            row_cntr += 1
            col += 1
            
        return p1_pos if self.player == 1 else p2_pos





    
   
    def clear_tree(self):
        # Delete a tree
        # Loop through all the children of the root node
        # Recursively clear the child nodes
        # Break reference to grandchildren
        # Clear child references
        if self.root:
            for child in self.root.children:
                if child.children:
                    for gc in child.children:
                        gc.children = []
                child.children = []

        self.root.children = []
        self.root = None
