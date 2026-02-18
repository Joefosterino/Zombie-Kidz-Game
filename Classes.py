class Room:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors
        self.zombies = 0
        self.is_locked = False

    def add_zombie(self):
        self.zombies += 1
        return self.zombies >= 4  # Returns True if game is lost
    
    def clear_room(self):
        self.zombies = 0
