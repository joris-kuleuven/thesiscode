from pydriller import Repository
import csv
repo_url = 'https://github.com/twisted/treq'
index=0
with open('gitinfo.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["Index", "Message", "Author"])
	for commit in Repository(repo_url).traverse_commits():
		#print(commit.hash)
		#print(commit.msg)
		#print(commit.author.name)
		print(index)
		writer.writerow([index, commit.msg, commit.author.name])
		index+=1;
	#for file in commit.modified_files:
	#	print(file.filename, ' has changed')
