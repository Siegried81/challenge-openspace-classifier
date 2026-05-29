class Seat:
    def __init__(self):
                                            # a seat starts as empty
        self.free = True
        self.occupant = None

    def set_occupant(self, name):
                                            # assign a person to the seat
        self.occupant = name
        self.free = False                   # seat is now taken

    def remove_occupant(self):
                                            # remove the person from the seat
        name = self.occupant                # save name before deleting

        self.occupant = None                # clear seat
        self.free = True                    # mark seat as free again

        return name                         # return removed person

class Table:
    def __init__(self, capacity=4):
                                            # create a table with a fixed number of seats
        self.seats = [Seat() for _ in range(capacity)]

    def assign_seat(self, name):
                                            # try to place a person in a free seat
        for seat in self.seats:
            if seat.free:                   # check if seat is available
                seat.set_occupant(name)     # assign person
                return True                 # success

        return False                        # no free seat found
    


#tests
table = Table()
table.assign_seat("Anna")
table.assign_seat("Dan")

print(table.assign_seat("Max"))            # True if still space
print(table.assign_seat("Hiba"))
print(table.assign_seat("X"))          # False if full

