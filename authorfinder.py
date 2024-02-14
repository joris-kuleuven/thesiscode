from github import Github
from config import githubToken
def find_github_user(full_name, access_token):
    g = Github(access_token)
    # Search for users based on the provided full name
    users = g.search_users(full_name)
    # Extract the first user (assuming it's the most relevant one)
    user = users[0] if users.totalCount > 0 else None
    return user.login if user else None

# Example usage:
full_name = "Matthias Schuhmayer"
access_token = githubToken

github_user = find_github_user(full_name, access_token)
if github_user:
    github_username = github_user.login
    print(f"The GitHub username for {full_name} is: {github_username}")
else:
    print(f"No GitHub user found for the name: {full_name}")
