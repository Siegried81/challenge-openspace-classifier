import random
from utils.table import Table


class OpenSpace:
    def __init__(self, number_of_tables=6):
        self.tables = [Table() for _ in range(number_of_tables)]

    def organize(self, people):
        random.shuffle(people)

        overflow = []

        for person in people:
            placed = False

            for table in self.tables:
                if table.assign_seat(person):
                    placed = True
                    break

            if not placed:
                overflow.append(person)

        return overflow

    def display(self):
        for i, table in enumerate(self.tables):
            print(f"\nTable {i + 1}")
            for seat in table.seats:
                print("-", seat.occupant)


                

from utils.file_utils import load_people
from utils.openspace import OpenSpace

people = load_people("new_colleagues.txt")

space = OpenSpace()

overflow = space.organize(people)

space.display()

print("\nOverflow:", overflow)