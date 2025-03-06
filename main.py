from fastapi import FastAPI, Request, File, UploadFile, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
import shutil
import pickle
import pandas as pd

app = FastAPI()

# Setting up templates
templates = Jinja2Templates(directory="templates")

# Serve static files (CSS, JS, Images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load the ATS Score Prediction Model
model_path = "ml_model/ats_model.pkl"
if os.path.exists(model_path):
    with open(model_path, "rb") as model_file:
        ats_model = pickle.load(model_file)
else:
    ats_model = None

@app.get("/")
async def home(request: Request):
    """ Serve the Landing Page """
    return templates.TemplateResponse("index.html", {"request": request, "title": "FastAPI Web Page"})

@app.get("/ats-score-check/")
async def ats_score_page(request: Request):
    """ Serve the ATS Score Check Page """
    return templates.TemplateResponse("ats_score_check.html", {"request": request, "title": "ATS Score Check"})

@app.post("/predict/")
async def predict_ats_score(file: UploadFile = File(...)):
    """ Process Resume & Predict ATS Score """
    try:
        # Save uploaded file temporarily
        file_location = f"temp/{file.filename}"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Convert file data to a format compatible with ML model (Dummy example)
        resume_data = {"feature1": [1], "feature2": [0], "feature3": [1]}  # Modify as per your model
        resume_df = pd.DataFrame(resume_data)

        # Make Prediction
        if ats_model:
            score = ats_model.predict(resume_df)[0]
        else:
            score = "Model not loaded"

        return {"status": "success", "score": score}

    except Exception as e:
        return {"status": "error", "message": str(e)}
