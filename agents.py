import random
import numpy as np

def agent_random(normal_moves, turn):
    return random.choice(normal_moves)

def agent_first_left_piece(normal_moves, turn):
    return normal_moves[0]

def agent_last_row(normal_moves, turn):
    moves=[]

    if turn==1:
        last_row = normal_moves[-1][0]  
    else:
        last_row = normal_moves[0][0]

    for move in normal_moves:
            if move[0]==last_row:
                moves.append(move)

    return random.choice(moves)

def agent_first_row(normal_moves, turn):
    moves=[]

    if turn==1:
        first_row = normal_moves[0][0]  
    else:
        first_row = normal_moves[-1][0]

    for move in normal_moves:
        if move[0]==first_row:
            moves.append(move)

    return random.choice(moves)

##################

def score_move(board,move):
    turn = board[move[0]][move[1]]-1
    next_board = make_move(np.copy(board),move,turn)
    score = get_heuristic(next_board,move)
    return score

def make_move(board, position, turn):
    board[position[2]][position[3]] = board[position[0]][position[1]]
    board[position[0]][position[1]] = 0
    a=int((position[0]-position[2])/abs(position[0]-position[2]))
    b=int((position[1]-position[3])/abs(position[1]-position[3]))
    if abs(position[0]-position[2])!=1 and board[position[2]+a][position[3]+b] != 0:
        board[position[2]+a][position[3]+b] = 0
        new_position = [position[2:]]
        if len(capture(board,new_position,turn)) != 0:
            return make_move(board,capture(board,new_position,turn)[0],turn)
    return board

def num_of(board,turn):
    pos=[]
    king_pos=[]
    for row in range(8):
        for col in range(8):
            if board[row][col] == turn+1:
                pos.append([row,col])
            if board[row][col] == turn+3:
                king_pos.append([row,col])
    return pos, king_pos

def capture(board,position,turn):
    capture_move = []
    if turn == 1:
        oponent = 1
    else: 
        oponent = 2
        
    pos=[]
    king_pos=[]
    for row in range(8):
        for col in range(8):
            if board[row][col] == turn+1:
                pos.append([row,col])
            if board[row][col] == turn+3:
                king_pos.append([row,col])
    position = pos + king_pos

    for i in range(2):
        for pos in position:
            try:
                if pos[1]==0 or pos[1]==1:
                    if board[pos[0]-1][pos[1]+1]==oponent and board[pos[0]-2][pos[1]+2]==0 and pos[0]!=0 and pos[0]!=1:
                        capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]+2])
                    if board[pos[0]+1][pos[1]+1]==oponent and board[pos[0]+2][pos[1]+2]==0 and pos[0]!=ROW_COUNT-1 and pos[0]!=ROW_COUNT-2:
                        capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]+2])
                        
                elif pos[1]==7 or pos[1]==6:
                    if board[pos[0]-1][pos[1]-1]==oponent and board[pos[0]-2][pos[1]-2]==0 and pos[0]!=0 and pos[0]!=1:
                        capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]-2])
                    if board[pos[0]+1][pos[1]-1]==oponent and board[pos[0]+2][pos[1]-2]==0 and pos[0]!=ROW_COUNT-1 and pos[0]!=ROW_COUNT-2:
                        capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]-2])
                    
                elif pos[0]==0 or pos[0]==1:
                    if board[pos[0]+1][pos[1]+1]==oponent and board[pos[0]+2][pos[1]+2]==0 and pos[1]!=ROW_COUNT-1 and pos[1]!=ROW_COUNT-2:
                        capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]+2])
                    if board[pos[0]+1][pos[1]-1]==oponent and board[pos[0]+2][pos[1]-2]==0 and pos[1]!=0 and pos[1]!=1:
                        capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]-2])

                elif pos[0]==7 or pos[0]==6:
                    if board[pos[0]-1][pos[1]+1]==oponent and board[pos[0]-2][pos[1]+2]==0 and pos[1]!=ROW_COUNT-1 and pos[1]!=ROW_COUNT-2:
                        capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]+2])
                    if board[pos[0]-1][pos[1]-1]==oponent and board[pos[0]-2][pos[1]-2]==0 and pos[1]!=0 and pos[1]!=1:
                        capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]-2])
                        
                else:
                    if board[pos[0]-1][pos[1]+1]==oponent and board[pos[0]-2][pos[1]+2]==0:
                        capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]+2])
                    if board[pos[0]-1][pos[1]-1]==oponent and board[pos[0]-2][pos[1]-2]==0:
                        capture_move.append([pos[0],pos[1],pos[0]-2,pos[1]-2])
                    if board[pos[0]+1][pos[1]+1]==oponent and board[pos[0]+2][pos[1]+2]==0:
                        capture_move.append([pos[0],pos[1],pos[0]+2,pos[1]+2])
                    if board[pos[0]+1][pos[1]-1]==oponent and board[pos[0]+2][pos[1]-2]==0:
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
        oponent+=2
    return capture_move

