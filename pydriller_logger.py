import csv
from pydriller import Repository
import logging

csv_file = 'repositories.csv'
index = 0
iterations = 100

#logger config
logfile_name = 'pydriller_logger.log'
logging.basicConfig(filename=logfile_name, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def commit_traverser(url_in, num_iterations):
        try:
            i = 0
            print(f"cloning into "+url_in)
            for commit in Repository(url_in).traverse_commits():
                print(commit.files)
                i +=1
                if(i>num_iterations):
                    logging.info(f"successfully done repo {url_in} after {str(i)} iterations")
                    break
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            logging.error("Error on repo url_in"+url_in)
#MAIN
try:
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:  # Check if the row is not empty
                url = row[0]
                commit_traverser(url, iterations)
                index +=1
except FileNotFoundError:
    print(f"File '{csv_file}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")