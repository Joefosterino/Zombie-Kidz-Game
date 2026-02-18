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
                target_room = game_board[new_room]  # Grab the actual Room object first
                
                if target_room.zombies < 3:
                    # Move the player
                    player.position = new_room 
                    
                    # Clear zombies using the target_room object directly
                    if target_room.zombies > 0:
                        print(f"\n✨ {target_room.zombies} zombies cleared from the {new_room}!")
                        target_room.clear_room()
                else:
                    print(f"🚫 {new_room} is overrun (3+ zombies)! You can't enter.")
            else:
                print("❌ Those rooms aren't connected!")
        
if __name__ == "__main__":
    game_loop()