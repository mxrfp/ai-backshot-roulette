import random
from numba import jit, int16, int64 ,  types
from numba.experimental import jitclass
from numba.typed import List

class_except = [
     ("init_bullets", int64),
     ("bullets", types.ListType(int64)),
     ("lifes", types.ListType(int64)),
     ("counter", int64),
     ("turn", int64),
     ("next_bullet", types.optional(int64))
]

@jitclass(class_except) #type: ignore
class Game:
    def __init__(self, n_bullets: int):
        self.init_bullets = n_bullets
        self.bullets = List.empty_list(int64)
        for _ in range(n_bullets):
            self.bullets.append(int64(random.randint(0,1)))
        self.lifes = List.empty_list(int64) # [primo_g, secondo_g]
        self.lifes.append(int64(5))
        self.lifes.append(int64(5)) 
        self.counter = 0 #poi fai counter % 2 + 1
        self.turn = 1
        self.next_bullet = None
    def make_move(self, move: int) -> None | int:
        if 0 in self.lifes:
            self.lifes = List.empty_list(int64) # [primo_g, secondo_g]
            self.lifes.append(int64(5))
            self.lifes.append(int64(5)) 
        next_bullet = self.bullets.pop(random.randint(0, len(self.bullets)-1))
        self.next_bullet = next_bullet
        if move == 0: #a te stesso
            if next_bullet == 1:
                self.lifes[self.counter%2] -= 1
                self.counter += 1
        else:
            if next_bullet == 1:
                self.lifes[(self.counter+1)%2] -= 1
            self.counter += 1
        self.turn = self.counter % 2 + 1
        if 0 in self.lifes:
            self.bullets = List.empty_list(int64)
            for _ in range(self.init_bullets):
                self.bullets.append(int64(random.randint(0,1)))
            self.counter = 0
            self.turn = 1
            return (self.lifes.index(0) + 1)%2 + 1
        if len(self.bullets) == 0:
            self.bullets = List.empty_list(int64)
            for _ in range(self.init_bullets):
                self.bullets.append(int64(random.randint(0,1)))
    def show(self) -> str:
        d = {
            "bullets": self.bullets,
            "real_bullets": sum(self.bullets),
            "fake_bullets": len(self.bullets)-sum(self.bullets),
            "player_1_lifes": self.lifes[0],
            "player_2_lifes": self.lifes[1],
            "turn": self.turn
        }
        
        return str(d).replace(",", ",\n").replace("{", "").replace("}", "").replace(" ", "")


    
