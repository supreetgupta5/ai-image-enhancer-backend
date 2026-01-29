from fastapi import FastAPI, File, UploadFile
import subprocess
import uuid
import os

app = FastAPI()

@app.post("/enhance")
async def enhance_image(file: UploadFile = File(...)):
    input_path = f"input_{uuid.uuid4()}.png"
    output_path = f"output_{uuid.uuid4()}.png"

    with open(input_path, "wb") as f:
        f.write(await file.read())

    subprocess.run([
        "realesrgan-ncnn-vulkan",
        "-i", input_path,
        "-o", output_path,
        "-s", "2"
    ])

    return {"enhanced_image": output_path}
