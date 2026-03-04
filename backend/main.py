from fastapi import FastAPI, UploadFile, File
import PyPDF2
import sys
sys.path.append('../ai-engine')  

from skill_detector import detect_skills

app = FastAPI()

# Basic endpoint to check if the backend is running
@app.get("/")
def home():
    return {"message": "SkillGuard AI Backend Running"}

# Endpoint to upload a resume and extract text from it
@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    
    text = ""

    pdf_reader = PyPDF2.PdfReader(file.file)

    for page in pdf_reader.pages:
        text += page.extract_text()

    skills = detect_skills(text)    


    return {"skills_detected": skills}