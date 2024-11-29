from fastapi import APIRouter, HTTPException
from typing import List, Optional, Dict
from services.images_service import ImageService

router = APIRouter()
image_service = ImageService()

@router.post("/images/")
async def create_embeddings(texts: List[str], metadata: Optional[List[Dict]] = None, ids: Optional[List[str]] = None):
    try:
        # result = embedding_repository.store_embeddings(texts, metadata, ids)
        image_service.store_embeddings
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/images/search/")
async def search_embeddings(query: str, n_results: int = 5):
    try:
        result = embedding_repository.search_similar(query, n_results)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
