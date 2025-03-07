from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_google_jobs(query="Python Developer", location="Remote"):
    driver = webdriver.Chrome()
    driver.get(f"https://www.google.com/search?q=site:linkedin.com/jobs {query} {location}")

    time.sleep(3)  # Wait for results
    jobs = []
    
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links[:10]:  # Fetch first 10 job listings
        jobs.append({"title": "Google Search Job", "link": link.get_attribute("href")})
    
    driver.quit()
    return jobs
