import map
from random import randint
from map import build_board
from Classes import ZombieBank


class Player:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.position = "Office"

# Create a list where the index matches the dice roll
# 0=White (Office), 1=Red (Gym), etc.
zombie_die_map = ["Office", "Gym", "Classroom", "Storeroom", "Library", "None"]

def display_status(game_board, players, zbank):
    print("\n" + "═" * 50)
    print(f"║ SCHOOL MAP | 🧟 Bank: {zbank.qty}/8 | 🔑 Gates: {sum(1 for r in game_board.values() if r.is_locked)}/4 ║")
    print("═" * 50)
    
    # Header
    print(f"{'Room':<25} | {'Zombies':<8} | {'Players':<12}")
    print("-" * 50)

    for name, room in game_board.items():
        # Get player names in this room
        occupants = ", ".join([p.name for p in players if p.position == name])
        
        # Build status indicators
        status_icon = ""
        if room.is_locked:
            status_icon = "[LOCKED]"
        elif room.zombies >= 3:
            status_icon = "[OVERRUN]"
        elif room.zombies > 0:
            status_icon = f"({room.zombies})"

        # Format the room name and status
        room_display = f"{name} {status_icon}"
        print(f"{room_display:<25} | {room.zombies:<8} | {occupants:<12}")
    print("═" * 50)

def game_loop():
    print("🧟--- Welcome to Zombie KidZ - Save the school!!🧟")
    # Initilise Game State
    
    game_board = build_board()
    zbank = ZombieBank(8)

    players = [Player("Hero 1", "Blue"),Player("Hero 2", "Red")]
    turn_counter = 0

    game_running = True
    while game_running:
        
        current_player = players[turn_counter % 2]
        print(f"It is {current_player.name}'s turn")
        print("....Dice Rolling....")
        dice_roll = randint(0,5)
        room_name = zombie_die_map[dice_roll]

        if room_name == "None":
            print("No Zombie entered the building")
        else:
        # Capture the result of the bank removal
            spawn_success = zbank.remove_zombie_from_bank()
            
            if spawn_success:
                game_board[room_name].add_zombie()
                print(f"Zombie entered the {room_name}. Zombie Bank: {zbank.qty}")
            else:
                print("\n💀 GAME OVER! No more zombies in the bank. The school is overrun!")
                game_running = False
                continue  # Skip the rest of the turn and exit
        
        display_status(game_board, players, zbank)

        print(f"\n{current_player.name} is in the {current_player.position}")
        action = input("Choose action: (m)ove, (q)uit: ").lower()

        if action == 'q':
            game_running = False
        elif action == 'm':
            new_room = input("Which room? (Office, Gym, Classroom, Storeroom, Library, Entryway1-4 or type current room to stay): ")
            
            # --- UPDATE: Check if neighbor OR staying put ---
            is_neighbor = new_room in game_board[current_player.position].neighbors
            is_staying = new_room == current_player.position

            if is_neighbor or is_staying:
                target_room = game_board[new_room]
                
                if target_room.zombies < 3:
                    # Move (or stay)
                    current_player.position = new_room 
                    
                    # Clear zombies
                    if target_room.zombies > 0:
                        zbank.add_zombie_to_bank(target_room.zombies)
                        print(f"\n✨ {target_room.zombies} zombies cleared from the {new_room}! Zombie Bank: {zbank.qty}")
                        target_room.clear_room()
                    
                    # --- WIN CONDITION CHECK (Moved here) ---
                    # Check if both players are now in the same room after the move
                    pos1 = players[0].position
                    pos2 = players[1].position

                    if pos1 == pos2:
                        room = game_board[pos1]
                        if room.is_entry and not room.is_locked:
                            room.is_locked = True
                            print(f"🔒 HIGH FIVE! {pos1} has been LOCKED!")
                            
                else:
                    print(f"🚫 {new_room} is overrun (3+ zombies)! You can't enter/stay.")
            else:
                print("❌ Those rooms aren't connected, and you didn't choose to stay put!")

        # Count how many rooms have is_locked == True
        locked_count = sum(1 for r in game_board.values() if r.is_locked)
        
        if locked_count == 4:
            print("🎉 CONGRATULATIONS! All gates are locked. The school is safe!")
            game_running = False
        
        turn_counter += 1
        
if __name__ == "__main__":
    game_loop()