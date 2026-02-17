import map.py

class Room:
    def __init__(self, name):
        self.name = name
        self.zombies = 0
        self.is_locked = False

class Player:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.position = "Office"

def game_loop():
    print("🧟--- Welcome to Zombie KidZ - Save the school!!🧟")
    # Initilise Game State
    rooms = {
        "Office" : Room("Office")
        "Gym" : Room("Gym")
        "Classroom" : Room("Classroom")
        "Storeroom" : Room("Storeroom")
        "Library" : Room("Library")
    }
    player = Player("Hero", "Blue")

    game_running = True
    while game_running:
        print(f"\n{player.name} is in the {player.position}")
        action = input("Choose action: (m)ove, (q)uit").lower()

        if action == 'q':
            game_running = False
        elif action == 'm':
            new_room = input("Which room? (Office, Gym, Classroom, Storeroom, Library)")
            if new_room in rooms:
                player.position = new_room
            else:
                print("invalid room!")
        
if __name__ == "__main__":
    game_loop()