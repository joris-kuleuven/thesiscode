import json
import requests
from tqdm import tqdm

# Your GitHub token
token = "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"

# Open the input file and load the data
with open('typescript_bv.json', 'r') as f:
    data = json.load(f)

# Set the headers for the API request
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

# Prepare the output data
output_data = []

for item in tqdm(data):
    # Create a new item with all fields from the input item
    new_item = item.copy()

    # If the item has commit URLs
    if 'commit_id' in item:
        # For each commit URL
        for commit_url in item['commit_id']:
            # Convert the commit URL to the API URL
            api_url = commit_url.replace("github.com", "api.github.com/repos").replace("commit", "commits")

            # Make the API request
            response = requests.get(api_url, headers=headers)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                commit_data = response.json()

                # Get the number of added and removed lines from the stats
                added_lines = commit_data["stats"]["additions"]
                removed_lines = commit_data["stats"]["deletions"]

                # Append the number of added and removed lines to the new item
                new_item['added_lines'] = added_lines
                new_item['removed_lines'] = removed_lines

    # Append the new item to the output data
    output_data.append(new_item)

# Save the output data to a new JSON file
with open('bv_extended.json', 'w') as f:
    json.dump(output_data, f, indent=4)