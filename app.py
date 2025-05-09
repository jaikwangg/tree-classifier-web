# backend/app.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
from PIL import Image
import torch
import io

app = FastAPI()

# Allow CORS (adjust for your frontend domain if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and feature extractor once
model_name = "OttoYu/TreeClassification"
model = AutoModelForImageClassification.from_pretrained(model_name)
extractor = AutoFeatureExtractor.from_pretrained(model_name)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data)).convert("RGB")

    inputs = extractor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
        label = model.config.id2label[predicted_class_idx]

    return {"label": label}
