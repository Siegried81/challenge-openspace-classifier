import random

class Seat:
    """
    Represents a single seat in a table.
    """
    def __init__(self) -> None:
        """
        Initializes an empty seat.
        """
        self.free: bool = True
        self.occupant: str = ""

    def __str__(self) -> str:
        """
        Returns a string representation of the seat.
        :return: A string indicating if the seat is free or occupied.
        """
        if self.free:
            return "Free"
        return f"Occupied by {self.occupant}"

    def set_occupant(self, name: str) -> None:
        """
        Assigns a colleague to this seat.
        :param name: The name of the colleague.
        """
        self.occupant = name
        self.free = False

    def remove_occupant(self) -> None:
        """
        Removes the colleague and frees the seat.
        """
        self.occupant = ""
        self.free = True


class Table:
    """
    Represents a table containing a fixed capacity of seats.
    """
    def __init__(self, capacity: int = 4) -> None:
        """
        Initializes a table with a fixed capacity.
        :param capacity: Total number of seats at this table.
        """
        self.capacity: int = capacity
        self.seats: list[Seat] = [Seat() for _ in range(capacity)]

    def __str__(self) -> str:
        """
        Returns a string overview of the table status.
        :return: Description of occupied seats out of capacity.
        """
        occupied = sum(1 for seat in self.seats if not seat.free)
        return f"Table ({occupied}/{self.capacity} occupied)"

    def has_free_spot(self) -> bool:
        """
        Checks if there is at least one unassigned seat.
        :return: True if a seat is free, False otherwise.
        """
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name: str) -> bool:
        """
        Assigns a person to the first available free seat at the table.
        :param name: The name of the person to seat.
        :return: True if assignment was successful, False if table is full.
        """
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False

    def left_capacity(self) -> int:
        """
        Calculates how many seats remain unoccupied at this table.
        :return: Count of free seats.
        """
        return sum(1 for seat in self.seats if seat.free)