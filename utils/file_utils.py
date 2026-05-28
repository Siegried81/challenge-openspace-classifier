import csv  # module to read CSV files

def read_names_from_csv(filepath):     
    names = []                              # create empty list to store names

    # open the csv file safely
    with open(filepath, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)           # read file line by line

                                            # loop through each row in the file
        for row in reader:
            if row:                         # avoid empty lines
                names.append(row[0])        # take first column (name)

                                            # return full list of names
    return names