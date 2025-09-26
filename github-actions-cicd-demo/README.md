# Flask App with CI/CD using GitHub Actions

This project demonstrates a simple **CI/CD pipeline** using **GitHub Actions**.
The pipeline automatically runs tests and deploys the app when changes are pushed.

## 🚀 Tech Stack
- Python 3.11
- Flask (web framework)
- Pytest (testing)
- GitHub Actions (CI/CD)
- Docker (containerization)
- AWS EC2 (deployment)
- Slack (notifications)

## 📦 Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/<your-username>/flask-app-ci-cd.git
cd flask-app-ci-cd
pip install -r requirements.txt
```

## ▶️ Run the app locally
       python app.py


The app will run on http://127.0.0.1:5000.

## 🧪 Running tests
	pytest

## Build Docker Image
```
docker build -t my-app:latest .
docker run -d -p 5000:5000 my-app:latest

```

## Deploy to EC2
```
ssh -i your-key.pem ec2-user@<EC2_PUBLIC_IP>
docker pull <your-dockerhub-username>/my-app:latest
docker run -d -p 80:5000 <image-name>

```
## 🔔 Slack Notification

Sent automatically via GitHub Actions using a webhook.

## ⚙️ CI/CD Pipeline

On every push/Manual Trigger:

- Code is checked out
- Dependencies are installed
- Tests are executed
- Build + push Docker image
- Deploy to EC2
- Send Slack notification

GitHub Actions workflow file: .github/workflows/ci-cd.yml



