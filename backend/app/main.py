from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "VisionLab Backend is Running! 🚀"}

@app.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
    # Placeholder: logic to process image will go here later
    return {
        "filename": file.filename, 
        "content_type": file.content_type,
        "status": "Received"
    }
