from flask import Flask, render_template

app = Flask(__name__)

PROFILE = {
    "name": "AKM Ashanur Haque",
    "title": "DevOps Engineer | Cloud & Automation",
    "summary": (
        "DevOps-focused IT professional with hands-on experience in AWS, "
        "Docker, Kubernetes, GitHub Actions, Terraform, Prometheus, Grafana and Python. "
        "I build reliable, automated and containerized solutions."
    ),
    "location": "India",
    "email": "ashanur.h10@gmail.com",
    "github": "https://github.com/haque-ashanur",
    "linkedin":"https://www.linkedin.com/in/akm-ashanur-haque-2b5ba818",
}
SKILLS = [
    {"category": "Cloud", "items": "AWS, EC2, S3, RDS, VPC, Lambda, CloudWatch"},
    {"category": "DevOps", "items": "Git, GitHub, GitHub Actions"},
    {"category": "Containers", "items": "Docker, Docker Hub"},
    {"category": "Kubernetes", "items": "Kubernetes, k3s"},
    {"category": "IaC", "items": "Terraform"},
    {"category": "Monitoring", "items": "Prometheus, Grafana"},
    {"category": "Programming", "items": "Python, Bash"},
]

PROJECTS = [
    {
        "name": "Momentum-King Trading Bot",
        "description": (
            "Python-based trading automation project with a Streamlit interface, "
            "containerization and DevOps deployment practices."
        ),
        "stack": "Python • Streamlit • GitHub Actions • Docker • Kubernetes/k3s • AWS • Terraform • Prometheus • Grafana",
    },
    {
        "name": "MyProfile DevOps Website",
        "description": (
            "This portfolio website demonstrates a complete CI/CD workflow using "
            "Git, GitHub, GitHub Actions, Docker and Docker Hub."
        ),
        "stack": "Python • Flask • HTML/CSS • Git • GitHub Actions • Docker • Docker Hub",
    },
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        profile=PROFILE,
        skills=SKILLS,
        projects=PROJECTS,
    )

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
