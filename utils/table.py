class Seat:
    def __init__(self):
        self.free = True
        self.occupant = None

    def set_occupant(self, name):
        if self.free:
            self.occupant = name
            self.free = False

    def remove_occupant(self):
        name = self.occupant
        self.occupant = None
        self.free = True
        return name


class Table:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]

    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                return True
        return False

    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False

    def left_capacity(self):
        count = 0

        for seat in self.seats:
            if seat.free:
                count += 1

        return count


# TESTS ↓↓↓ (tout en bas, sans indentation)

table1 = Table()

print(table1.left_capacity())

table1.assign_seat("Anna")
table1.assign_seat("Dan")

print(table1.left_capacity())

print(table1.has_free_spot())