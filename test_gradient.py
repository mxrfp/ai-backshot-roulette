from game import Game
from matplotlib import pyplot as plt
import random
import numpy as np
import time
from numba import njit

game_graph = Game(5)

@njit  
def abs_error(wh) -> float:
            g_ax = 50000
            game = Game(5)
            threshold = 2
            outcomes = []
            for i in range(g_ax):
                outcome = None
                counter_for_turn = random.randint(1,2)
                while outcome is None:
                    if game.turn == counter_for_turn:
                        sum_b = 0
                        for i in game.bullets:
                             sum_b += i*wh
                        choice = sum_b
                        if choice > threshold:
                            outcome = game.make_move(1)
                        else:
                            outcome = game.make_move(0)
                    else:
                        if sum(game.bullets) > game.init_bullets//2:
                            outcome = game.make_move(1)
                        else:
                            outcome = game.make_move(0)
                if outcome == counter_for_turn:
                        outcomes.append(1)
                else:
                        outcomes.append(0)
            return 1- (sum(outcomes)/len(outcomes))

x = np.linspace(-10, 10, (n:=5000)).tolist()
y = []
avg_time = 10**-9

counter = 0
for i in x:
     timer1 = time.perf_counter()
     counter += 1
     y.append(abs_error(i))
     timer2 = time.perf_counter()
     avg_time = avg_time + (timer2-timer1)
     print(f"\rGames: {counter}/{n} | ETA: {round(((avg_time/counter)*(n-counter))/60, 1)} min", end="", flush=True)



plt.plot(x, y)
plt.show()
