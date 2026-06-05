from game import Game
from AI import SimpleAi

def bullets(lst: list[int]):
    mask = {
        1: "real",
        0: "blank"
    }
    string = ""
    for i in range(7):
        if i == 0 or i == 6:
            string += ("-"*7 + "  ")*len(lst) + "\n"
        elif i == 7//2:
            f_string = ""
            for j in lst:
                f_string += "|" + mask[j].center(6) + "| "
            string += f_string + "\n"
        else: 
            string += ("|" + " "*6 + "| ")*len(lst) + "\n"
    return string

                

def_approx = 9999
def_bullets = 5

print("-"*30)
print("AI BUCKSHOT ROULETTE".center(30))
print("-"*30)
print()
print("[0]: SHOOT AT YOURSELF")
print()
print("[1]: SHOOT AT THE ENEMY")

game_to_play = Game(def_bullets)
bot = SimpleAi(Game(5))

while True:
    if (choice := input("Start (y/n): ").lower().strip()) in "yn":
        if choice == "y":
            break
        else:
            exit()
    else:
        print("Not valid")

print()
print("TRAINING AI...")
print("  this process might take a while")
print()
bot.train(def_approx)

print("")

while True:
    if len(game_to_play.bullets) == game_to_play.init_bullets:
        print(bullets(game_to_play.bullets))
    if game_to_play.turn == 1:
        while True:
            try:
                move = input("Move('exit' to exit): ").lower().strip()
                if move == "exit":
                    exit()
                move = int(move)
                if move not in {0,1}:
                    raise ValueError
                break
            except ValueError:
                print("not valid")
        game_to_play.make_move(move)
    else:
        move = bot.play(game_to_play)
        print(f"The bot played: {move}")
        game_to_play.make_move(move)
    print()
    print(f"Bullet was " + ("blank" if game_to_play.next_bullet == 0 else "real"))
    print()
    print("Your lifes: " + "|"*game_to_play.lifes[0] + "           " + "Bot's lifes: " + "|"*game_to_play.lifes[1])
    print()

    

        

