import json

with open('typescript_bv.json') as f:
    data = json.load(f)

commit_url_count = 0

for item in data:
    if 'commit_id' in item:
        commit_url_count += len(item['commit_id'])

print('Total number of commit URLs:', commit_url_count)