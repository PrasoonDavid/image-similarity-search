import os
from pathlib import Path
import requests
from PIL import Image
from io import BytesIO
from .embedding_service import EmbeddingService
from repository.image_repository import ImageRepository



class ImageService:
    def __init__(self, images_dir="./images"):
        self.embeddingservice = EmbeddingService()
        self.image_repository = ImageRepository()
        self.images_dir = Path(images_dir).resolve()  # Convert to absolute path
        
    def store_embeddings(self, image, metadata=None, ids=None):
        try:
            # Check if directory exists
            if not self.images_dir.exists():
                raise FileNotFoundError(f"Images directory not found: {self.images_dir}")
                
            for image_file in os.listdir(self.images_dir):
                if image_file.endswith(".jpg"):
                    product_id = Path(image_file).stem
                    product_name = product_id.replace("_", " ").title()
                    
                    image_path = os.path.join(self.images_dir, image_file)
                    
                    try:
                        embedding = self.embeddingservice.generate_embedding_image_path(image_path)
                        self.image_repository.add_embedding(product_id, product_name, embedding)
                    except Exception as e:
                        print(f"Error processing {image_file}: {str(e)}")
                        continue
                        
        except Exception as e:
            raise Exception(f"Error in store_embeddings: {str(e)}")
    
    def search_similar(self, image_url, n_results=5):
        try:
            query = self.load_image_from_url(image_url)
            query_embedding = self.embeddingservice.generate_embedding(query)
            return self.image_repository.query_embedding(query_embedding, n_results)
        except Exception as e:
            raise Exception(f"Error in search_similar: {str(e)}")
    
    def load_image_from_url(self, image_url):
        try:
            response = requests.get(image_url, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes
            img = Image.open(BytesIO(response.content)).convert("RGB")
            return img
        except requests.RequestException as e:
            raise Exception(f"Error loading image from URL: {str(e)}")
        except Exception as e:
            raise Exception(f"Error processing image: {str(e)}")