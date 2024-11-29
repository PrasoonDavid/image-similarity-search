from fastapi import APIRouter, HTTPException
from typing import List, Optional, Dict
from repository.embedding_repository import EmbeddingRepository

router = APIRouter()
embedding_repository = EmbeddingRepository()

@router.post("/embeddings/")
async def create_embeddings(texts: List[str], metadata: Optional[List[Dict]] = None, ids: Optional[List[str]] = None):
    try:
        result = embedding_repository.store_embeddings(texts, metadata, ids)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/embeddings/search/")
async def search_embeddings(query: str, n_results: int = 5):
    try:
        result = embedding_repository.search_similar(query, n_results)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/embeddings/{ids}")
async def delete_embeddings(ids: List[str]):
    try:
        result = embedding_repository.remove_embeddings(ids)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))