import csv
def read_names_from_csv(filepath):
    names = []

    with open(filepath, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            if row:
                names.append(row[0])

    return names