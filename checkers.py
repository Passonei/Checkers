import numpy as np
import sys
import time
import pygame
import math
import random
from agents import *

class Checkers():

    def __init__(self,ROWS_COUNT,show=True):
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

    def make_move(self,position):
        self.board[position[2]][position[3]] = self.board[position[0]][position[1]]
        self.board[position[0]][position[1]] = 0

    def capture(self,position):
        capture_move = []
        if self.turn == 1:
            oponent = 1
        else: oponent = 2

        for i in range(2):
            for pos in position:
                try:
                    if pos[1]==0 or pos[1]==1:
                        if self.board[pos[0]-1][pos[1]+1]==oponent and self.board[pos[0]-2][pos[1]+2]==0 and pos[0]!=0 and pos[0]!=1:
                            capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]+2])
                        if self.board[pos[0]+1][pos[1]+1]==oponent and self.board[pos[0]+2][pos[1]+2]==0 and pos[0]!=self.ROW_COUNT-1 and pos[0]!=self.ROW_COUNT-2:
                            capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]+2])
                        
                    elif pos[1]==self.ROW_COUNT-1 or pos[1]==self.ROW_COUNT-2:
                        if self.board[pos[0]-1][pos[1]-1]==oponent and self.board[pos[0]-2][pos[1]-2]==0 and pos[0]!=0 and pos[0]!=1:
                            capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]-2])
                        if self.board[pos[0]+1][pos[1]-1]==oponent and self.board[pos[0]+2][pos[1]-2]==0 and pos[0]!=self.ROW_COUNT-1 and pos[0]!=self.ROW_COUNT-2:
                            capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]-2])
                    
                    elif pos[0]==0 or pos[0]==1:
                        if self.board[pos[0]+1][pos[1]+1]==oponent and self.board[pos[0]+2][pos[1]+2]==0 and pos[1]!=self.ROW_COUNT-1 and pos[1]!=self.ROW_COUNT-2:
                            capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]+2])
                        if self.board[pos[0]+1][pos[1]-1]==oponent and self.board[pos[0]+2][pos[1]-2]==0 and pos[1]!=0 and pos[1]!=1:
                            capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]-2])

                    elif pos[0]==self.ROW_COUNT-1 or pos[0]==self.ROW_COUNT-2:
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
                    if len(pos)==4:
                        capture_move[-1][0]=pos[2]
                        capture_move[-1][1]=pos[3]
                        if capture_move[-1][0]-capture_move[-1][1] == capture_move[-1][2]-capture_move[-1][3] or capture_move[-1][0]+capture_move[-1][1] == capture_move[-1][2]+capture_move[-1][3]:
                            continue
                        else: capture_move.pop()
                except: continue
            oponent+=2
        return capture_move

    def normal_move(self,position):
        move = []
        for pos in position:
            try:
                if self.turn == 1 and pos[0]!=0:
                    if pos[1]==0:
                        if self.board[pos[0]-1][pos[1]+1]==0:
                            move.append([pos[0],pos[1],pos[0]-1,pos[1]+1])
                    elif pos[1]==self.ROW_COUNT-1:
                        if self.board[pos[0]-1][pos[1]-1]==0:
                            move.append([pos[0],pos[1],pos[0]-1,pos[1]-1])
                    else:
                        if self.board[pos[0]-1][pos[1]+1]==0:
                            move.append([pos[0],pos[1],pos[0]-1,pos[1]+1])
                        if self.board[pos[0]-1][pos[1]-1]==0:
                            move.append([pos[0],pos[1],pos[0]-1,pos[1]-1])
                if self.turn == 0:
                    if pos[1]==0:
                        if self.board[pos[0]+1][pos[1]+1]==0:
                            move.append([pos[0],pos[1],pos[0]+1,pos[1]+1])
                    elif pos[1]==self.ROW_COUNT-1:
                        if self.board[pos[0]+1][pos[1]-1]==0:
                            move.append([pos[0],pos[1],pos[0]+1,pos[1]-1])
                    else:
                        if self.board[pos[0]+1][pos[1]+1]==0:
                            move.append([pos[0],pos[1],pos[0]+1,pos[1]+1])
                        if self.board[pos[0]+1][pos[1]-1]==0:
                            move.append([pos[0],pos[1],pos[0]+1,pos[1]-1])
            except: continue
        return move

    def draw_board(self):
        screen = pygame.display.set_mode((self.ROW_COUNT*self.SQUARESIZE,self.ROW_COUNT*self.SQUARESIZE))
        radius = int(self.SQUARESIZE/2 - self.ROW_COUNT)
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

    def pieces(self):
        pos=[]
        king_pos=[]
        for row in range(self.ROW_COUNT):
            for col in range(self.ROW_COUNT):
                if self.board[row][col] == self.turn+1:
                    pos.append([row,col])
                if self.board[row][col] == self.turn+3:
                    king_pos.append([row,col])
        return pos, king_pos

    def capture_move(self,possible_capture):
        self.make_move(possible_capture)
        a=int((possible_capture[0]-possible_capture[2])/abs(possible_capture[0]-possible_capture[2]))
        b=int((possible_capture[1]-possible_capture[3])/abs(possible_capture[1]-possible_capture[3]))
        self.board[possible_capture[2]+a][possible_capture[3]+b] = 0
        new_position = [possible_capture[2:]]
        if len(self.capture(new_position))!=0:
            if self.show == True:
                self.draw_board()
                time.sleep(0.2)
            return self.capture_move(self.capture(new_position)[0])

    def change_to_king(self):
        self.board[0] = np.where(self.board[0]==2,4,self.board[0])
        self.board[-1] = np.where(self.board[-1]==1,3,self.board[-1])

    def rotate_diagonal(self,direction):
        if direction == 0: return [1,1]
        elif direction == 1: return [1,-1]
        elif direction == 2: return [-1,-1]
        else:  return [-1,1]

    def diagonal(self,position,c):
        diagonal=[]
        row = position[0]
        col = position[1]
        while 0 <= row <= self.ROW_COUNT-1 and 0 <= col <= self.ROW_COUNT-1:
            if [row,col]!= position:
                diagonal.append([row,col])
            row+=c[0]
            col+=c[1]
        return diagonal

    def kings_move(self,king_pos):
        normal_king_move=[]
        jump_move=[]
        for pos in king_pos:
            for direction in range(4):
                c = self.rotate_diagonal(direction)
                position_on_diagonal = self.diagonal(pos,c)
                for pos1, pos2 in position_on_diagonal:
                    if self.board[pos1,pos2]==0:
                        normal_king_move.append([pos[0],pos[1],pos1,pos2]) 
                    else:
                        jump_move.append([pos1-c[0],pos2-c[1],pos[0],pos[1]]) 
                        break
        return normal_king_move, jump_move

    def who_won(self,positions,kings_positions):
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
        return move

    def play_vs_agent(self,player_turn,agent):
        if player_turn == 1:
            first_player = 'player'
            second_player = agent
        else:
            first_player = agent
            second_player = player

        pygame.init()
        self.draw_board()
        it=1

        while True:
            positions, kings_positions = self.pieces()
            
            kings_moves, long_capture_position = self.kings_move(kings_positions)
            normal_moves = self.normal_move(positions)

            capture_normal = self.capture(positions+kings_positions)
            long_capture = self.capture(long_capture_position)
            capture = capture_normal + long_capture
            
            if len(positions+kings_positions)==0 or len(normal_moves+kings_moves+capture)==0:
                winner = self.who_won(positions,kings_positions)
                break

            if self.turn==1:
                agent = first_player
            else:
                agent = second_player

            if agent == agent_heuristic_one_step or agent == agent_minmax:
                param = self.board
            elif agent == agent_ten_random_games:
                param = self
            else:
                param = self.turn

            if agent == 'player':
                player_move = [0,0,0,0]
                if len(capture)==0:
                    while not(player_move in normal_moves):
                        player_move = self.player_choose_move()
                    self.make_move(player_move)
                else:
                    while not(player_move in capture):
                        player_move = self.player_choose_move()
                    self.capture_move(player_move)
                
            else:
                if len(capture)==0:
                    move = agent(normal_moves, kings_moves,param)
                    self.make_move(move)
                else:
                    move = agent(capture,[],param)
                    self.capture_move(move)

            self.change_to_king()
            self.draw_board()

            self.turn += 1
            self.turn = self.turn % 2
            time.sleep(0.3)

            it += 1
        
        if self.turn == 1:
            winner = 'Black'
        else:
            winner = 'White'

        return winner, it

    def play(self,agent_white,agent_black):
        if self.show==True:
            pygame.init()
            self.draw_board()
        it=1
        first_move=[]
        
        while True:
            positions, kings_positions = self.pieces()
            
            kings_moves, long_capture_position = self.kings_move(kings_positions)
            normal_moves = self.normal_move(positions)

            capture_normal = self.capture(positions+kings_positions)
            long_capture = self.capture(long_capture_position)
            capture = capture_normal + long_capture
            
            if len(positions+kings_positions)==0 or len(normal_moves+kings_moves+capture)==0:
                winner = self.who_won(positions,kings_positions)
                break

            if self.turn==1:
                agent = agent_white
            else:
                agent = agent_black

            if agent == agent_heuristic_one_step or agent == agent_minmax:
                param = self.board
            elif agent == agent_ten_random_games:
                param = self
            else:
                param = self.turn


            if len(capture)==0:
                move = agent(normal_moves, kings_moves,param)
                self.make_move(move)
            else:
                move = agent(capture,[],param)
                self.capture_move(move)

            if it==1:
                first_move = move

            self.change_to_king()

            if self.show == True:
                self.draw_board()
                time.sleep(0.3)

            self.turn += 1
            self.turn = self.turn % 2

            it += 1
        
        if self.turn == 1:
            winner = 'Black'
        else:
            winner = 'White'

        return winner, it, first_move

# game = Checkers(8)
# winner = game.play(agent_ten_random_games,agent_heuristic_one_step)
# print(winner[:2])
