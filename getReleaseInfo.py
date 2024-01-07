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

    # Print information for each release
    for release in data:
        if release['tag_name'] == 'v10.0.4':
            print('Name:', release['name'])
            #print('Published at:', release['published_at'])
            #print('Description:', release['body'])
            print('URL:', release['html_url'])

            print('Assets:')
            for asset in release['assets']:
                print('  -', asset['name'])
                print('    Size:', asset['size'])
                print('    Download count:', asset['download_count'])
                print('    Download URL:', asset['browser_download_url'])
else:
    print("Failed to fetch data:", response.status_code)