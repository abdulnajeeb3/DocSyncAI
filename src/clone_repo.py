import os
from git import Repo

def clone_repo(repo_url, repo_path='repo'):
    try:
        if os.path.exists(repo_path):
            repo = Repo(repo_path)
            repo.remotes.origin.pull()
        else:
            repo = Repo.clone_from(repo_url, repo_path)
        print(f"Repository cloned or updated at {repo_path}")
        return repo
    except Exception as e:
        print(f"Error cloning or updating the repo: {e}")
        return None
