class Room:
    def __init__(self, name, neighbors, is_entry = False):
        self.name = name
        self.neighbors = neighbors
        self.zombies = 0
        self.is_entry = is_entry
        self.is_locked = False

    def add_zombie(self):
        self.zombies += 1
        return self.zombies >= 4  # Returns True if game is lost
    
    def clear_room(self):
        self.zombies = 0

class ZombieBank:
    def __init__(self, qty=8):
        self.qty = qty
        self.max_qty = qty

    def add_zombie_to_bank(self, amount):
        self.qty += amount
        if self.qty > self.max_qty:
            self.qty = self.max_qty

    def remove_zombie_from_bank(self):
        if self.qty > 0:
            self.qty -= 1
            return True
        return False