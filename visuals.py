def show_map(board, players):
    print("\n--- SCHOOL MAP ---")
    # This version shows Zombies (Z) and Players (P)

    # Create a helper to see what's in a room
    def get_label(room_name):
        stripped_room = room_name.strip()
        room = board.get(stripped_room)
        if not room: return room_name

        # Count zombies and check for players
        z = room.zombies
        p = "P" if any(player.position == stripped_room for player in players) else ""
        return f"{stripped_room[:9]:^9}(Z:{z}){p}"

    # The Layout
    print(f"[{get_label('Entryway1')}] -- [{get_label('Storeroom')}] -- [{get_label('Entryway2')}]")
    print("      |                    |                   |      ")
    print("      |                    |                   |      ")
    print(f"[{get_label('   Gym   ')}] -- [{get_label(' Office  ')}] -- [{get_label(' Library ')}]")
    print("      |                    |                   |      ")
    print("      |                    |                   |      ")
    print(f"[{get_label('Entryway4')}] -- [{get_label('Classroom')}] -- [{get_label('Entryway3')}]")
    print("---------------------------------------------")
    input("Press Enter to return to game...")