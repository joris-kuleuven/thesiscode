import json
import csv

output_file = 'repositories.csv'

def url_exists_in_csv(url, filename='repositories.csv'):
    # Check if the URL is already in the CSV file
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['URL'] == url:
                return True
    return False

def append_url_to_csv(url_in):
    # Check if the URL is already in the CSV
    if not url_exists_in_csv(url_in):
        # Open the CSV file in append mode or create it if it doesn't exist
        with open('repositories.csv', 'a', newline='') as csvfile:
            fieldnames = ['URL']  # Define the column names

            # Create a CSV writer object
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the URL to the CSV file
            writer.writerow({'URL': url_in})

#First write header row
with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["URL"])


# Open and read the JSON file
with open('output.json', 'r') as json_file:
    data = json.load(json_file)

# Iterate through the JSON data and print URLs with the structure "https://github.com/xxx/yyy"
for cve, cve_data in data.items():
    references = cve_data.get("References", [])
    for reference in references:
        url = reference.get("url", "")
        if url.startswith("https://github.com/"):
            parts = url.split("/")
            if len(parts) >= 5:  # Ensure there are at least 4 parts (https:, , github.com, xxx)
                github_url = "/".join(parts[:5])
                print(github_url)
                append_url_to_csv(github_url)
