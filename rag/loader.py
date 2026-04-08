import os
import json
from config import DOCUMENTS_DIR
from typing import Dict, Any

def load_documents() -> Dict[str, Dict[str, Any]]:
    """
    Loads all .txt files from the documents directory and their accompanying metadata.
    Returns: { "filename.txt": {"content": "...", "metadata": ["keyword1", ...]} }
    """
    documents = {}
    if not os.path.exists(DOCUMENTS_DIR):
        print(f"Warning: Directory {DOCUMENTS_DIR} does not exist.")
        return documents

    # Load metadata.json if exists
    metadata = {}
    metadata_path = os.path.join(DOCUMENTS_DIR, "metadata.json")
    if os.path.exists(metadata_path):
        try:
            with open(metadata_path, "r", encoding="utf-8") as fm:
                metadata = json.load(fm)
        except Exception as e:
            print(f"Error reading metadata.json: {e}")

    for filename in os.listdir(DOCUMENTS_DIR):
        if filename.endswith(".txt"):
            filepath = os.path.join(DOCUMENTS_DIR, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    file_meta = metadata.get(filename, [])
                    documents[filename] = {
                        "content": content,
                        "metadata": [m.lower() for m in file_meta]
                    }
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                
    return documents
