# Image API Server

This is a simple FastAPI server that serves images through an API.

## Setup
0. Setup environment
```bash
python3 -m venv imageSolServerEnv
source imageSolServerEnv/bin/activate
```

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn main:app --reload
```

## API Endpoints

- `GET /`: Returns a welcome message
- `GET /images/{image_name}`: Returns the requested image file

## Usage

1. Place your images in the `images` directory
2. Access images through: `http://localhost:8000/images/your_image.jpg`