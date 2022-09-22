import numpy as np
import sys
import time
import pygame
import math
import random
from agents import *

class Checkers():

    def __init__(self, ROWS_COUNT, show=True):
        self.ROW_COUNT = ROWS_COUNT
        self.SQUARESIZE = 50
        self.BLACK = pygame.Color('black')
        self.WHITE = pygame.Color('white')
        self.BISQUE = pygame.Color('bisque1')
        self.BROWN = pygame.Color('bisque3')
        self.turn = 1
        self.board = self.create_board()
        self.show = show

    def create_board(self):
        board = np.zeros((self.ROW_COUNT,self.ROW_COUNT))
        for col in range (self.ROW_COUNT):
            for row in range(int(self.ROW_COUNT/2) - 1):
                if (row+col) % 2 == 1:
                    board[row][col] = 1
            for row in range(int(self.ROW_COUNT/2) + 1,self.ROW_COUNT):
                if (row+col) % 2 == 1:
                    board[row][col] = 2
        return board

    def change_turn(self):
        self.turn += 1
        self.turn = self.turn % 2

    def make_move(self, position):
        self.board[position[2]][position[3]] = self.board[position[0]][position[1]]
        self.board[position[0]][position[1]] = 0
        a=int((position[0]-position[2])/abs(position[0]-position[2]))
        b=int((position[1]-position[3])/abs(position[1]-position[3]))
        if abs(position[0]-position[2])!=1 and self.board[position[2]+a][position[3]+b] != 0:
            self.board[position[2]+a][position[3]+b] = 0
            new_position = [position[2:]]
            if len(self.capture(new_position)) != 0:
                if self.show == True:
                    self.draw_board()
                    time.sleep(0.5)
                return self.make_move(self.capture(new_position)[0])

    def capture(self, position):
        capture_move = []
        num_of_capture = 0
        if self.turn == 1:
            oponent = 1
        else: oponent = 2

        for i in range(2):
            for pos in position:
                try:
                    if pos[1] == 0 or pos[1] == 1:
                        if self.board[pos[0]-1][pos[1]+1]==oponent and self.board[pos[0]-2][pos[1]+2]==0 and pos[0]!=0 and pos[0]!=1:
                            capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]+2])
                        if self.board[pos[0]+1][pos[1]+1]==oponent and self.board[pos[0]+2][pos[1]+2]==0 and pos[0]!=self.ROW_COUNT-1 and pos[0]!=self.ROW_COUNT-2:
                            capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]+2])
                        
                    elif pos[1] == self.ROW_COUNT-1 or pos[1] == self.ROW_COUNT-2:
                        if self.board[pos[0]-1][pos[1]-1]==oponent and self.board[pos[0]-2][pos[1]-2]==0 and pos[0]!=0 and pos[0]!=1:
                            capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]-2])
                        if self.board[pos[0]+1][pos[1]-1]==oponent and self.board[pos[0]+2][pos[1]-2]==0 and pos[0]!=self.ROW_COUNT-1 and pos[0]!=self.ROW_COUNT-2:
                            capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]-2])
                    
                    elif pos[0] == 0 or pos[0] == 1:
                        if self.board[pos[0]+1][pos[1]+1]==oponent and self.board[pos[0]+2][pos[1]+2]==0 and pos[1]!=self.ROW_COUNT-1 and pos[1]!=self.ROW_COUNT-2:
                            capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]+2])
                        if self.board[pos[0]+1][pos[1]-1]==oponent and self.board[pos[0]+2][pos[1]-2]==0 and pos[1]!=0 and pos[1]!=1:
                            capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]-2])

                    elif pos[0] == self.ROW_COUNT-1 or pos[0] == self.ROW_COUNT-2:
                        if self.board[pos[0]-1][pos[1]+1]==oponent and self.board[pos[0]-2][pos[1]+2]==0 and pos[1]!=self.ROW_COUNT-1 and pos[1]!=self.ROW_COUNT-2:
                            capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]+2])
                        if self.board[pos[0]-1][pos[1]-1]==oponent and self.board[pos[0]-2][pos[1]-2]==0 and pos[1]!=0 and pos[1]!=1:
                            capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]-2])
                        
                    else:
                        if self.board[pos[0]-1][pos[1]+1]==oponent and self.board[pos[0]-2][pos[1]+2]==0:
                            capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]+2])
                        if self.board[pos[0]-1][pos[1]-1]==oponent and self.board[pos[0]-2][pos[1]-2]==0:
                            capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]-2])
                        if self.board[pos[0]+1][pos[1]+1]==oponent and self.board[pos[0]+2][pos[1]+2]==0:
                            capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]+2])
                        if self.board[pos[0]+1][pos[1]-1]==oponent and self.board[pos[0]+2][pos[1]-2]==0:
                            capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]-2])
                    
                    num_of_new_capture = len(capture_move) - num_of_capture
                    remove_list = []
                    
                    if len(pos) == 4 and (num_of_new_capture > 0):
                        for i in range(1,num_of_new_capture+1):
                            capture_move[-i][0] = pos[2]
                            capture_move[-i][1] = pos[3]
                            if capture_move[-i][0]-capture_move[-i][1] == capture_move[-i][2]-capture_move[-i][3] or capture_move[-i][0]+capture_move[-i][1] == capture_move[-i][2]+capture_move[-i][3]:
                                pass
                            else:
                                remove_list.append(capture_move[-i])
                        
                        for remove in remove_list:
                            del capture_move[capture_move.index(remove)]
                    num_of_capture = len(capture_move)
                except: continue
            oponent += 2
        return capture_move

    def normal_move(self, position):
        move = []
        for pos in position:
            try:
                if self.turn == 1 and pos[0] != 0:
                    if pos[1] == 0:
                        if self.board[pos[0]-1][pos[1]+1] == 0:
                            move.append([pos[0],pos[1],pos[0]-1,pos[1]+1])
                    elif pos[1] == self.ROW_COUNT-1:
                        if self.board[pos[0]-1][pos[1]-1] == 0:
                            move.append([pos[0],pos[1],pos[0]-1,pos[1]-1])
                    else:
                        if self.board[pos[0]-1][pos[1]+1] == 0:
                            move.append([pos[0],pos[1],pos[0]-1,pos[1]+1])
                        if self.board[pos[0]-1][pos[1]-1] == 0:
                            move.append([pos[0],pos[1],pos[0]-1,pos[1]-1])
                if self.turn == 0:
                    if pos[1] == 0:
                        if self.board[pos[0]+1][pos[1]+1] == 0:
                            move.append([pos[0],pos[1],pos[0]+1,pos[1]+1])
                    elif pos[1] == self.ROW_COUNT-1:
                        if self.board[pos[0]+1][pos[1]-1] == 0:
                            move.append([pos[0],pos[1],pos[0]+1,pos[1]-1])
                    else:
                        if self.board[pos[0]+1][pos[1]+1] == 0:
                            move.append([pos[0],pos[1],pos[0]+1,pos[1]+1])
                        if self.board[pos[0]+1][pos[1]-1] == 0:
                            move.append([pos[0],pos[1],pos[0]+1,pos[1]-1])
            except: continue
        return move

    def draw_board(self):
        screen = pygame.display.set_mode((self.ROW_COUNT*self.SQUARESIZE,(self.ROW_COUNT+1)*self.SQUARESIZE))
        radius = int(self.SQUARESIZE/2 - self.ROW_COUNT)

        pygame.display.set_caption('Checkers')
        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans MS', 16)
        text_agent_white = font.render(f'White -  {self.agent_white}', True, self.WHITE)
        text_agent_black = font.render(f'Black   -  {self.agent_black}', True, self.WHITE)
        screen.blit(text_agent_white, (0, (self.ROW_COUNT) * self.SQUARESIZE))
        screen.blit(text_agent_black, (0, (self.ROW_COUNT + 0.5) * self.SQUARESIZE))

        for row in range(self.ROW_COUNT):
            for col in range(self.ROW_COUNT):
                if (row+col) % 2 == 0:
                    pygame.draw.rect(screen, self.BISQUE, (col*self.SQUARESIZE, row*self.SQUARESIZE,self.SQUARESIZE,self.SQUARESIZE))
                else:
                    pygame.draw.rect(screen, self.BROWN, (col*self.SQUARESIZE, row*self.SQUARESIZE,self.SQUARESIZE,self.SQUARESIZE))

        for row in range(self.ROW_COUNT):
            for col in range(self.ROW_COUNT):
                if self.board[row][col] == 1:
                    pygame.draw.circle(screen, self.BLACK, (int(col*self.SQUARESIZE+self.SQUARESIZE/2), int(row*self.SQUARESIZE+self.SQUARESIZE/2)),radius)
                if self.board[row][col] == 2:
                    pygame.draw.circle(screen, self.WHITE, (int(col*self.SQUARESIZE+self.SQUARESIZE/2), int(row*self.SQUARESIZE+self.SQUARESIZE/2)),radius)
                if self.board[row][col] == 3:
                    pygame.draw.circle(screen, self.BLACK, (int(col*self.SQUARESIZE+self.SQUARESIZE/2), int(row*self.SQUARESIZE+self.SQUARESIZE/2)),radius)
                    pygame.draw.circle(screen, self.BROWN, (int(col*self.SQUARESIZE+self.SQUARESIZE/2), int(row*self.SQUARESIZE+self.SQUARESIZE/2)),radius/2)
                if self.board[row][col] == 4:
                    pygame.draw.circle(screen, self.WHITE, (int(col*self.SQUARESIZE+self.SQUARESIZE/2), int(row*self.SQUARESIZE+self.SQUARESIZE/2)),radius)
                    pygame.draw.circle(screen, self.BROWN, (int(col*self.SQUARESIZE+self.SQUARESIZE/2), int(row*self.SQUARESIZE+self.SQUARESIZE/2)),radius/2)
        pygame.display.update()

    def pieces(self,):
        # x, y = np.where(self.board == t+1)
        # pos = list(zip(x,y))
        # xk, yk = np.where(self.board == t+3)
        # king_pos = list(zip(xk, yk))
        pos = []
        king_pos = []
        for row in range(self.ROW_COUNT):
            for col in range(self.ROW_COUNT):
                if self.board[row][col] == self.turn+1:
                    pos.append([row,col])
                if self.board[row][col] == self.turn+3:
                    king_pos.append([row,col])
        return pos, king_pos

    def valid_moves(self, positions, kings_positions):
        kings_moves, long_capture_position = self.kings_move(kings_positions)
        normal_moves = self.normal_move(positions)
        not_capture_moves = normal_moves + kings_moves

        capture_normal = self.capture(positions+kings_positions)
        long_capture = self.capture(long_capture_position)
        capture = capture_normal + long_capture
        if len(capture) == 0:
            return not_capture_moves
        else:
            return capture 

    def change_to_king(self):
        self.board[0] = np.where(self.board[0]==2,4,self.board[0])
        self.board[-1] = np.where(self.board[-1]==1,3,self.board[-1])

    def rotate_diagonal(self, direction):
        if direction == 0: return [1,1]
        elif direction == 1: return [1,-1]
        elif direction == 2: return [-1,-1]
        else:  return [-1,1]

    def diagonal(self, position, change_diagonal):
        diagonal = []
        row = position[0]
        col = position[1]
        while 0 <= row <= self.ROW_COUNT-1 and 0 <= col <= self.ROW_COUNT-1:
            if [row,col] != position:
                diagonal.append([row,col])
            row += change_diagonal[0]
            col += change_diagonal[1]
        return diagonal

    def kings_move(self, king_pos):
        normal_king_move = []
        jump_move = []
        for pos in king_pos:
            for direction in range(4):
                change_diagonal = self.rotate_diagonal(direction)
                position_on_diagonal = self.diagonal(pos, change_diagonal)
                for pos1, pos2 in position_on_diagonal:
                    if self.board[pos1,pos2] != 0:
                        jump_move.append([pos1-change_diagonal[0], pos2-change_diagonal[1], pos[0], pos[1]]) 
                        break
                    elif [pos1, pos2] == position_on_diagonal[-1] and [pos1, pos2] != pos:
                        jump_move.append([pos1, pos2, pos[0], pos[1]]) 
                        break
                    else:
                        normal_king_move.append([pos[0], pos[1], pos1, pos2]) 
        return normal_king_move, jump_move

    def who_won(self, positions, kings_positions):
        if len(positions+kings_positions)==0:
            if self.turn == 1:
                    winner = 'Black'
            else:
                    winner = 'White'
            return winner
        else:
            if self.turn == 2:
                    winner = 'Black'
            else:
                    winner = 'White'
            return winner

    def player_choose_move(self):
        move = []
        while len(move) < 4:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx = event.pos[0]
                    col = int(math.floor(posx/self.SQUARESIZE))
                    posy = event.pos[1]
                    row = int(math.floor(posy/self.SQUARESIZE))
                    move.append(row)
                    move.append(col)
                    if self.board[row][col] == (self.turn+1 or self.turn+3):
                        screen = pygame.display.set_mode((self.ROW_COUNT*self.SQUARESIZE,(self.ROW_COUNT+1)*self.SQUARESIZE))
                        radius = int(self.SQUARESIZE/2 - self.ROW_COUNT)
                        self.draw_board()
                        pygame.draw.circle(screen, self.WHITE, (int(col*self.SQUARESIZE+self.SQUARESIZE/2), int(row*self.SQUARESIZE+self.SQUARESIZE/2)),radius*20000)
                    
        return move

    def play_vs_agent(self, player_turn, agent):
        if player_turn == 1:
            first_player = 'player'
            second_player = agent
            self.agent_white = first_player
            self.agent_black = second_player.__name__
        else:
            first_player = agent
            second_player = 'player'
            self.agent_white = first_player.__name__
            self.agent_black = second_player

        pygame.init()
        self.draw_board()
        it=1

        while True:
            positions, kings_positions = self.pieces()
            valid_moves = self.valid_moves(positions, kings_positions)
            
            if len(positions + kings_positions) == 0 or len(valid_moves) == 0:
                winner = self.who_won(positions, kings_positions)
                break

            if self.turn == 1:
                agent = first_player
            else:
                agent = second_player

            if agent == agent_heuristic_one_step or agent == agent_minmax:
                param = self.board
            else:
                param = self.turn

            if agent == 'player':
                player_move = [0,0,0,0]
                while not(player_move in valid_moves):
                    player_move = self.player_choose_move()
                self.make_move(player_move)             
            else:
                move = agent(valid_moves, param)
                self.make_move(move)

            self.change_to_king()
            self.draw_board()

            self.change_turn()
            time.sleep(0.3)

            it += 1
        
        if self.turn == 1:
            winner = 'Black'
        else:
            winner = 'White'

        return winner, it

    def play(self, agent_white, agent_black):
        if self.show == True:
            self.agent_white = agent_white.__name__
            self.agent_black = agent_black.__name__
            pygame.init()
            self.draw_board()

        it=1
        
        while True:
            positions, kings_positions = self.pieces()
            valid_moves = self.valid_moves(positions, kings_positions)
            
            if len(positions + kings_positions) == 0 or len(valid_moves) == 0:
                winner = self.who_won(positions, kings_positions)
                break

            if self.turn==1:
                agent = agent_white
            else:
                agent = agent_black

            if agent == agent_heuristic_one_step or agent == agent_minmax:
                param = self.board
            else:
                param = self.turn

            move = agent(valid_moves, param)
            self.make_move(move)

            self.change_to_king()

            if self.show == True:
                self.draw_board()
                time.sleep(0.5)

            self.change_turn()

            it += 1
        
        if self.turn == 1:
            winner = 'Black'
        else:
            winner = 'White'

        return winner, it

game = Checkers(8) 
# winner = game.play_vs_agent(1, agent_minmax) 
winner = game.play(agent_minmax,agent_heuristic_one_step)
print(winner[:2])
