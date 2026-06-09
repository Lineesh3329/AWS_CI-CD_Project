# `Building a CI/CD Workflow Using AWS DevOps Services`

## About the Project
This Project demonstrates the implementation of a Continuous Integration and Continuous Deployment (CI/CD) pipeline on AWS using Docker containers.

A Python Flask application is containerized using Docker and stored in a container registry-Docker Hub. AWS CodeDeploy is used to automate the deployment process to an Amazon EC2 instance. The project showcases how application updates can be deployed quickly and consistently with minimal manual intervention.

-----
### Technologies Used

- GitHub (Source Code Platform)
- AWS CodePipeline (Pipeline orchestration)
- AWS CodeBuild (Build & Docker image creation)
- AWS CodeDeploy (Deployment service)
- AWS EC2 (Hosting/Target Source)
- AWS IAM (Access Management)
- Docker (Containerization)
- Flask (A Python framework)
-----

### Project Workflow
1. Developer pushes code changes to GitHub.
2. AWS CodePipeline detects the latest code changes.
3. AWS CodeBuild builds application & Docker image and pushed to Docker Hub
4. Docker pulls and runs the application container.
5. AWS CodeDeploy deploys the application to EC2.
6. Amazon EC2 receives the deployment package.
7. Flask starts the web application on port 5000.
9. Users access the application through a web browser.
------
        GitHub → CodePipeline → CodeBuild → Docker Hub → CodeDeploy → EC2 → Docker Container → Appplication
------
### Key Features

- Automated CI/CD pipeline using AWS services.
- Containerized application deployment using Docker.
- Continuous deployment from GitHub to EC2.
- Scalable and reusable deployment workflow.
---------
### Overall Outcome

- Successfully built and deployed a containerized Flask application using an AWS CI/CD pipeline integrating GitHub, CodePipeline, CodeBuild, Docker Hub, CodeDeploy, and Amazon EC2.
- Gained practical experience in DevOps automation and cloud deployment.
-------------
