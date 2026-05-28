class Table:
    def __init__(self, capacity: int = 4):
        self.seats = [Seat() for _ in range(capacity)]

    def assign_seat(self, name: str) -> bool:
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False

    def left_capacity(self):
        return sum(1 for seat in self.seats if seat.free)