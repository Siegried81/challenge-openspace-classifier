class Seat:
    def __init__(self):
                                        # seat is free at the beginning
        self.free = True
        self.occupant = None

    def set_occupant(self, name: str):
                                        # assign a person to the seat
        self.occupant = name
        self.free = False

    def remove_occupant(self):
                                        # remove person from seat and return name
        name = self.occupant
        self.occupant = None
        self.free = True
        return name


# simple tests (disabled)
# seat = Seat()
# print(seat.free)
# seat.set_occupant("Anna")
# print(seat.occupant)
# print(seat.free)
# removed = seat.remove_occupant()
# print(removed)
# print(seat.free)


class Table:
    def __init__(self, capacity: int = 4):
                                        # create seats inside table
        self.seats = [Seat() for _ in range(capacity)]

    def has_free_spot(self):
                                        # check if at least one seat is free
        for seat in self.seats:
            if seat.free:
                return True
        return False

    def assign_seat(self, name: str):
                                        # assign person to first available seat
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False

    def left_capacity(self):
                                        # count free seats
        return sum(1 for seat in self.seats if seat.free)


# simple tests (disabled)
# table = Table()
# print(table.left_capacity())
# print(table.has_free_spot())
# table.assign_seat("Anna")
# table.assign_seat("Dan")
# print(table.left_capacity())
# print(table.has_free_spot())
# table.assign_seat("Max")
# table.assign_seat("Hiba")
# print(table.left_capacity())
# print(table.has_free_spot())