from checkers import Checkers
from heuristic_agent import agent_one_step_heuristic
from minmax_agent import agent_minmax
import time

def main():
    player1 = agent_minmax()
    player2 = agent_one_step_heuristic()

    n = 100
    win_ratio = [0, 0, 0, 0]
    
    for i in range(n):
        game = Checkers(8,False)
        winner = game.play(player1, player2)
        if winner[0] == "White":
            win_ratio[0] += 1
        else: win_ratio[1] += 1

        game = Checkers(8,False)
        winner = game.play(player2, player1)
        if winner[0] == "White":
            win_ratio[2] += 1
        else: win_ratio[3] += 1

    win_ratio = map(lambda x: round(x*100/n, 2), win_ratio)
    win_ratio = list(win_ratio)

    print("white_ratio_minmax: ", win_ratio[0], " [%]")
    print("black_ration_one: ", win_ratio[1], " [%]")
    print()
    print("white_ratio_one: ", win_ratio[2], " [%]")
    print("black_ratio_minmax: ", win_ratio[3], " [%]")

if __name__ == "__main__":
    start = time.time()
    main()
    stop = time.time()
    print(stop-start)