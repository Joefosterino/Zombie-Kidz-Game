# map_data.py
from Classes import Room

def build_board():
    # 1. Create the room objects with their neighbors
    rooms = {
        "Office": Room("Office", ["Gym", "Classroom", "Storeroom", "Library"]),
        "Gym": Room("Gym", ["Office", "Classroom", "Storeroom"]),
        "Storeroom": Room("Storeroom", ["Office", "Gym", "Library"]),
        "Classroom": Room("Classroom", ["Office", "Gym", "Storeroom"]),
        "Library": Room("Library", ["Office", "Classroom", "Storeroom"])
    }
    return rooms