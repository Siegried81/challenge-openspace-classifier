import csv                                  # module to read CSV files

def read_names_from_csv(filepath):
    names = []                              # list to store names

                                            # open file safely with utf-8 encoding
    with open(filepath, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

                                            # read each row
        for row in reader:
            if row:                         # skip empty rows
                names.append(row[0])        # take first column

    return names

