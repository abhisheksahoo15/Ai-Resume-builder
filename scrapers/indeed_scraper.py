import requests
from bs4 import BeautifulSoup

def scrape_indeed_jobs(query="Python Developer", location="Remote"):
    URL = f"https://www.indeed.com/jobs?q={query.replace(' ', '+')}&l={location}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    jobs = []
    for job in soup.find_all("h2", class_="jobTitle"):
        title = job.text.strip()
        link = "https://www.indeed.com" + job.find("a")["href"]
        jobs.append({"title": title, "link": link})

    return jobs
