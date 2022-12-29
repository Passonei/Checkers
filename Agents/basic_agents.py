import random
import numpy as np

class agent_random:
    def decision(self, moves, *arg):
        return random.choice(moves)

class agent_one_side_preferred:
    def __init__(self, side_preferred="left"):
        if str(side_preferred) == "left":
            self.preferred = min
        else:
            self.preferred = max

    def decision(self, moves, *arg):
        moves = np.array(moves)
        side_moves = moves[moves[:,1]==self.preferred(moves[:,1])]
        return random.choice(side_moves)

class agent_row_preferred:
    def __init__(self, row_preferred="first"):
        if str(row_preferred) == "first":
            self.preferred = [max,min]
        else:
            self.preferred = [min,max]
    
    def decision(self, moves, turn):
        moves = np.array(moves)
        preferred_moves = moves[moves[:,0]==self.preferred[turn](moves[:,0])]
        return random.choice(preferred_moves)