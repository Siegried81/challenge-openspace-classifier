import sys
from utils.file_utils import load_people
from utils.openspace import OpenSpace

def main():
    filepath = sys.argv[1] if len(sys.argv) > 1 else "new_colleagues.txt"
    people = load_people(filepath)
    space = OpenSpace()
    overflow = space.organize(people)
    space.display()
    print("\nSeats left:", space.seats_left())
    print("Overflow:", overflow)

if __name__ == "__main__":
    main()