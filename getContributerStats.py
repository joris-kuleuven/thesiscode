import requests
from github import Github
from config import githubToken

def find_github_user(full_name, access_token):
    g = Github(access_token)
    # Search for users based on the provided full name
    users = g.search_users(full_name)
    # Extract the first user (assuming it's the most relevant one)
    user = users[0] if users.totalCount > 0 else None
    print(user.login)
    return user.login

def print_user_features(username):
    # Make a GET request to the GitHub API to retrieve user information
    response = requests.get(f"https://api.github.com/users/{username}")

    if response.status_code == 200:
        user_data = response.json()

        # Extract the desired user features
        name = user_data["name"]
        followers = user_data["followers"]
        following = user_data["following"]
        public_repos = user_data["public_repos"]
        stars = 0

        # Make a GET request to the GitHub API to retrieve the user's starred repositories
        response = requests.get(f"https://api.github.com/users/{username}/starred")

        if response.status_code == 200:
            starred_repos = response.json()
            stars = len(starred_repos)

        # Print the user features
        print(f"User: {name}")
        print(f"Followers: {followers}")
        print(f"Following: {following}")
        print(f"Public Repositories: {public_repos}")
        print(f"Stars: {stars}")
    else:
        print("Failed to retrieve user information.")

# Example usage
github_user = find_github_user("Matthias Schuhmayer", githubToken)
print_user_features(github_user)
