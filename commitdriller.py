from pydriller import GitRepository
from urllib.parse import urlparse, unquote
import os

def analyze_commit(url):
    # Parse the URL to get the repository and commit hash
    parsed_url = urlparse(url)
    commit_hash = os.path.basename(parsed_url.path)
    repo_url = 'https://github.com' + os.path.dirname(parsed_url.path)

    # Use PyDriller to analyze the commit
    gr = GitRepository(repo_url)
    commit = gr.get_commit(commit_hash)
    modifications = commit.modifications
    files_changed = len(modifications)
    lines_added = sum(mod.added for mod in modifications)
    lines_deleted = sum(mod.removed for mod in modifications)

    print(f'Commit {commit_hash} in repository {repo_url} changed {files_changed} files')
    print(f'Total lines added: {lines_added}')
    print(f'Total lines deleted: {lines_deleted}')

    # Developer information
    print(f'Commit author: {commit.author.name}')
    print(f'Author email: {commit.author.email}')

# Test the function with a commit URL
analyze_commit('https://github.com/ishepard/pydriller/commit/4a8b6e6e68577e6a0f3a7590298e6709d6db70db')