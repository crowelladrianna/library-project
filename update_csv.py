import csv
import os

def get_ids_header(file_name):
    ids = set()
    header = []
    try:
        with open(file_name, newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                ids.add(row[0])
        return ids, header
    except FileNotFoundError as fnf_error:
        print(fnf_error)

def add_to_complete(add_name, complete_name, complete_ids, header):
    try:
        with open(complete_name, 'a', newline='') as f1, open(add_name, newline='') as f2:
            writer = csv.DictWriter(f1, fieldnames=header)
            reader = csv.DictReader(f2)
            for row in reader:
                if(not row[header[0]] in complete_ids):
                    writer.writerow(row)
    except FileNotFoundError as fnf_error:
        print(fnf_error)


def delete_from_complete(delete_ids, complete_name, header):
    try:
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
    except FileNotFoundError as fnf_error:
        print(fnf_error)

def get_input():
    print("What would you like to do today?")
    print("Enter 'a' for add entries, 'd' for delete entries, and 'c' for cancel")
    mode = input()
    if mode == 'c':
        return
    print("What's the path to the complete csv of entries?")
    complete = input()
    ids_present, header = get_ids_header(complete)
    if mode == 'a':
        print("What's the path to the csv of entries to add?")  
        add = input()
        add_to_complete(add, complete, ids_present, header)
        print("Adding successful")
    elif mode == 'd':
        print("What's the path to the csv of entries to delete?")
        delete = input()
        print("Are you sure you want to delete %s (y/n)? This action cannot be undone." %(delete))
        confirm = input()
        if confirm == 'y':
            ids_to_delete = get_ids_header(delete)[0]
            delete_from_complete(ids_to_delete, complete, header)
            print("Deleting succesful")
        elif confirm == 'n':
            return
        else:
            print("Input not valid, try again")
            get_input()
    else:
        print("Input not valid, please try again")
        get_input()

if __name__ == "__main__":
    get_input()