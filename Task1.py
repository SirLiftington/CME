import csv

def find_species_with_largest_length(file_path):
    #Initialize variables to track legnth of the species
    max_length = 0
    species_with_max_length = None
    
    #Open csv file for reading
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)

        #iterate through rows of csv
        for row in reader:
            species = row.get('species')
            length = float(row.get('length')[:-1]) if row.get('length') else 1.0  # Assuming if length is not provided, it's 1.0m
            #update max legth and species if current legnth is greater
            if length > max_length:
                max_length = length
                species_with_max_length = species
    
    return species_with_max_length

if __name__ == "__main__":
    file_path = 'dinosaurs.csv' # path to CSV file
    species_with_largest_length = find_species_with_largest_length(file_path)
    print(species_with_largest_length)
