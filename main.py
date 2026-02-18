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

# Create a list where the index matches the dice roll
# 0=White (Office), 1=Red (Gym), etc.
zombie_die_map = ["Office", "Gym", "Classroom", "Storeroom", "Library", "None"]

def game_loop():
    print("🧟--- Welcome to Zombie KidZ - Save the school!!🧟")
    # Initilise Game State
    print("....Dice Rolling....")
    game_board = build_board()
    dice_roll = randint(0,5)
    room_name = zombie_die_map[dice_roll]

    if room_name == "None":
        print("No Zombie entered the building")
    else:
        game_board[room_name].add_zombie()
        print(f"Zombie entered the {room_name}")

    player = Player("Hero", "Blue")

    game_running = True
    while game_running:
        print(f"\n{player.name} is in the {player.position}")
        action = input("Choose action: (m)ove, (q)uit: ").lower()

        if action == 'q':
            game_running = False
        elif action == 'm':
            new_room = input("Which room? (Office, Gym, Classroom, Storeroom, Library): ")
            if new_room in game_board[player.position].neighbors:
                player.position = new_room
                if (game_board[player.position].zombies < 3) and (game_board[player.position].zombies > 0):
                    print(f"\n{game_board[player.position].zombies} zombies cleared from the {player.position}")
                    game_board[player.position].clear_room()
                else:
                    print(f"More than 3 zombies in the {player.position}, unable to clear it!")
            else:
                print("Unable to move to this room! Please try again:")
        
if __name__ == "__main__":
    game_loop()