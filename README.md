# MyProfile — Python DevOps Portfolio

A modern personal profile website built with **Python Flask** and designed as a practical DevOps portfolio project.

## Architecture

```text
Developer
   |
   v
Git
   |
   v
GitHub
   |
   v
GitHub Actions
   |
   +--> Python validation
   |
   +--> Docker build
   |
   v
Docker Hub
   |
   v
Container deployment
```

## Run locally with Python

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
# source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open: http://localhost:5000

## Run with Docker

```bash
docker build -t myprofile .
docker run --rm -p 5000:5000 myprofile
```

Open: http://localhost:5000

## Docker Hub

Create a Docker Hub repository named `myprofile`.

Create a Docker Hub access token and add these GitHub repository secrets:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

Then push to the `main` branch:

```bash
git add .
git commit -m "Initial MyProfile website"
git push origin main
```

GitHub Actions will validate the Python app, build the Docker image and push it to Docker Hub.

## Suggested Git workflow

```bash
git init
git branch -M main
git add .
git commit -m "Initial MyProfile website"
git remote add origin https://github.com/<YOUR_USERNAME>/myprofile.git
git push -u origin main
```

## Customize

Edit the `PROFILE`, `SKILLS`, and `PROJECTS` dictionaries in `app.py`.

Replace:
- `your-email@example.com`
- GitHub URL
- LinkedIn URL

with your actual details.
