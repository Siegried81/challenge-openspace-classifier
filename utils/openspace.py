import random
from utils.table import Table


class OpenSpace:
    def __init__(self):
        self.tables = [Table() for _ in range(6)]

    def organize(self, names):
        random.shuffle(names)

        overflow = []

        for name in names:
            placed = False

            for table in self.tables:
                if table.assign_seat(name):
                    placed = True
                    break

            if not placed:
                overflow.append(name)

        return overflow

    def display(self):
        for i, table in enumerate(self.tables):
            print(f"\nTable {i+1}")

            for seat in table.seats:
                if seat.occupant:
                    print("-", seat.occupant)

    def store(self, filename):
        file = open(filename, "w")

        file.write("Table,Seat,Name\n")

        for i, table in enumerate(self.tables):
            for j, seat in enumerate(table.seats):
                if seat.occupant:
                    file.write(f"{i+1},{j+1},{seat.occupant}\n")

        file.close()

#test
people = ["Anna", "Dan", "Max", "Hiba", "Victor", "Neha"]

space = OpenSpace()

overflow = space.organize(people)

space.display()

print("\nOverflow:", overflow)
space.store("output.csv")