from fastapi import FastAPI, Request, File, UploadFile, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
import shutil
import pickle
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

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

# ---------------------- NEW JOB FINDING FEATURE ----------------------

@app.get("/job-find/")
async def job_find_page(request: Request):
    """ Serve the Job Search Page """
    return templates.TemplateResponse("job_find.html", {"request": request, "title": "Job Finder"})


@app.post("/fetch-jobs/")
async def fetch_jobs(role: str = Form(...), location: str = Form(...)):
    """ Fetch job listings from LinkedIn (or another job board) """
    try:
        # LinkedIn job search URL
        url = f"https://www.linkedin.com/jobs/search/?keywords={role}&location={location}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.google.com/",
        }

        response = requests.get(url, headers=headers)
        time.sleep(2)  # Prevent rate limiting

        if response.status_code != 200:
            return {"status": "error", "message": "Failed to fetch job listings"}

        # Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        job_cards = soup.find_all("div", class_="base-card")

        jobs = []
        for job in job_cards[:10]:  # Fetching top 10 jobs
            title_tag = job.find("h3", class_="base-search-card__title")
            company_tag = job.find("h4", class_="base-search-card__subtitle")
            link_tag = job.find("a", class_="base-card__full-link")

            title = title_tag.text.strip() if title_tag else "N/A"
            company = company_tag.text.strip() if company_tag else "N/A"
            job_link = link_tag["href"] if link_tag else "N/A"

            jobs.append({"title": title, "company": company, "link": job_link})

        return {"status": "success", "jobs": jobs}

    except Exception as e:
        return {"status": "error", "message": str(e)}