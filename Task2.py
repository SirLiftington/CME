import csv
from collections import defaultdict

def signature(name):
    """calculate signature, remove spaces, convert to lowercase and sort alphabetically"""
    return ''.join(sorted(set(name.replace(' ', '').lower())))

def group_dinosaurs(csv_file):
    """Group dinosaurs based on their signature"""
    groups = defaultdict(list)

    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            sig = signature(name)
            groups[sig].append(name)

    #Return groups with more than 1 Dino
    return [dinosaurs for dinosaurs in groups.values() if len(dinosaurs) > 1]

if __name__ == "__main__":
    result = group_dinosaurs('dinosaurs.csv')
    print(result)
