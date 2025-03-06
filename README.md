# AI Resume Builder

## 1️⃣ About the Project
AI Resume Builder is a smart, AI-powered platform designed to simplify the resume-building process. It helps users create professional resumes, check their ATS (Applicant Tracking System) score, and find relevant job opportunities based on their resume.

## 2️⃣ Features & Functionality
- **Resume Creation**: Generates professional resumes based on user input with various themes.
- **ATS Score Check**: Analyzes resumes and provides an ATS compatibility score using a machine learning model.
- **Job Finder**: Suggests job opportunities based on resume details, utilizing integrated APIs.

## 3️⃣ Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: FastAPI, Django
- **Database**: PostgreSQL
- **Machine Learning**: Python (pickle module for model loading)
- **CI/CD**: GitHub Actions, Terraform
- **Cloud Deployment**: Azure Web App

## 4️⃣ CI/CD Pipeline
The CI/CD pipeline automates code integration, testing, and deployment:
- **Development Phase**: Developers push changes to the feature branch.
- **Testing Phase**: Automated tests run on every push to ensure stability.
- **Deployment Phase**: Successful builds are deployed to Azure via GitHub Actions and Terraform.

## 5️⃣ DevSecOps Implementation
- **Security Measures**: Uses OWASP guidelines to ensure security.
- **Static Code Analysis**: Integrated security scanners.
- **Automated Security Testing**: Runs security checks during CI/CD.
- **Infrastructure as Code (IaC)**: Terraform ensures secure and consistent cloud deployments.

## 6️⃣ Deployment Process
- The app is deployed using **Terraform** and **GitHub Actions**.
- Infrastructure is managed using Terraform configurations.
- GitHub Actions automates the deployment to Azure Web Apps.
- The live version can be accessed at: [AI Resume Builder](https://ai-resume-builder.azurewebsites.net)

## 7️⃣ Contributors
- **Abhishek Shaoo** - Project Lead & Developer
- Open to contributions! Feel free to submit a PR.

## 8️⃣ Agile Development Process
- Follows **Scrum** methodology.
- Sprint planning and task tracking using **Jira**.
- Regular code reviews and team collaboration.

## 9️⃣ How to Run Locally
```sh
# Clone the repository
git clone https://github.com/abhisheksahoo15/Ai-Resume-builder.git
cd Ai-Resume-builder

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --host 0.0.0.0 --port 8000
```
Visit `http://localhost:8000/docs` to access the FastAPI Swagger UI.

## 🔟 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
