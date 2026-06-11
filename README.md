# Student Management System - Kubernetes GitOps Project

## Overview

The Student Management System is a containerized CRUD web application built using Flask and MySQL. The application allows users to manage student records, including adding, editing, viewing, and searching students.

The project demonstrates modern DevOps practices by deploying the application on Kubernetes and managing deployments using Argo CD with a GitOps workflow.

---

## Features

* Add new students
* View all students
* Edit student details
* Search students by name
* MySQL database integration
* Dockerized application
* Kubernetes deployment
* GitOps-based continuous deployment using Argo CD

---

## Technology Stack

### Backend

* Python 3.12
* Flask 3.0.2

### Database

* MySQL 8

### Containerization

* Docker
* Docker Compose

### Container Registry

* Docker Hub

### Orchestration

* Kubernetes (Minikube)

### GitOps

* Argo CD

### Version Control

* Git
* GitHub

---

## Architecture

```text
User Browser
      │
      ▼
Flask Web Application
      │
      ▼
MySQL Database
```

### Kubernetes Architecture

```text
                 +----------------+
                 |    Argo CD     |
                 +--------+-------+
                          |
                          |
                          ▼
                    GitHub Repository
                          |
                          ▼
+------------------------------------------------+
|                Kubernetes Cluster              |
|                                                |
|   +----------------+      +----------------+   |
|   | Flask Pod      | ---> | MySQL Pod      |   |
|   +----------------+      +----------------+   |
|           |                       |            |
|           ▼                       ▼            |
|   Flask Service          MySQL Service         |
|                                                |
+------------------------------------------------+
```

---

## Project Structure

```text
## Project Structure

```text
student-management-v1/
├── README.md
├── docker-compose.yml
│
├── flask-app/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   ├── static/
│   │   └── style.css
│   └── templates/
│       ├── index.html
│       ├── add.html
│       └── edit.html
│
├── mysql/
│   └── init.sql
│
├── nginx/
│   └── nginx.conf
│
├── app/
│   ├── deployment.yaml
│   └── service.yaml
│
├── k8s/
│   ├── flask-deployment.yaml
│   ├── flask-service.yaml
│   ├── mysql-deployment.yaml
│   ├── mysql-service.yaml
│   ├── mysql-secret.yaml
│   └── mysql-init-configmap.yaml
│
└── argocd/
    └── application.yaml
```

### Directory Description

| Directory/File       | Purpose                                                     |
| -------------------- | ----------------------------------------------------------- |
| `flask-app/`         | Flask application source code and Dockerfile                |
| `mysql/`             | Database initialization scripts                             |
| `nginx/`             | Nginx configuration files                                   |
| `app/`               | Initial Kubernetes manifests used during deployment testing |
| `k8s/`               | Production Kubernetes manifests for Flask and MySQL         |
| `argocd/`            | Argo CD Application manifest for GitOps deployment          |
| `docker-compose.yml` | Local multi-container deployment configuration              |
| `README.md`          | Project documentation                                       |

```
```

```

---

## Database Schema

```sql
CREATE DATABASE IF NOT EXISTS studentdb;

USE studentdb;

CREATE TABLE students
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    course VARCHAR(100)
);
```

---

## Docker Deployment

### Build Image

```bash
docker build -t student-management-flask ./flask-app
```

### Run Using Docker Compose

```bash
docker compose up -d
```

### Access Application

```text
http://localhost:5000
```

---

## Docker Hub Image

```text
vamsiv22/student-management-flask:v1
```

---

## Kubernetes Deployment

Apply Kubernetes manifests:

```bash
kubectl apply -f app/
```

Verify resources:

```bash
kubectl get all
```

Access service:

```bash
minikube service flask-service
```

---

## Argo CD GitOps Deployment

The application is deployed using Argo CD.

### GitOps Workflow

```text
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub Repository
    │
    ▼
Argo CD
    │
    ▼
Kubernetes Cluster
```

### Argo CD Features Used

* Automated synchronization
* Self-healing
* Declarative deployments
* Git as single source of truth

---

## Screenshots

### Student List Page

Displays all students stored in the database.

### Add Student Page

Allows users to add new student records.

### Argo CD Dashboard

Shows application health, synchronization status, and deployment resources.

### Kubernetes Resources

Displays running pods, services, deployments, and replica sets.

---

## Application Endpoints

| Endpoint   | Method    | Description             |
| ---------- | --------- | ----------------------- |
| /          | GET       | View all students       |
| /add       | GET, POST | Add new student         |
| /edit/<id> | GET, POST | Edit existing student   |
| /search    | GET       | Search students by name |

---

## Learning Outcomes

This project helped demonstrate:

* Docker image creation
* Multi-container applications
* Docker Compose orchestration
* Kubernetes Deployments and Services
* ConfigMaps and Secrets
* MySQL integration with Kubernetes
* GitOps workflows
* Argo CD continuous deployment
* Container networking
* Application lifecycle management

---

## Future Enhancements

* Delete student functionality
* Kubernetes Ingress
* Persistent Volumes for MySQL
* Helm charts
* GitHub Actions CI/CD pipeline
* SSL/TLS support
* Monitoring with Prometheus and Grafana
* Logging with ELK Stack

---

## Author

Vamsi Pulidindi

GitHub:
https://github.com/VamsiPulidindi

Docker Hub:
https://hub.docker.com/r/vamsiv22/student-management-flask

