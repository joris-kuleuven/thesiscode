# https://pygithub.readthedocs.io/en/stable/examples/Repository.html
from github import Github
# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token("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")

# Public Web Github
g = Github(auth=auth)

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