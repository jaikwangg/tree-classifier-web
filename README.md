<<<<<<< HEAD
# tree-classifier-web
=======
# 🌳 Tree Classification API (Lightweight via Hugging Face)

This is a lightweight FastAPI backend that sends images to Hugging Face Inference API to classify tree species using the `OttoYu/TreeClassification` model.

## ✅ Features

- Accepts image uploads via `/predict` endpoint
- Converts image to base64 and sends to Hugging Face
- Returns the predicted tree species
- Uses `.env` for secure API token management

## 🚀 Quickstart

1. Clone this repository
2. Create `.env` file:
   ```
   HF_API_TOKEN=your_huggingface_token_here
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the API:
   ```
   uvicorn app:app --reload
   ```

## 🔒 .env format

```bash
HF_API_TOKEN=hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## 📦 Dependencies

- FastAPI
- Uvicorn
- Pillow
- Requests
- python-dotenv

## 📸 API Usage

**POST /predict**

- `file`: image file (`.jpg`, `.png`, etc.)
- Response:
```json
{ "label": "Terminalia mantaly" }
```

## 🧠 Model

Powered by [OttoYu/TreeClassification](https://huggingface.co/OttoYu/TreeClassification) on Hugging Face.
>>>>>>> 7e0a396 (Update api)
