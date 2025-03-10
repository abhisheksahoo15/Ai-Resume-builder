from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_linkedin_jobs(query="Python Developer", location="Remote"):
    driver = webdriver.Chrome()
    driver.get(f"https://www.linkedin.com/jobs/search/?keywords={query.replace(' ', '%20')}&location={location}")
    
    time.sleep(5)  # Allow time for page to load
    jobs = []
    
    job_elements = driver.find_elements(By.CLASS_NAME, "base-card__full-link")
    for job in job_elements[:10]:  # Get first 10 jobs
        jobs.append({"title": job.text, "link": job.get_attribute("href")})
    
    driver.quit()
    return jobs
