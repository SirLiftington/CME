# CME

This repository contains solutions for two coding challenges related to processing data from a CSV file containing information about dinosaurs.

Part 1: Species with the Largest Average Length
Task Description:
Given the provided CSV file, the task is to determine the species with the largest average length. If a length is not specified for a species, it is assumed to be 1.0 meters. If a species is not provided, the entire row can be ignored.

**Example Output:**
sanjuanensis


# Solution Overview (Task1.py):

find_species_with_largest_length(file_path): This function takes the file path of the CSV file as input and returns the species with the largest average length.
The CSV file is read using the csv.DictReader module.
The function iterates through each row of the CSV, calculates the length (assuming 1.0 meter if not provided), and updates the maximum length and corresponding species accordingly.
Finally, it returns the species with the largest average length.
Part 2: Group Dinosaurs by Letters
Task Description:
Given the same CSV file, this task involves grouping dinosaurs based on the letters used in their names. Dinosaurs with the same set of letters (ignoring spaces and case) are grouped together.

**Example Output:**
[['allosaurus', 'aralosaurus'], ['austrosaurus', 'torosaurus']]

# Solution Overview (Task2.py):

signature(name): This function calculates the signature of a dinosaur name by removing spaces, converting to lowercase, and sorting alphabetically.
group_dinosaurs(csv_file): This function groups dinosaurs based on their signatures and returns a list of lists where each sublist contains names of dinosaurs that can be made using the same letters.
The CSV file is read using csv.DictReader.
The function iterates through each row, calculates the signature of the dinosaur name, and groups them accordingly.
It returns the groups with more than one dinosaur.

**Running the Code:**
Ensure Python is installed on your system.
Execute Task1.py and Task2.py with the provided CSV file (dinosaurs.csv).
The output will be printed to the console.
