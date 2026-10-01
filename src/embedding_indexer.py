from sentence_transformers import SentenceTransformer
import pinecone
import os

def initialize_pinecone(api_key):
    try:
        pinecone.init(api_key=api_key)
        index_name = 'documentation'
        
        if index_name not in pinecone.list_indexes():
            pinecone.create_index(
                name=index_name, 
                dimension=384, 
                metric='cosine'
            )
        index = pinecone.Index(index_name)
        print("Pinecone initialized and index created")
        return index
    except Exception as e:
        print(f"Error initializing Pinecone: {e}")
        return None

def index_documentation(repo_path, model, index):
    try:
        readme_path = os.path.join(repo_path, 'README.md')
        if not os.path.exists(readme_path):
            print(f"README.md not found at {repo_path}")
            return

        with open(readme_path, 'r') as f:
            readme_content = f.read()

        doc_embeddings = model.encode([readme_content])
        index.upsert(vectors=[('readme', doc_embeddings[0])])
        print("Documentation indexed successfully")
    except Exception as e:
        print(f"Error indexing documentation: {e}")
