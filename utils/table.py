class Seat:
    def __init__(self):
        self.free = True
        self.occupant = None

    def set_occupant(self, name: str):
        self.occupant = name
        self.free = False

    def remove_occupant(self):
        name = self.occupant
        self.occupant = None
        self.free = True
        return name


#test
seat = Seat()

print(seat.free)  

seat.set_occupant("Anna")

print(seat.occupant)  
print(seat.free)      

removed = seat.remove_occupant()

print(removed)         
print(seat.free)       



class Table:
    def __init__(self, capacity: int = 4):
        self.seats = [Seat() for _ in range(capacity)]

    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                return True
        return False

    def assign_seat(self, name: str):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False

    def left_capacity(self):
        return sum(1 for seat in self.seats if seat.free)
    
#test
table = Table()

# table empty at the beginning
print(table.left_capacity())   
print(table.has_free_spot())   

# fill in partialy
table.assign_seat("Anna")
table.assign_seat("Dan")

print(table.left_capacity())   
print(table.has_free_spot())   

# fill in totally
table.assign_seat("Max")
table.assign_seat("Hiba")

print(table.left_capacity())   
print(table.has_free_spot())   