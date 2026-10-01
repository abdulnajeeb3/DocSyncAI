from git import Repo

def get_diff(repo_path):
    try:
        repo = Repo(repo_path)
        diff = repo.git.diff('HEAD~1..HEAD')
        
        print("Diff detected successfully")
        print(diff)
        return diff
    except Exception as e:
        print(f"Error getting diff: {e}")
        return None
