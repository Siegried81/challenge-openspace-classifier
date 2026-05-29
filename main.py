from src.openspace import OpenSpace
from src.utils import read_names_from_csv

def main():
    # charge les données
    names = read_names_from_csv("new_colleagues.csv")

    # setup fixe (sans config.json)
    open_space = OpenSpace(
        {"tables": 6, "seats_per_table": 4}
    )

    # exécution simple
    open_space.organize(names)

    print("Seats:", open_space.total_seats())
    print("People:", open_space.total_people())
    print("Remaining:", open_space.remaining_seats())

if __name__ == "__main__":
    main()