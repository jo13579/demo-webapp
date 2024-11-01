## Using Docker
To build the docker image:
```bash
docker build -t my-awesome-app .
```

To run in docker:
```bash 
docker run -p 8000:8000 fastapi-app
```

## Run locally

To run locally:
First time, build venv:
```bash 
python -m venv venv
```
[Install requirements.txt]
Activate venv: 
```bash 
source venv/bin/activate
```

Run app:
```bash
python -m uvicorn main:app --reload 
```

## Using the app
Open a web browser and go to http://127.0.0.1:8000.
Your FastAPI application should be running, and you can test its functionality to ensure everything is working as expected.


## Deploying on Render
__Step 1: Set Up a render.yaml (optional)__

If using Render.com, a render.yaml configuration file can help automate deployment.
In the root of your project, create render.yaml:
```yaml
services:
  - type: web
    name: fastapi-app
    env: docker
    plan: free
    buildCommand: ""
    startCommand: uvicorn app:app --host 0.0.0.0 --port 8000
```

__Step 2: Deploy on Render.com__

Create a Render Account:
Sign up at Render.com if you don’t have an account.

Create a New Web Service:
In the Render dashboard, choose New + > Web Service.
Connect your GitHub or GitLab account and select your repository containing the FastAPI project.
Configure the service:
- Environment: Set to Docker.
- Name: Choose a name for your app (e.g., fastapi-app).
- Region: Choose the closest region.
- Branch: Select the branch to deploy from (usually main or master).
- Build Command: Leave blank (Docker will handle it).
- Start Command: uvicorn app:app --host 0.0.0.0 --port 8000.
Click Create Web Service to start deployment.

__Step 3: Access Your Application:__

After deployment, Render provides a URL for your web service (e.g., https://fastapi-app.onrender.com).
Your FastAPI application will now be live on the web at this URL.

Test and Monitor the Deployed Application

Access and Test:
Go to the URL provided by Render in your browser to access the application.
Test the application to ensure both the search and add product functionalities work as expected.

Monitor Logs and Redeploy:
Render provides logs and an easy redeployment option. If you make updates to the application, just push changes to your GitHub/GitLab repository, and Render will redeploy automatically.
