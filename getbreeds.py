# import csv
# import json

# # Load the JSON file
# with open('response.json', 'r') as json_file:
#     data = json.load(json_file)

# breeds = data['breeds']  # Extract the "breeds" array from the JSON

# # Extract names from breed objects
# names = [breed['name'] for breed in breeds]

# # Write names to CSV file
# with open('breeds.csv', 'w', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['Name'])  # Write header
#     writer.writerows([[name] for name in names])  # Write names as rows

# print(f'Successfully written {len(names)} names to breeds.csv')
import csv

import csv

def find_repeated_unique_words(file_path, column_name):
    repeated_unique_words = []
    unique_words = set()
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            words = row[column_name].split()
            for word in words:
                if word in unique_words and word not in repeated_unique_words:
                    repeated_unique_words.append(word)
                else:
                    unique_words.add(word)
    
    return repeated_unique_words

# Example usage
file_path = 'breeds.csv'  # Replace with your CSV file path
column_name = 'Name'  # Replace with the name of the column to check for repeated unique words
repeated_unique_words = find_repeated_unique_words(file_path, column_name)
print("Repeated unique words:", repeated_unique_words)
