# https://pygithub.readthedocs.io/en/stable/examples/Repository.html
from github import Github
# Authentication is defined via github.Auth
from github import Auth
from config import githubToken
# using an access token


# Public Web Github
g = Github(githubToken)

repo_url = "PyGithub/PyGithub"
def getMilestones():
    repo = g.get_repo(repo_url)
    open_milestones = repo.get_milestones(state='open')
    for milestone in open_milestones:
        print(milestone)

def getOpenIssues():
    repo = g.get_repo("PyGithub/PyGithub")
    open_issues = repo.get_issues(state='open')
    for issue in open_issues:
        print(issue)

#getOpenIssues()
user = g.get_user()
user.login