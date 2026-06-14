import random
import numpy as np


class SimpleAi:
    def __init__(self, game):
        self.game = game
        self.weight = 0
        self.threshold = 2

    def train(self, graph_approx: int) -> None:
        def abs_error(wh, g_ax) -> float:
            outcomes = []
            for i in range(g_ax):
                outcome = None
                counter_for_turn = random.randint(1, 2)
                while outcome is None:
                    if self.game.turn == counter_for_turn:
                        choice = (np.array(self.game.bullets) * wh).sum()
                        if choice > self.threshold:
                            outcome = self.game.make_move(1)
                        else:
                            outcome = self.game.make_move(0)
                    else:
                        if sum(self.game.bullets) > self.game.init_bullets // 2:
                            outcome = self.game.make_move(1)
                        else:
                            outcome = self.game.make_move(0)
                if outcome == counter_for_turn:
                    outcomes.append(1)
                else:
                    outcomes.append(0)
            return 1 - (sum(outcomes) / len(outcomes))

        whg = random.randint(2, 10)
        step = 0.5
        calculated_points = dict()
        epoch = 1000
        for _ in range(epoch):
            errors = []
            whgs = [whg - step, whg, whg + step]
            for i in whgs:
                new_w = calculated_points.get(i)
                if new_w is None:
                    new_w = abs_error(i, graph_approx)
                    calculated_points[i] = new_w
                else:
                    new_w = calculated_points[i]
                errors.append(new_w)
            slopes = []
            slopes.append((errors[0] - errors[1]) / (max(whgs[:2:]) - min(whgs[:2:])))
            slopes.append((errors[2] - errors[1]) / (max(whgs[1:]) - min(whgs[1:])))
            if slopes[1] > 0 and slopes[0] > 0:
                break
            elif slopes[0] < slopes[1]:
                whg = whg - step
            else:
                whg = whg + step
            print(f"\rwheight: {whg}", end="", flush=True)
        self.weight = whg

    def play(self, game) -> int:
        choice = (np.array(game.bullets) * self.weight).sum()
        if choice > self.threshold:
            return 1
        else:
            return 0
