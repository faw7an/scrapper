# import csv
# from collections import Counter

# # Function to read CSV file and return a list of its contents
# def read_csv(file_name):
#     try:
#         with open(file_name, 'r', encoding='utf-8') as csv_file:
#             reader = csv.reader(csv_file)
#             return [row[0] for row in reader]  # Assuming each row contains a single column
#     except FileNotFoundError:
#         print(f"File '{file_name}' not found.")
#         return []

# # Prompt the user to input the names of the CSV files to be opened
# csv_files = input("Please enter the names of the CSV files to be opened, separated by commas: ").split(',')

# # Read the contents of each specified CSV file
# all_data = []
# for file_name in csv_files:
#     file_name = file_name.strip()  # Remove any leading/trailing whitespace
#     all_data.extend(read_csv(file_name))

# # Count the occurrences of each entry
# data_counter = Counter(all_data)

# # Filter entries that appear more than once
# duplicate_entries = {item: count for item, count in data_counter.items() if count > 1}

# # Write the duplicate entries and their counts to a new CSV file named 'trace.csv'
# with open('trace.csv', 'w', newline='', encoding='utf-8') as trace_file:
#     writer = csv.writer(trace_file)
#     writer.writerow(['Entry', 'Count'])  # Write header
#     for item, count in duplicate_entries.items():
#         writer.writerow([item, count])

# print("Duplicate entries have been written to 'trace.csv' successfully.")

import csv
from collections import Counter

# Function to read CSV file and return a list of its contents
def read_csv(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            return [row[0] for row in reader]  # Assuming each row contains a single column
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []

# Prompt the user to input the names of the CSV files to be opened
csv_files = input("Please enter the names of the CSV files to be opened, separated by commas: ").split(',')

# Read the contents of each specified CSV file
all_data = []
for file_name in csv_files:
    file_name = file_name.strip()  # Remove any leading/trailing whitespace
    all_data.extend(read_csv(file_name))

# Count the occurrences of each entry
data_counter = Counter(all_data)

# Filter entries that appear more than once
duplicate_entries = {item: count for item, count in data_counter.items() if count > 1}

# Sort the duplicate entries by count in descending order
sorted_duplicates = sorted(duplicate_entries.items(), key=lambda x: x[1], reverse=True)

# Write the sorted duplicate entries and their counts to a new CSV file named 'trace.csv'
with open('trace.csv', 'w', newline='', encoding='utf-8') as trace_file:
    writer = csv.writer(trace_file)
    writer.writerow(['Entry', 'Count'])  # Write header
    for item, count in sorted_duplicates:
        writer.writerow([item, count])

print("Duplicate entries have been written to 'trace.csv' successfully.")