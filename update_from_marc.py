from pymarc import MARCReader
import csv

def to_add(filename):
    with open(filename, 'rb') as f:
        rows = []
        reader = MARCReader(f)
        for record in reader:
            row = [record['001'].value(), 
                   record['035']['a'], 
                   record['245']['a'], 
                   record['245']['c'], 
                   record['852']['h'],
                   record['852']['b'],
                   record['856']['u']]
            rows.append(row)
    return rows

add_file = "test_data/test_add_file.mrc"
add_records = to_add(add_file)
print(add_records[0])