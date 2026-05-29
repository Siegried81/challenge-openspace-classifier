from src.utils.file_utils import read_names_from_csv  # import function to read CSV file
from src.utils.openspace import OpenSpace           # import OpenSpace class (handles tables and seating)


def main():
                                                # read all names from CSV file
    names = read_names_from_csv("new_colleagues.csv")
                                                # create an OpenSpace (all tables + seats)
    space = OpenSpace()
                                                # assign people to seats, get those who have no place
    overflow = space.organize(names)
                                                # display seating arrangement in console
    space.display()
                                                # save seating result into a CSV file
    space.store("output.csv")
                                                # print people who could not be placed
    print("\nOverflow:", overflow)
                                                # run the program
main()