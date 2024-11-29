from fastapi import FastAPI
from routes.embedding_routes import router as embedding_router

app = FastAPI()

app.include_router(embedding_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)