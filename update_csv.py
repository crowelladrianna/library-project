import csv

# eventually have these passed as command line arguments 
# something like python update_csv.py add name_to_add
add_file = "test_data/test_add_file.csv"
complete_file = "test_data/test_complete_list.csv"

def read_file(file_name):
    rows = []  # this list should contain one tuple per row
    
    with open(file_name, newline='') as f:
        reader = csv.DictReader(f)

        for row in reader:
            rows.append(row)
    return rows

def parse_complete(file_name):
    ids = set()
    header = []

    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            ids.add(row[0])
    return ids, header

def add_to_complete(add_rows, complete_ids, header, complete_name):
    with open(complete_name, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        for row in add_rows:
            if(not row[header[0]] in complete_ids):
                writer.writerow(row)

    
to_add = read_file(add_file)
ids_present, header = parse_complete(complete_file)

add_to_complete(to_add, ids_present, header, complete_file)


