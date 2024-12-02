import chromadb

class ImageRepository:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.client.get_or_create_collection(
            name="product_search",
            embedding_function=None  # Use this to manually provide embeddings
            )
    
    def query_embedding(self, query_embeddings, top_k=5):
        """Query similar embeddings"""
        return self.collection.query(
            query_embeddings=[query_embeddings],
            n_results=top_k
        )
    
    def delete_embedding(self, ids):
        """Delete embeddings by IDs"""
        return self.collection.delete(ids=ids)
    
    def add_embedding(self,product_id, metadatas, embedding):
        self.collection.add(
            ids=[product_id],  # Unique identifier for the product
            embeddings=[embedding],
            metadatas=metadatas # Additional metadata
            )