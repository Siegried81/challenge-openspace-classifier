import utils.file_utils as utils                # import file utilities
from utils.openspace import OpenSpace           # import OpenSpace class


def main():
                                                # load names from csv file
    names = utils.read_names_from_csv("new_colleagues.csv")

                                                # create open space system
    space = OpenSpace()

                                                # assign people to tables
    overflow = space.organize(names)

                                                # display seating plan
    space.display()

                                                # save result into csv file
    space.store("output.csv")

                                                # print people without seats
    print("\nOverflow:", overflow)


                                                # run program
main()