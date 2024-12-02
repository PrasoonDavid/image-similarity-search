import json
import os
from pathlib import Path
import requests
from PIL import Image
from io import BytesIO
from .embedding_service import EmbeddingService
from repository.image_repository import ImageRepository
import requests
from dto.b2b_image_api_response import B2BAPIResponse
from typing import List, Optional, Dict

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
    def store_embeddings_algolia(self):
        page_no = 0
        co = 0
        # self.call_external_api(page_no,12)
        return self.store_embeddings_from_array()

    def call_external_api(self,page_no,page_size):
        try:
            # Define the URL
            url = "https://jmd-b2b.jiox5.de/api/service/application/catalog/v1.0/products/?page_id=%2A&page_size=5000"

            # Define the query parameters
            # params = {
            #     "page_no": page_no,
            #     "page_size": page_size,
            #     "page_type": "number"
            # }

            # Define the headers
            headers = {
                "Accept": "application/json, text/plain, */*",
                "Cookie": ("anonymous_id=41b463c5e94743f7843f288a2a3bf72c; old_browser_anonymous_id=41b463c5e94743f7843f288a2a3bf72c; _fw_crm_v=4a1a139b-c264-4b4e-bc14-1de9bf662f27; f.session=s%3Aedeym-Ue5YEgTuMx97U_LCM50n0N4C7D.JHJw%2BMm99xclf8AdsmpYxWV4bCiRgnJuagT3mHr%2B1GY; token=Bearer%20eyJhbGciOiJIUzI1NiJ9.eyJsYXN0TmFtZSI6IkRBVklEIiwic3ViIjoiMjkzMjAxIiwibW9iaWxlIjoiOTE3OTkyMjE1NzEzIiwiYXBwcm92ZWRBdCI6bnVsbCwidHlwZSI6IlJldGFpbGVyIiwidXNlckxvZ2luIjoiSk0xMjM0MTIzNCIsImZpcnN0TmFtZSI6IlBSQVNPT04iLCJ0ZW5hbnROYW1lIjoiSk1EIiwiZ3N0biI6IjI3Qk1CUFM5OTAySDFaUiIsImRlcGFydG1lbnROdW1iZXIiOiJSMyIsInRlbmFudElkIjoiNjQ4NmNlMzY1MTVhZTcxNDUwMzlmNmE4IiwicHJtSWQiOiJKTTEyMzQxMjM0IiwicGFuIjoiRVNJUFM5NzIzTiIsImV4cCI6MTczMTk1NDA5OSwiaWF0IjoxNzMxOTE4MDk5LCJlbWFpbCI6ImltZGF2aWRyb2NrQGdtYWlsLmNvbSIsInN0b3JlQ29kZSI6IkpNMTIzNDEyMzQifQ.oAnEy7MX6UscQQmoca_QuYq6e1EDgxrt8Y81Yu_yomA; authorization=eyJhbGciOiJIUzI1NiJ9.eyJsYXN0TmFtZSI6IkRBVklEIiwic3ViIjoiMjkzMjAxIiwibW9iaWxlIjoiOTE3OTkyMjE1NzEzIiwiYXBwcm92ZWRBdCI6bnVsbCwidHlwZSI6IlJldGFpbGVyIiwidXNlckxvZ2luIjoiSk0xMjM0MTIzNCIsImZpcnN0TmFtZSI6IlBSQVNPT04iLCJ0ZW5hbnROYW1lIjoiSk1EIiwiZ3N0biI6IjI3Qk1CUFM5OTAySDFaUiIsImRlcGFydG1lbnROdW1iZXIiOiJSMyIsInRlbmFudElkIjoiNjQ4NmNlMzY1MTVhZTcxNDUwMzlmNmE4IiwicHJtSWQiOiJKTTEyMzQxMjM0IiwicGFuIjoiRVNJUFM5NzIzTiIsImV4cCI6MTczMTk1NDA5OSwiaWF0IjoxNzMxOTE4MDk5LCJlbWFpbCI6ImltZGF2aWRyb2NrQGdtYWlsLmNvbSIsInN0b3JlQ29kZSI6IkpNMTIzNDEyMzQifQ.oAnEy7MX6UscQQmoca_QuYq6e1EDgxrt8Y81Yu_yomA; x.session=s%3A2RkZNeXpflJ6uQlNlwlVowLBcw_jvSZs.Ok%2BJkc0frDT5SR9QodeNTSYYqcAY%2FnrhBNjhCEBq8yY; company_id=2769; _dd_s=logs=1&id=f895d844-4c04-4857-adda-00bba3c5bf20&created=1733070197346&expire=1733071477908"),
                "x-fp-date": "20241201T162938Z",
                "x-fp-sdk-version": "1.4.8-alpha.1720434476",
                "x-fp-signature":"v1.1:c1758e1b5021a59a008f50c485106996f4c038b9327ea64f0a502d69b9b0b9d8",
                "Authorization": "Bearer NjJiMmZiOGVkYzk1NzlkZDkzNGYzZDlmOmRQQW5hTUdWZA==",
            }
            # Make the GET request
            response = requests.get(url, headers=headers)

            # Check the response
            if response.status_code == 200:
                json_data = response.json()  # Parse JSON response
                api_response = B2BAPIResponse.parse_obj(json_data)  # Deserialize to APIResponse class
                return api_response
                # Access data
                # print(f"Total items: {api_response.page.item_total}")
                # for product in api_response.items:
                #     product.medias[0].url
                #     print(f"Product Name: {product.name}, Brand: {product.brand.name if product.brand else 'Unknown'}")
            else:
                print(f"Failed to fetch data: {response.status_code}")
        except Exception as e:
            raise Exception(f"Error in calling image api: {str(e)}")
    
    def store_embeddings_from_array(self):
        with open('./dto/b2b_response.json', 'r') as file:
            data = json.load(file)
        # Extract all `medias.url`

        co = 0
        for item in data.get('items', []):  # Iterate over items
            url = item.get('medias', [{}])[0].get('url')  # Safely access `medias`
            name = item.get('name')
            product_id = item.get('item_code')
            
            if not url or not name or not product_id:
                print(f"Skipping item due to missing data: {item}")
                continue
            
            try:
                # Generate embedding from the image URL
                embedding = self.embeddingservice.generate_embedding(self.load_image_from_url(url))
                
                # Prepare metadata as a single dictionary
                metadata = {
                    "name": name,
                    "url": url
                }
                
                # Add the embedding, id, and metadata
                self.image_repository.add_embedding(product_id, metadata, embedding)
                co= co+1
            except Exception as e:
                print(f"Error processing {name}: {str(e)}")
                continue
        return co

