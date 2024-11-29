from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
import os
from pathlib import Path

app = FastAPI()

# Create images directory if it doesn't exist
IMAGES_DIR = Path("images")
IMAGES_DIR.mkdir(exist_ok=True)

@app.get("/")
async def root():
    return {"message": "Image API Server"}

@app.get("/images/{image_name}")
async def get_image(image_name: str):
    image_path = IMAGES_DIR / image_name
    if not image_path.exists():
        return {"error": "Image not found"}, 404
    return FileResponse(image_path)