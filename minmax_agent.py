import random
import numpy as np
from checkers import Checkers
from heuristic_agent import agent_one_step_heuristic

class agent_minmax(agent_one_step_heuristic,Checkers):
    def __init__(self, ROWS_COUNT=8, n_steps=3, weight=[10, 50, -4, -50, -20, 0]):
        # num_of: pieces, kings, pieces_oponent, kings_oponent
        self.n_steps = n_steps
        self.weight = np.array(weight)
        self.ROW_COUNT = ROWS_COUNT

    def is_terminal(self, board, turn):
        position, king_position = self.positions(board, turn)
        if len(position + king_position) == 0:
            return True
        else: 
            return False

    def kings_move(self, board, king_pos):
        normal_king_move = []
        jump_move = []

        for pos in king_pos:
            for direction in range(4):
                change_diagonal = self.rotate_diagonal(direction)
                position_on_diagonal = self.diagonal(pos, change_diagonal)

                for pos1, pos2 in position_on_diagonal:
                    if board[pos1,pos2] != 0:
                        jump_move.append([pos1-change_diagonal[0], pos2-change_diagonal[1], pos[0], pos[1]]) 
                        break
                    elif [pos1, pos2] == position_on_diagonal[-1] and [pos1, pos2] != pos:
                        jump_move.append([pos1, pos2, pos[0], pos[1]]) 
                        break
                    else:
                        normal_king_move.append([pos[0], pos[1], pos1, pos2]) 
        return normal_king_move, jump_move

    def normal_move(self, board, position, turn):
        move = []
        for pos in position:
            try:
                if turn == 1 and pos[0]!=0:
                    if pos[1]==0:
                        if board[pos[0]-1][pos[1]+1]==0:
                            move.append([pos[0],pos[1],pos[0]-1,pos[1]+1])

                    elif pos[1]==7:
                        if board[pos[0]-1][pos[1]-1]==0:
                            move.append([pos[0],pos[1],pos[0]-1,pos[1]-1])

                    else:
                        if board[pos[0]-1][pos[1]+1]==0:
                            move.append([pos[0],pos[1],pos[0]-1,pos[1]+1])

                        if board[pos[0]-1][pos[1]-1]==0:
                            move.append([pos[0],pos[1],pos[0]-1,pos[1]-1])

                if turn == 0:
                    if pos[1]==0:
                        if board[pos[0]+1][pos[1]+1]==0:
                            move.append([pos[0],pos[1],pos[0]+1,pos[1]+1])

                    elif pos[1]==7:
                        if board[pos[0]+1][pos[1]-1]==0:
                            move.append([pos[0],pos[1],pos[0]+1,pos[1]-1])

                    else:
                        if board[pos[0]+1][pos[1]+1]==0:
                            move.append([pos[0],pos[1],pos[0]+1,pos[1]+1])

                        if board[pos[0]+1][pos[1]-1]==0:
                            move.append([pos[0],pos[1],pos[0]+1,pos[1]-1])
            except: continue
        return move

    def valid_moves(self, board, turn):
        positions, kings_positions = self.positions(board, turn)
                
        kings_moves, long_capture_position = self.kings_move(board,kings_positions)
        normal_moves = self.normal_move(board,positions,turn)

        capture_normal = self.captures(board,positions,turn)
        long_capture = self.captures(board,long_capture_position,turn)
        capture_moves = capture_normal + long_capture

        if len(capture_moves)!=0:
            return capture_moves
        else:
            return normal_moves+kings_moves

    def minmax(self, board, move, depth, maximizing, turn, alpha, beta):
    
        if depth == 0 or not self.is_terminal:
            return self.get_heuristic_minmax(board, move, turn)
        
        turn += 1
        turn = turn %2

        valid = self.valid_moves(board, turn)

        if maximizing:
            value = -np.Inf
            for move in valid:
                next_board = self.make_move(np.copy(board), move, turn)
                value = max(value, self.minmax(next_board, move, depth-1, False, turn, alpha, beta))
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return value
        else:
            value = np.Inf
            for move in valid:
                next_board = self.make_move(np.copy(board),move,turn)
                value = min(value, self.minmax(next_board, move, depth-1, True, turn, alpha, beta))
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value

    def get_heuristic_minmax(self, board, move, turn):

        possible_capture = self.captures(board,move,turn)

        if turn == 0: 
            enemy_turn = 1
            c=3
        else: 
            enemy_turn = 0 
            c=4

        possible_capture_oponent = self.captures(board,move,enemy_turn)
    
        num_of_pieces, num_of_kings = self.positions(board, turn)
        num_of_pieces_oponent, num_of_kings_oponent = self.positions(board,enemy_turn)

        points = (np.array((len(num_of_pieces), len(num_of_kings), len(num_of_pieces_oponent), 
                    len(num_of_kings_oponent), len(possible_capture), len(possible_capture_oponent))))

        score = np.matmul(points, self.weight)
        return score

    def score_move_minmax(self, board,move,n_steps):
        turn = board[move[0]][move[1]]-1
        next_board = self.make_move(np.copy(board),move,turn)
        score = self.minmax(next_board, move, n_steps-1, False, turn, -np.Inf, np.Inf)
        return score

    def decision(self, all_moves, board):
        scores = dict(zip(np.arange(len(all_moves)), [self.score_move_minmax(board, move, self.n_steps) for move in all_moves]))
        max_score = [key for key in scores.keys() if scores[key] == max(scores.values())]
        return all_moves[random.choice(max_score)]
