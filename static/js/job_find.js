async function uploadResume() {
    let input = document.getElementById("resumeInput").files[0];

    if (!input) {
        alert("Please upload a resume file.");
        return;
    }

    let formData = new FormData();
    formData.append("file", input);

    let jobContainer = document.getElementById("jobResults");
    jobContainer.innerHTML = "<p>Loading job matches...</p>";

    try {
        let response = await fetch("/upload-resume/", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.statusText}`);
        }

        let data = await response.json();
        jobContainer.innerHTML = "";  // Clear previous results

        if (!data.jobs || data.jobs.length === 0) {
            jobContainer.innerHTML = "<p>No matching jobs found.</p>";
            return;
        }

        data.jobs.forEach(job => {
            let jobCard = `
                <div class='job-card'>
                    <h3>${job.title}</h3>
                    <p>${job.company} - ${job.location}</p>
                    <a href="${job.link}" target="_blank">Apply Now</a>
                </div>`;
            jobContainer.innerHTML += jobCard;
        });

    } catch (error) {
        jobContainer.innerHTML = `<p style="color: red;">Error fetching jobs: ${error.message}</p>`;
    }
}
