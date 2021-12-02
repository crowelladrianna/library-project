import update_csv
import csv
import unittest

def csv_same(file1, file2):
    rows1 = []
    rows2 = []

    with open(file1, newline='') as f1, open(file2, newline='') as f2:
        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)
        for row in reader1:
            rows1.append(row)
        for row in reader2:
            rows2.append(row)
        if not len(rows1) == len(rows2):
            return False
        for i in range(len(rows1)):
            if not len(rows1[i]) == len(rows2[i]):
                return False
            for j in range(len(rows1[i])):
                if not rows1[i][j] == rows2[i][j]:
                    return False
    return True

class TestCSV(unittest.TestCase):
    def test_add_then_delete(self):
        complete_original = "test_data/test_complete_list_og.csv"

        add_file = "test_data/test_add_file.csv"
        complete_file = "test_data/test_complete_list.csv"
        ids_present, header = update_csv.get_ids_header(complete_file)
        ids_to_delete = update_csv.get_ids_header(add_file)[0]
        update_csv.add_to_complete(add_file, complete_file, ids_present, header)
        update_csv.delete_from_complete(ids_to_delete, complete_file, header)
        self.assertEqual(csv_same(complete_original, complete_file), True, "Adding and removing the same csv")

    def test_no_ids_repeated(self):
        add_file = "test_data/test_add_file.csv"
        complete_file = "test_data/test_complete_list.csv"
        ids_present, header = update_csv.get_ids_header(complete_file)
        update_csv.add_to_complete(add_file, complete_file, ids_present, header)
        ids = []
        ids_set = set()
        with open(complete_file, newline='') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                ids.append(row[0])
                ids_set.add(row[0])

        # deleting so complete stays consistent
        ids_to_delete = update_csv.get_ids_header(add_file)[0]
        update_csv.delete_from_complete(ids_to_delete, complete_file, header)

        self.assertEqual(len(ids), len(ids_set), "Only items with unique value in '1' column should be added")

    def test_correct_number_deleted(self):
        complete_file = "test_data/test_complete_list.csv"
        delete_file = "test_data/test_delete_file.csv"

        ids_present, header = update_csv.get_ids_header(complete_file)
        ids_to_delete = update_csv.get_ids_header(delete_file)[0]
        
        final_ids = ids_present - ids_to_delete

        update_csv.delete_from_complete(ids_to_delete, complete_file, header)
        ids_updated = update_csv.get_ids_header(complete_file)[0]

        update_csv.add_to_complete(delete_file, complete_file, ids_updated, header)

        self.assertSetEqual(final_ids, ids_updated, "Only items whose value in '1' column is not in the '1' column of the csv to delete should be present")

if __name__ == '__main__':
    unittest.main()

# add_file = "test_data/test_add_file.csv"
# complete_file = "test_data/test_complete_list.csv"
# complete_initial = "test_data/test_complete_list_og.csv"
# delete_file = "test_data/test_delete_file.csv"