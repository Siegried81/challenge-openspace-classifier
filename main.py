import utils.file_utils as utils
from utils.openspace import OpenSpace


def main():
    names = utils.read_names_from_csv("new_colleagues.csv")

    space = OpenSpace()

    overflow = space.organize(names)

    space.display()

    space.store("output.csv")

    print("\nOverflow:", overflow)


main()