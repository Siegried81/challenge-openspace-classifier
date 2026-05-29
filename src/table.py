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

#tests 
# Create a new Seat object
# At the beginning, the seat should be empty
seat1 = Seat()

# Display the initial state of the seat
print("Initial state:")

# Check if the seat is free
# Expected result: True
print("Free:", seat1.free)

# Check who is sitting on the seat
# Expected result: None because nobody is sitting there
print("Occupant:", seat1.occupant)


# Assign a person to the seat
# Here we place "Max" on the seat
seat1.set_occupant("Max")


# Display the state after assigning someone
print("\nAfter assigning Max:")

# The seat should no longer be free
# Expected result: False
print("Free:", seat1.free)

# The occupant should now be Max
# Expected result: Max
print("Occupant:", seat1.occupant)


# Remove the person from the seat
# The method returns the name of the removed person
removed = seat1.remove_occupant()


# Display the state after removing the occupant
print("\nAfter removal:")

# Show the name of the removed person
# Expected result: Max
print("Removed:", removed)

# The seat should now be free again
# Expected result: True
print("Free:", seat1.free)

# There should be no occupant anymore
# Expected result: None
print("Occupant:", seat1.occupant)


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

