from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
import base64
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # 🔒 Load .env variables

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HF_API_URL = "https://api-inference.huggingface.co/models/OttoYu/TreeClassification"
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_data = await file.read()
    base64_image = base64.b64encode(image_data).decode("utf-8")

    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        HF_API_URL,
        headers=headers,
        json={"inputs": {"image": base64_image}}
    )

    if response.status_code != 200:
        return {"error": "Failed to get prediction from Hugging Face API", "details": response.text}

    result = response.json()
    try:
        label = result[0]["label"]
    except Exception:
        label = "ไม่สามารถจำแนกได้"

    return {"label": label}
