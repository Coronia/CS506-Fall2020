import csv

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    res = []
    with open(csv_file_path, 'r') as file:
        lines = csv.reader(file)
        res = []
        for line in lines:
            for i in range(len(line)):
                if line[i].isdigit():
                    line[i] = int(line[i])
            res.append(line)
    return res
