import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the FastAPI app from main.py
from main import app

# Initialize the test client
client = TestClient(app)

def test_home_page():
    """Test if the home page loads successfully."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Resume Builder" in response.text  # Ensure the expected text is in response

def test_resume_builder_page():
    """Test if the resume builder page loads successfully."""
    response = client.get("/resume-builder/")
    assert response.status_code == 200
    assert "Resume Builder" in response.text  # Ensure correct page load

# def test_ats_score_page():
#     """Test if the ATS score check page loads successfully."""
#     response = client.get("/ats-score-check/")
#     assert response.status_code == 200
#     assert "ATS Score Check" in response.text

def test_job_finder_page():
    """Test if the job finder page loads successfully."""
    response = client.get("/job-find/")
    assert response.status_code == 200
    assert "Job Finder" in response.text

def test_health_check():
    """Test if the health check endpoint is running."""
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "running",
        "message": "FastAPI service is up and running"
    }

@pytest.mark.parametrize("role, location", [
    ("Software Engineer", "New York"),
    ("Data Scientist", "San Francisco"),
    ("Backend Developer", "Bangalore"),
])
def test_fetch_jobs(role, location, monkeypatch):
    """Mock the job fetch function to avoid real API calls."""
    
    def mock_fetch_jobs(*args, **kwargs):
        return {
            "status": "success",
            "jobs": [
                {"title": "Fake Job", "company": "Fake Corp", "link": "http://fakejob.com"}
            ]
        }
    
    # Mock fetch_jobs function in main.py
    monkeypatch.setattr("main.fetch_jobs", mock_fetch_jobs)
    
    # Use JSON data instead of form-data for API call
    response = client.post("/fetch-jobs/", data={"role": role, "location": location})
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["status"] == "success"
    assert isinstance(data["jobs"], list)
    assert len(data["jobs"]) > 0
    assert "title" in data["jobs"][0]
    assert "company" in data["jobs"][0]
    assert "link" in data["jobs"][0]
