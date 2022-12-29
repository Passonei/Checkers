import random
import numpy as np

class agent_one_step_heuristic:
    def __init__(self, weight=[1, -10, 100, 1, 2], ROW_COUNT=8):
        self.weight = np.array(weight)
        self.ROW_COUNT = ROW_COUNT 
        # num_of: possible_capture, possible_capture_oponent, get_king, pieces, kings
    def king_upgrade(self, board, turn):
        sum = 0
        if turn == 1:
            sign = 1
        else: 
            sign = -1

        if np.any(board[0] == 2):
            sum += sign
        if np.any(board[-1] == 1):
            sum -= 2*sign
        return sum

    def positions(self, board, turn):
        pos = []
        king_pos = []

        for row in range(len(board)):
            for col in range(len(board)):

                if board[row][col] == turn+1:
                    pos.append([row,col])

                if board[row][col] == turn+3:
                    king_pos.append([row,col])

        return pos, king_pos

    def captures(self, board, position, turn):
        capture_move = []
        
        if turn == 1:
            oponent = 1
        else: 
            oponent = 2 
        
        pos, king_pos = self.positions(board, turn)
        position = pos + king_pos

        for i in range(2):
            for pos in position:
                try:
                    if pos[1]==0 or pos[1]==1: #capture at the left wall
                        if (board[pos[0]-1][pos[1]+1]==oponent and 
                            board[pos[0]-2][pos[1]+2]==0 and 
                            pos[0]!=0 and pos[0]!=1):

                            capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]+2])

                        if (board[pos[0]+1][pos[1]+1]==oponent and 
                            board[pos[0]+2][pos[1]+2]==0 and 
                            pos[0]!=self.ROW_COUNT-1 and pos[0]!=self.ROW_COUNT-2):

                            capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]+2])
                            
                    elif pos[1] == self.ROW_COUNT-1 or pos[1] == self.ROW_COUNT-2: #capture at the right wall
                        if (board[pos[0]-1][pos[1]-1]==oponent and 
                            board[pos[0]-2][pos[1]-2]==0 and 
                            pos[0]!=0 and pos[0]!=1):

                            capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]-2])

                        if (board[pos[0]+1][pos[1]-1]==oponent and 
                            board[pos[0]+2][pos[1]-2]==0 and 
                            pos[0]!=self.ROW_COUNT-1 and pos[0]!=self.ROW_COUNT-2):

                            capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]-2])
                        
                    elif pos[0]==0 or pos[0]==1: #capture at the top wall
                        if (board[pos[0]+1][pos[1]+1]==oponent and 
                            board[pos[0]+2][pos[1]+2]==0 and 
                            pos[1]!=self.ROW_COUNT-1 and pos[1]!=self.ROW_COUNT-2):

                            capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]+2])

                        if (board[pos[0]+1][pos[1]-1]==oponent and 
                            board[pos[0]+2][pos[1]-2]==0 and 
                            pos[1]!=0 and pos[1]!=1):

                            capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]-2])

                    elif pos[0] == self.ROW_COUNT-1 or pos[0] == self.ROW_COUNT-2: #capture at the bottom wall
                        if (board[pos[0]-1][pos[1]+1]==oponent and 
                            board[pos[0]-2][pos[1]+2]==0 and 
                            pos[1]!=self.ROW_COUNT-1 and pos[1]!=self.ROW_COUNT-2):

                            capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]+2])

                        if (board[pos[0]-1][pos[1]-1]==oponent and 
                            board[pos[0]-2][pos[1]-2]==0 and 
                            pos[1]!=0 and pos[1]!=1):

                            capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]-2])
                            
                    else:
                        if (board[pos[0]-1][pos[1]+1]==oponent and 
                            board[pos[0]-2][pos[1]+2]==0):

                            capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]+2])

                        if (board[pos[0]-1][pos[1]-1]==oponent and 
                            board[pos[0]-2][pos[1]-2]==0):

                            capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]-2])

                        if (board[pos[0]+1][pos[1]+1]==oponent and 
                            board[pos[0]+2][pos[1]+2]==0):

                            capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]+2])

                        if (board[pos[0]+1][pos[1]-1]==oponent and 
                            board[pos[0]+2][pos[1]-2]==0):

                            capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]-2])
                    
                    num_of_new_capture = len(capture_move) - num_of_capture
                    remove_list = []
                        
                    if len(pos) == 4 and (num_of_new_capture > 0):
                        for i in range(1,num_of_new_capture+1):
                            capture_move[-i][0] = pos[2]
                            capture_move[-i][1] = pos[3]

                            if (capture_move[-i][0]-capture_move[-i][1] == capture_move[-i][2]-capture_move[-i][3] or 
                                capture_move[-i][0]+capture_move[-i][1] == capture_move[-i][2]+capture_move[-i][3]):
                                pass
                            else:
                                remove_list.append(capture_move[-i])
                            
                        for remove in remove_list:
                            del capture_move[capture_move.index(remove)]
                    num_of_capture = len(capture_move)    
                except: continue
            oponent+=2
        return capture_move

    def make_move(self, board, position, turn):
        board[position[2]][position[3]] = board[position[0]][position[1]]
        board[position[0]][position[1]] = 0

        a=int((position[0]-position[2])/abs(position[0]-position[2]))
        b=int((position[1]-position[3])/abs(position[1]-position[3]))

        if (abs(position[0]-position[2])!=1 and board[position[2]+a][position[3]+b]!=0):
            board[position[2]+a][position[3]+b] = 0
            new_position = [position[2:]]

            if len(self.captures(board,new_position,turn)) != 0:
                return self.make_move(board, self.captures(board, new_position, turn)[0], turn)
        return board

    def get_heuristic(self, board, move):
        turn = board[move[2]][move[3]]-1

        possible_capture = self.captures(board, move, turn)

        if turn == 0: enemy_turn = 1
        else: enemy_turn = 0 
        
        possible_capture_oponent = self.captures(board, move, enemy_turn)

        get_king = self.king_upgrade(board, turn)

        num_of_pieces, num_of_kings = self.positions(board, turn)

        points = np.array((len(possible_capture), len(possible_capture_oponent), get_king, len(num_of_pieces), len(num_of_kings)))

        score = np.matmul(points, self.weight)
        return score

    def score_move(self, board, move):
        turn = board[move[0]][move[1]]-1
        next_board = self.make_move(np.copy(board), move, turn)
        score = self.get_heuristic(next_board, move)
        return score

    def decision(self, all_moves, board):
        scores = dict(zip(np.arange(len(all_moves)), [self.score_move(board, move) for move in all_moves]))
        max_score = [key for key in scores.keys() if scores[key] == max(scores.values())]
        return all_moves[random.choice(max_score)]
