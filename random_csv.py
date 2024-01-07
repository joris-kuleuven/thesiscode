import csv
import random

# Function to generate random data
def generate_random_data():
    name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    age = random.randint(18, 65)
    score = round(random.uniform(50, 100), 2)
    return [name, age, score]

# Function to create and write data to a CSV file
def create_csv_file(filename, num_records):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Score"])
        
        for _ in range(num_records):
            data = generate_random_data()
            writer.writerow(data)

if __name__ == "__main__":
    output_file = "random_data.csv"  # Name of the output CSV file
    num_records = 10  # Number of random records to generate

    create_csv_file(output_file, num_records)
    print(f"CSV file '{output_file}' with {num_records} random records has been created.")
