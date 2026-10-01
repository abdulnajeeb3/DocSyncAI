# Copy this file to config/pinecone_config.py and fill in your own key.
# config/pinecone_config.py is gitignored so the real key is never committed.
import os

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY", "your-pinecone-api-key")
