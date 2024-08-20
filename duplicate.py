import csv

# Prompt the user to input the name of the CSV file to open
csv_file_name = input("Please enter the name of the CSV file to open (e.g., 'output.csv'): ")

# Function to remove duplicates from a list
def remove_duplicates(data_list):
    return list(set(data_list))

# Read the contents of the CSV file
try:
    with open(csv_file_name, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        data_list = [row[0] for row in reader]  # Assuming each row contains a single column
except FileNotFoundError:
    print(f"File '{csv_file_name}' not found.")
    exit()

# Remove duplicates from the list
unique_data_list = remove_duplicates(data_list)

# Write the unique entries back to the same CSV file, replacing the original contents
with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    for item in unique_data_list:
        writer.writerow([item])

print(f"Duplicates have been removed and the file '{csv_file_name}' has been updated successfully.")