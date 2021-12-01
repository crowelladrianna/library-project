import csv

def read_file(file_name):
    rows = []  # this list should contain one tuple per row
    
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        next(reader) # skips the header
        for row in reader:
            row_tup = (row[0], row[1], row[2], row[3], row[4])
            rows.append(row_tup)
    return rows

# to_add = read_file(WHATEVER NAME)
# complete = read_file(WHATEVER NAME)