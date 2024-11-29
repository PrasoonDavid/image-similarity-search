from embedding_service import EmbeddingService
import os
from pathlib import Path
class ImageService:
    def __init__(self) -> None:
        self.embedding_service = EmbeddingService()
    def store_embeddings(self, image, metadata=None, ids=None):
        # generate image embedding
        images_dir = "../images"
        for image_file in os.listdir(images_dir):
            # Only process .jpg files
            if image_file.endswith(".jpg"):
                # Extract product ID from the filename (without the extension)
                product_id = Path(image_file).stem
                product_name = product_id.replace("_", " ").title()  # Example name formatting (adjust if needed)

                # Get the full path to the image
                image_path = os.path.join(images_dir, image_file)
                
                embedding = generate_embedding(image_path)
                store_embedding(product_id, product_name, embedding)

        # Store the embedding
        return self.embedding_service.generate_embedding(image)