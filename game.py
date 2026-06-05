import random

class Game:
    def __init__(self, n_bullets: int):
        self.init_bullets = n_bullets
        self.bullets = [random.randint(0,1) for _ in range(n_bullets)] #1: vero, 0: falso
        self.lifes = [5,5] # [primo_g, secondo_g]
        self.counter = 0 #poi fai counter % 2 + 1
        self.turn = 1
        self.next_bullet = None
    def make_move(self, move: int) -> None | int:
        if 0 in self.lifes:
            self.lifes = [5,5]
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
            self.bullets = [random.randint(0,1) for _ in range(self.init_bullets)]
            self.counter = 0
            self.turn = 1
            return (self.lifes.index(0) + 1)%2 + 1
        if len(self.bullets) == 0:
            self.bullets = [random.randint(0,1) for _ in range(self.init_bullets)]
    def __repr__(self) -> str:
        d = {
            "bullets": self.bullets,
            "real_bullets": sum(self.bullets),
            "fake_bullets": len(self.bullets)-sum(self.bullets),
            "player_1_lifes": self.lifes[0],
            "player_2_lifes": self.lifes[1],
            "turn": self.turn
        }
        
        return str(d).replace(",", ",\n").replace("{", "").replace("}", "").replace(" ", "")


    