def king_update(board,turn):
    a=0
    if turn==1:
        p = 1
    else: 
        p =- 1

    if np.any(board[0]==2):
        a += p
    if np.any(board[-1]==1):
        a -= 2*p
    return a

def get_heuristic(board,move):
    turn = board[move[2]][move[3]]-1

    possible_capture = capture(board,move,turn)

    if turn == 0: enemy_turn = 1
    else: enemy_turn = 0 
    
    possible_capture_oponent = capture(board,move,enemy_turn)

    get_king = king_update(board, turn)

    num_of_pieces, num_of_kings = num_of(board, turn)

    score = len(possible_capture) - 10*len(possible_capture_oponent) + 100*get_king + len(num_of_pieces) + len(num_of_kings)*2
    return score

def agent_heuristic_one_step(all_moves, board):
    scores = dict(zip(np.arange(len(all_moves)), [score_move(board,move) for move in all_moves]))
    max_score = [key for key in scores.keys() if scores[key] == max(scores.values())]
    return all_moves[random.choice(max_score)]

##################

def is_terminal(board,turn):
    position, king_position = num_of(board, turn)
    if len(positions+kings_position) == 0:
        return True
    else: 
        return False

def rotate_diagonal(direction):
    if direction == 0: return [1,1]
    elif direction == 1: return [1,-1]
    elif direction == 2: return [-1,-1]
    else:  return [-1,1]

def diagonal(position, change_diagonal):
    diagonal=[]
    row = position[0]
    col = position[1]
    while 0 <= row <= 7 and 0 <= col <= 7:
        if [row,col]!= position:
            diagonal.append([row,col])
        row += change_diagonal[0]
        col += change_diagonal[1]
    return diagonal

def kings_move(board, king_pos):
        normal_king_move = []
        jump_move = []
        for pos in king_pos:
            for direction in range(4):
                change_diagonal = rotate_diagonal(direction)
                position_on_diagonal = diagonal(pos, change_diagonal)
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

def normal_move(board,position,turn):
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

def valid_moves(board,turn):
    positions, kings_positions = num_of(board, turn)
            
    kings_moves, long_capture_position = kings_move(board,kings_positions)
    normal_moves = normal_move(board,positions,turn)

    capture_normal = capture(board,positions,turn)
    long_capture = capture(board,long_capture_position,turn)
    capture_moves = capture_normal + long_capture
    if len(capture_moves)!=0:
        return capture_moves
    else:
        return normal_moves+kings_moves

def get_heuristic_minmax(board,move,turn):

    possible_capture = capture(board,move,turn)

    if turn == 0: 
        enemy_turn = 1
        c=3
    else: 
        enemy_turn = 0 
        c=4

    possible_capture_oponent = capture(board,move,enemy_turn)

    num_of_pieces, num_of_kings = num_of(board, turn)
    num_of_pieces_oponent, num_of_kings_oponent = num_of(board,enemy_turn)

    score = len(num_of_pieces)*10 + len(num_of_kings)*50 - len(num_of_pieces_oponent)*c - len(num_of_kings_oponent)*50
    return score

def minmax(board, move, depth, maximizing, turn, alpha, beta):
    
    if depth == 0 or not is_terminal:
        return get_heuristic_minmax(board, move, turn)
    
    turn += 1
    turn = turn %2

    valid = valid_moves(board,turn)

    if maximizing:
        value = -np.Inf
        for move in valid:
            next_board = make_move(np.copy(board), move, turn)
            value = max(value, minmax(next_board, move, depth-1, False, turn, alpha, beta))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = np.Inf
        for move in valid:
            next_board = make_move(np.copy(board),move,turn)
            value = min(value, minmax(next_board, move, depth-1, True, turn, alpha, beta))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

def score_move_minmax(board,move,n_steps):
    turn = board[move[0]][move[1]]-1
    next_board = make_move(np.copy(board),move,turn)
    score = minmax(next_board, move, n_steps-1, False, turn, -np.Inf, np.Inf)
    return score

def agent_minmax(all_moves, board):
    n_steps = 3
    scores = dict(zip(np.arange(len(all_moves)), [score_move_minmax(board,move,n_steps) for move in all_moves]))
    max_score = [key for key in scores.keys() if scores[key] == max(scores.values())]
    return all_moves[random.choice(max_score)]

