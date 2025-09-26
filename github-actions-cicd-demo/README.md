# Flask App with CI/CD using GitHub Actions

This project demonstrates a simple **CI/CD pipeline** using **GitHub Actions**.
The pipeline automatically runs tests and deploys the app when changes are pushed.

## 🚀 Tech Stack
- Python 3.11
- Flask (web framework)
- Pytest (testing)
- GitHub Actions (CI/CD)
- Docker (optional, for containerization)

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

##🧪 Running tests
	pytest

##⚙️ CI/CD Pipeline

On every push:

Code is checked out

Dependencies are installed

Tests are executed

On main branch merge:

App is deployed (example: Docker Hub / AWS / Render)

GitHub Actions workflow file: .github/workflows/ci-cd.yml

