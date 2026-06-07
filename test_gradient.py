from game import Game
from matplotlib import pyplot as plt
import random
import numpy as np
import time
from numba import njit, prange

game_graph = Game(5)
is_parallel = None
graph_approx = None
points = None
mask = {
    "y": True,
    "n": False
}

while True:
    try:
        graph_approx = int(input("number of rounds for every point: ").lower().strip())
        break
    except ValueError:
        print("Value is not valid")
while True:
    try:
        points = int(input("number of points: ").lower().strip())
        break
    except ValueError:
        print("Value is not valid")
while is_parallel is None:
    is_parallel = mask.get(input("Do you wanna use multi-threading?(y/n):").strip().lower())


@njit(fastmath=True)
def abs_error(wh) -> float:
    g_ax = graph_approx
    game = Game(5)
    threshold = 2
    outcomes = []
    for i in range(g_ax): #type: ignore
        outcome = None
        counter_for_turn = random.randint(1, 2)
        while outcome is None:
            if game.turn == counter_for_turn:
                sum_b = 0
                for i in game.bullets:
                    sum_b += i * wh
                choice = sum_b
                if choice > threshold:
                    outcome = game.make_move(1)
                else:
                    outcome = game.make_move(0)
            else:
                if sum(game.bullets) > game.init_bullets // 2:
                    outcome = game.make_move(1)
                else:
                    outcome = game.make_move(0)
        if outcome == counter_for_turn:
            outcomes.append(1)
        else:
            outcomes.append(0)
    return 1 - (sum(outcomes) / len(outcomes))


x = np.linspace(-10, 10, (points))
y = []
avg_time = 10**-9

@njit(parallel=True, fastmath=True)
def parallel_results(lst):
    results = np.zeros(len(lst), dtype=np.float64)
    for i in prange(len(lst)):
        results[i] = abs_error(lst[i])
    return results



if not is_parallel:
    counter = 0
    for i in x:
        timer1 = time.perf_counter()
        counter += 1
        y.append(abs_error(i))
        timer2 = time.perf_counter()
        avg_time = avg_time + (timer2 - timer1)
        print(
            f"\rGames: {counter}/{points} | ETA: {round(((avg_time/counter)*(points-counter))/60, 1)} min",
            end="",
            flush=True,
        )
    print(f"\nprocess finished in {round((avg_time)/60, 1)} min")
else:
    print("calculating with multi-threading...")
    t1 = time.perf_counter()
    y = parallel_results(x)
    t2 = time.perf_counter()
    print(f"process finished in {round((t2-t1)/60, 1)} min")


plt.plot(x, y)
plt.show()
