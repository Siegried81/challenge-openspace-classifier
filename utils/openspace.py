import random
from utils.table import Table


class OpenSpace:
    def __init__(self):
        self.tables = [Table() for _ in range(6)]

    def organize(self, people: list[str]):
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
            print(f"\nTable {i+1}")

            for seat in table.seats:
                if seat.occupant:
                    print("-", seat.occupant)

    def seats_left(self):
        return sum(table.left_capacity() for table in self.tables)