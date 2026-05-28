class Seat:
    def __init__(self):
        self.free = True
        self.occupant = None

    def set_occupant(self, name):
        self.occupant = name
        self.free = False


class Table:
    def __init__(self):
        self.seats = [Seat(), Seat(), Seat(), Seat()]

    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False