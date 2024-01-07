import requests

# Define the URL of the repository's releases
url = "https://api.github.com/repos/{owner}/{repo}/releases"

# Replace {owner} and {repo} with the owner and name of the repository
url = url.format(owner="grafana", repo="grafana")

# Send a GET request to the GitHub API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Print the tag name (version) of each release
    for release in data:
        print(release['tag_name'])
else:
    print("Failed to fetch data:", response.status_code)