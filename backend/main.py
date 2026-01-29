import requests
from fastapi import FastAPI, UploadFile, File
import base64

app = FastAPI()

HF_API_URL = "https://supreetgupta5-ai-image-enhancer.hf.space/run/predict"

@app.post("/enhance")
async def enhance_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    payload = {
        "data": [
            f"data:image/png;base64,{image_base64}"
        ]
    }

    response = requests.post(HF_API_URL, json=payload)

    if response.status_code != 200:
        return {"error": "HF Space error"}

    result_base64 = response.json()["data"][0].split(",")[1]
    result_bytes = base64.b64decode(result_base64)

    return {
        "image": base64.b64encode(result_bytes).decode("utf-8")
    }
