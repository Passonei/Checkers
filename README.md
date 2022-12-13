# Checkers
Checkers game with AI agents.  
The game has official rules such as:
- capturing is mandatory,
- backward capture is possible.

## checkers.py - Contains enviroment to checkers game.   

  - Checkers(ROWS_COUNTS=8, show=True)  
  Creates the starting board.  
  ###### Parameters:  
    ROW_COUNTS : int, optional  
        Defines side of a square board (size = ROW_COUNTSxROW_COUNTS).  
    show : bool, optional  
        Displays the progress of the game.
  
  #### play(agent_white, agent_black)  
  It plays a game between two autonomous agents.  
  ###### Parameters:  
    agent_white : object  
      Declaration of the agent making the first move.  
    agent_black : object  
      Declaration of the agent making the second move.  
  ###### Return :   
    Two-element list contains the winning player and the total number of moves made during the game. 
  <p align="center">
  <b> Example game between two agents <b/>   
  
  ![](https://github.com/Passonei/Checkers/blob/master/SampleGame.gif)  
  </p>
  
  #### play_vs_agent(player_turn, agent)  
  It plays a game between player and agents.  
  ###### Parameters:  
    player_turn : int  
      Declare who the first move belongs to.
      (player_turn = 1 : player starts first)  
    agent : object  
      Declaration of the agent who is the opponent.  
  ###### Return :   
    Two-element list contains the winning player and the total number of moves made during the game. 
   
## basic_agents.py - Contains agents making decisions based on simple strategies.   
  - agent_random()  
  Makes decisions randomly from among the allowed moves.
  
  - agent_one_side_preferred(side_preferred="left")  
  Makes decisions at random from among the allowed moves, preferring pawns from the selected side.
  ###### Parameters:
    side_preferred : str, optional
      Declaration of the preferred side.
      {"left", other string}
      
  - agent_row_preferred(row_preferred="first")  
  Makes decisions at random from among the allowed moves, preferring pawns from the selected side.
  ###### Parameters:
    row_preferred : str, optional
      Declaration of the preferred row.
      {"first", other string}
      
## heuristic_agent.py - Contains an agent that analyzes next moves.  
  - agent_one_step_heuristic(weight=[1, -10, 100, 1, 2], ROW_COUNT=8)  
  The agent makes decisions about the choice of move based on the heuristics of one next move.  
  ###### Parameters:  
    ROW_COUNTS : int, optional  
        Defines side of a square the board on which the game is played. (size = ROW_COUNTSxROW_COUNTS).  
    weight : list, optional  
        List of five integers values that are the weights of the parameters when calculating the heuristic.  
        Score = Matrix product of weight and X, where X=[a, b, c, d, e]
        a - num of possible capture, 
        b - num of possible oponent's capture, 
        c - possibility get_king, 
        d - num of pieces, 
        e - num of kings.
  
## minmax_agent.py - Contains an agent that analyzes several next moves  
  - agent_minmax(ROWS_COUNT=8, n_steps=3, weight=[10, 50, -4, -50, -20, 0])  
  The agent makes decisions about the choice of move based on the heuristics. The agent calculates the heuristics after n consecutive moves, selecting the move with the highest value being the sum of scores in odd moves (own) and the lowest in even moves (opponent's moves).
  ###### Parameters:  
    ROW_COUNTS : int, optional  
        Defines side of a square the board on which the game is played. (size = ROW_COUNTSxROW_COUNTS). 
    n_steps : int, optional 
        Defining the number of moves after which the heuristic is to be calculated.
    weight : list, optional  
        List of five integers values that are the weights of the parameters when calculating the heuristic.  
        Score = Matrix product of weight and X, where X=[a, b, c, d, e, f]
        a - num of pieces, 
        b - num of kings, 
        c - num of oponent's pieces, 
        d - num of oponent's kings, 
        e - num of possible capture,   
        f - num of possible oponent's capture. 
        
 # Future work
 - Addition of an agent using reinforcement learning.
