import pandas as pd

def save_to_csv(jobs, filename="jobs.csv"):
    df = pd.DataFrame(jobs)
    df.to_csv(filename, index=False)
    print(f"✅ Jobs saved to {filename}")
