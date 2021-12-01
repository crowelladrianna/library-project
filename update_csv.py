import csv

# eventually have these passed as command line arguments 
# something like python update_csv.py add name_to_add
add_file = "test_data/test_add_file.csv"
complete_file = "test_data/test_complete_list.csv"

def parse_complete(file_name):
    ids = set()
    header = []

    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            ids.add(row[0])
    return ids, header

def add_to_complete(add_name, complete_ids, header, complete_name):
    with open(complete_name, 'a', newline='') as f1, open(add_name, newline='') as f2:
        writer = csv.DictWriter(f1, fieldnames=header)
        reader = csv.DictReader(f2)
        for row in reader:
            if(not row[header[0]] in complete_ids):
                writer.writerow(row)

ids_present, header = parse_complete(complete_file)

add_to_complete(add_file, ids_present, header, complete_file)