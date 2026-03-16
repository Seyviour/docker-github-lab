### docker-tutorial (forked from [https://github.com/rasikh111/docker-github-lab.git](https://github.com/rasikh111/docker-github-lab.git))
# Tutorial 4: Containerization and Docker

This lab demonstrates how to integrate **Docker** with **GitHub** effectively by creating a simple Flask application, building a Docker image, running it locally, and sharing it through **Docker Hub**.

---

## Objectives
- Understand how to integrate Docker with GitHub.
- Learn to create and configure a `Dockerfile` in a GitHub repository.
- Gain hands-on experience cloning, building, and running a Docker container.
- Learn how to tag and share Docker images using Docker Hub.

---

##  Prerequisites
Before starting, ensure you have:
- Basic understanding of **Git** and version control.
- Familiarity with **Docker** and Dockerfiles.
- A **GitHub account**.
- Installed **Docker Desktop**.
- Installed **git** on your local machine.

---

## 📝 Lab Tasks

### ✅ Task 1: Create a Simple Project in GitHub with a Dockerfile

1. **Create a new repository** on GitHub:
   - Name: `docker-github-lab`
   - Public visibility
   - Initialize with a README

2. **Add a simple Flask application** (`app.py`):

   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def hello():
       return "Hello, Docker!"

   if __name__ == '__main__':
       app.run(host='0.0.0.0')

    Create a Dockerfile:

FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]

Commit and push changes:

    git add .
    git commit -m "Add simple Flask app and Dockerfile"
    git push origin main

✅ Task 2: Clone Locally and Run Docker Build

    Clone the repo:

git clone https://github.com/your-username/docker-github-lab.git
cd docker-github-lab

Build the Docker image:

docker build -t my-flask-app .

Run the container:

docker run -p 5000:5000 my-flask-app

Now visit: 👉 http://localhost:5000


✅ Task 3: Push image to Docker Hub

1. **Create a Docker Hub account** at [hub.docker.com](https://hub.docker.com/) if you do not already have one.

2. **Log in** to Docker Hub from your terminal:

   ```bash
   docker login
   ```

3. **Tag** your image with your Docker Hub username. Replace `YOUR-USERNAME` with your Docker Hub ID:

   ```bash
   docker tag my-flask-app YOUR-USERNAME/my-flask-app:v1.0
   ```

4. **Push** the tagged image to Docker Hub:

   ```bash
   docker push YOUR-USERNAME/my-flask-app:v1.0
   ```

5. Visit your repository on Docker Hub and confirm that the `v1.0` image appears.

🏁 Conclusion

By completing this lab, you have learned how to:

    Create and run a Dockerized application directly from GitHub.

    Build and run Docker containers locally.

    Tag and push Docker images to Docker Hub.

This workflow makes your application easier to share, distribute, and run on other systems. 🎉
📌 Repository Structure

docker-github-lab/
<pre><font color="#12488B"><b>.</b></font>
├── Dockerfile
├── README.md
└── app.py

1 directory, 3 files
</pre>
