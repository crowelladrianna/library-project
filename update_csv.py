import csv
import os

# eventually have these passed as command line arguments 
# something like python update_csv.py add name_to_add
add_file = "test_data/test_add_file.csv"
complete_file = "test_data/test_complete_list.csv"
delete_file = "test_data/test_delete_file.csv"

def get_ids_header(file_name):
    ids = set()
    header = []

    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            ids.add(row[0])
    return ids, header

def add_to_complete(add_name, complete_name, complete_ids, header):
    with open(complete_name, 'a', newline='') as f1, open(add_name, newline='') as f2:
        writer = csv.DictWriter(f1, fieldnames=header)
        reader = csv.DictReader(f2)
        for row in reader:
            if(not row[header[0]] in complete_ids):
                writer.writerow(row)

def delete_from_complete(delete_ids, complete_name, header):
    temp = "test_data/test_complete_list_new.csv"
    with open(complete_name, newline='') as f1, open(temp, 'w', newline='') as f2:
        reader = csv.DictReader(f1)
        writer = csv.DictWriter(f2, fieldnames=header)
        writer.writeheader()
        for row in reader:
            if(not(row[header[0]]) in delete_ids):
                writer.writerow(row)
    with open(complete_name, 'w', newline='') as f1, open(temp, newline='') as f2:
        writer = csv.DictWriter(f1, fieldnames=header)
        reader = csv.DictReader(f2)
        writer.writeheader()
        for row in reader:
            writer.writerow(row)
    os.remove(temp)     

# deleting contents of add to verify same before and after
# eventually do this formally as test
ids_present, header = get_ids_header(complete_file)
ids_to_delete = get_ids_header(add_file)[0]
add_to_complete(add_file, complete_file, ids_present, header)
delete_from_complete(ids_to_delete, complete_file, header)