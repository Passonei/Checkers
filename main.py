from checkers import Checkers
from Agents.heuristic_agent import agent_one_step_heuristic
from Agents.minmax_agent import agent_minmax
import time
from datetime import timedelta

def show_result(ratio, player1, player2):
    print(f"White_ratio {player1.__class__.__name__}: {ratio[0]} [%]")
    print(f"Black_ratio {player2.__class__.__name__}: {ratio[1]} [%]")
    print()

def n_matches(n, player1, player2):
    win_ratio = [0, 0, 0, 0]
    
    for i in range(n):
        game = Checkers(8,False)
        winner = game.play(player1, player2)
        if winner[0] == "White":
            win_ratio[0] += 1
        else: win_ratio[1] += 1

    win_ratio = map(lambda x: round(x*100/n, 2), win_ratio)
    win_ratio = list(win_ratio)
    return win_ratio

def main():
    player1 = agent_minmax()
    player2 = agent_one_step_heuristic()
    n = 100

    win_ratio = n_matches(n, player1, player2)
    show_result(win_ratio, player1, player2)

    win_ratio = n_matches(n, player2, player1)
    show_result(win_ratio, player2, player1)

if __name__ == "__main__":
    start = time.time()
    try:
        main()
    except Exception as e:
        if(str(e)=="No available video device"):
            print("No available video device. Run with changing Checker's show parameter to False.")

    stop = time.time()
    print(timedelta(seconds = (stop-start)))