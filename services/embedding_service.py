import chromadb
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

class EmbeddingService:
    def __init__(self):
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    
    # Function to generate embeddings
    def generate_embedding(image_path):
        image = Image.open(image_path).convert("RGB")
        inputs = processor(images=image, return_tensors="pt", padding=True)
        with torch.no_grad():
            embeddings = model.get_image_features(**inputs)
        # Normalize the embeddings for better search results
        normalized_embeddings = embeddings / embeddings.norm(dim=-1, keepdim=True)
        return normalized_embeddings.squeeze().tolist()
