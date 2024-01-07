import csv
from pydriller import Repository



def pydr_csv(url_in, index):
    filename = str(index) + '_repo.csv'
    row = 0
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Index", "Author", "Insertions", "Deletions"])
        for commit in Repository(url_in).traverse_commits():
            #print(row)
            writer.writerow([row, commit.author.name, commit.insertions, commit.deletions])
            row+=1

    #for file in commit.modified_files:
        #print(file.filename, ' has changed')

# Replace 'urls.csv' with the path to your CSV file
csv_file = 'urls.csv'
index=0

try:
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:  # Check if the row is not empty
                url = row[0]
                print(url)
                pydr_csv(url, index)
                index +=1
except FileNotFoundError:
    print(f"File '{csv_file}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

    #https://github.com/twisted/treq
#https://github.com/nRF24/RF24