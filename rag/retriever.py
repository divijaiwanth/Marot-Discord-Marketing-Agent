from typing import Dict, Any, List

def retrieve_relevant_docs(query: str, documents: Dict[str, Dict[str, Any]], top_k: int = 2) -> str:
    """
    Metadata/Keyword based retriever.
    Scores documents strictly based on metadata keyword hits rather than full text scanning for faster inference.
    Returns a unified string of the highest scoring documents' content.
    """
    query_words = set(query.lower().split())
    doc_scores = []
    
    for filename, data in documents.items():
        score = 0
        metadata = data.get("metadata", [])
        content = data.get("content", "")
        
        # Fast scoring against metadata array
        for word in query_words:
            if len(word) > 3 and word in metadata:
                score += 1
                
        # If no metadata exists, fallback to full text matching
        if not metadata:
            doc_lower = content.lower()
            for word in query_words:
                if len(word) > 3 and word in doc_lower:
                    score += 1
                    
        doc_scores.append((score, filename, content))
        
    # Sort docs by score descending
    doc_scores.sort(key=lambda x: x[0], reverse=True)
    
    # Grab the top_k
    top_docs = doc_scores[:top_k]
    
    # If no docs match at all, we can fallback to the general company overview or return empty
    # For now, let's just return the highest score docs even if the score is 0,
    # or if score is 0 we return empty. Let's just return what we have (with score > 0).
    
    relevant_texts = []
    for score, fname, content in top_docs:
        if score > 0 or len(documents) <= top_k: # ensure some context if small corpus
            relevant_texts.append(f"--- Document Source: {fname} ---\n{content}")
            
    if not relevant_texts:
        return "No specific company knowledge retrieved."
        
    return "\n\n".join(relevant_texts)
