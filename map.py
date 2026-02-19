# map_data.py
from Classes import Room

def build_board():
    # 1. Create the room objects with their neighbors
    rooms = {
        "Office": Room("Office", ["Gym", "Classroom", "Storeroom", "Library"]),
        "Gym": Room("Gym", ["Office", "Classroom", "Storeroom", "Entryway1", "Entryway4"]),
        "Storeroom": Room("Storeroom", ["Office", "Gym", "Library", "Entryway1", "Entryway2"]),
        "Classroom": Room("Classroom", ["Office", "Gym", "Storeroom", "Entryway3", "Entryway4"]),
        "Library": Room("Library", ["Office", "Classroom", "Storeroom", "Entryway2", "Entryway3"]),
        "Entryway1": Room("Entryway1", ["Gym", "Storeroom"], True),
        "Entryway2": Room("Entryway2", ["Storeroom", "Library", True]),
        "Entryway3": Room("Entryway3", ["Classroom", "Library", True]),
        "Entryway4": Room("Entryway4", ["Gym", "Classroom"], True)     
    }
    return rooms