import json

def save_to_json(jobs, filename="jobs.json"):
    with open(filename, "w") as file:
        json.dump(jobs, file, indent=4)
    print(f"✅ Jobs saved to {filename}")
