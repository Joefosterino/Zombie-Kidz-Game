# map_data.py
from Classes import Room

def build_board():
    # 1. Create the room objects with their neighbors
    rooms = {
        "Entry": Room("Entry", ["Gym", "Changing Room"]),
        "Gym": Room("Gym", ["Entry", "Classroom"]),
        "Changing Room": Room("Changing Room", ["Entry", "Locker Room"]),
        "Classroom": Room("Classroom", ["Gym"]),
        "Locker Room": Room("Locker Room", ["Changing Room"])
    }
    return rooms