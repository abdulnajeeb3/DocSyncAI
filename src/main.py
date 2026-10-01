import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from clone_repo import clone_repo
from diff_detector import get_diff
from static_analysis import parse_diff
from embedding_indexer import initialize_pinecone, index_documentation
from documentation_updater import update_documentation
from sentence_transformers import SentenceTransformer
from config.pinecone_config import PINECONE_API_KEY

def main():
    repo_url = 'https://github.com/abdulnajeeb3/car-data-explorer'
    repo_path = 'cloned_repo'

    print("Starting DocSync AI")

    # Step 1: Clone the GitHub Repository
    repo = clone_repo(repo_url, repo_path)
    if not repo:
        print("Failed to clone or update the repository")
        return

    # Step 2: Detect Changes
    diff = get_diff(repo_path)
    if not diff:
        print("No differences detected")
        return

    # Step 3: Static Analysis to Find Changed Functions
    changed_functions = parse_diff(diff)
    if not changed_functions:
        print("No changed functions detected")
        return

    # Step 4: Initialize Model and Pinecone
    model = SentenceTransformer('all-MiniLM-L6-v2')
    index = initialize_pinecone(PINECONE_API_KEY)
    if not index:
        print("Failed to initialize Pinecone")
        return

    # Step 5: Index Documentation
    index_documentation(repo_path, model, index)

    # Step 6: Query Documentation and Suggest Updates
    update_documentation(changed_functions, model, index)

if __name__ == '__main__':
    main()
