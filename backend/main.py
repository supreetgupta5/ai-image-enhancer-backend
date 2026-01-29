from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uuid, shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "TEST MODE RUNNING"}

@app.post("/enhance")
async def enhance(file: UploadFile = File(...)):
    filename = f"output_{uuid.uuid4()}.png"
    with open(filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return FileResponse(filename, media_type="image/png")
