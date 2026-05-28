import random                           # used to shuffle people randomly
from utils.table import Table  # import Table class


class OpenSpace:
    def __init__(self):
                                        # create 6 tables in the open space
        self.tables = [Table() for _ in range(6)]

    def organize(self, names):
                                        # shuffle list to randomize order
        random.shuffle(names)

                                        # list for people without seats
        overflow = []

                                        # assign each person to a table
        for name in names:
            placed = False              # check if person was placed

                                        # try each table
            for table in self.tables:
                if table.assign_seat(name):
                    placed = True
                    break  # stop when placed

                                        # if no seat found, add to overflow
            if not placed:
                overflow.append(name)

                                        # return people without seats
        return overflow

    def display(self):
                                        # print each table and its occupants
        for i, table in enumerate(self.tables):
            print(f"\nTable {i+1}")

                                        # show each occupied seat
            for seat in table.seats:
                if seat.occupant:
                    print("-", seat.occupant)

    def store(self, filename):
                                        # open file in write mode
        file = open(filename, "w")

                                        # write header row
        file.write("Table,Seat,Name\n")

                                        # loop through tables
        for i, table in enumerate(self.tables):
            for j, seat in enumerate(table.seats):
                if seat.occupant:
                                        # write data into csv file
                    file.write(f"{i+1},{j+1},{seat.occupant}\n")

                                        # close file after writing
        file.close()


# simple test (disabled)
# people = ["Anna", "Dan", "Max", "Hiba", "Victor", "Neha"]
# space = OpenSpace()
# overflow = space.organize(people)
# space.display()
# print("\nOverflow:", overflow)
# space.store("output.csv")