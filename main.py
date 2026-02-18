import map
from random import randint
from map import build_board


class Player:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.position = "Office"

class Zombie_Bank:
    def __init__(self, no_zombies):
        pass

def game_loop():
    print("🧟--- Welcome to Zombie KidZ - Save the school!!🧟")
    # Initilise Game State
    print("....Dice Rolling....")
    dice_roll = randint(0,5)

    game_board = build_board()

    player = Player("Hero", "Blue")

    game_running = True
    while game_running:
        print(f"\n{player.name} is in the {player.position}")
        action = input("Choose action: (m)ove, (q)uit").lower()

        if action == 'q':
            game_running = False
        elif action == 'm':
            new_room = input("Which room? (Office, Gym, Classroom, Storeroom, Library)")
            if new_room in game_board[player.position]:
                player.position = new_room
            else:
                print("Invalid room!")
        
if __name__ == "__main__":
    game_loop()