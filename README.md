# Microservices CI/CD Platform

A containerized microservices application with an automated CI/CD and GitOps deployment pipeline using Docker, Kubernetes, Helm, Jenkins, and Argo CD.

## Architecture

Developer
   ↓
GitHub
   ↓
Jenkins
   ↓
Automated Tests
   ↓
Docker Build
   ↓
Docker Hub
   ↓
GitOps Update
   ↓
Argo CD
   ↓
Kubernetes
   ↓
4 Microservices

## Microservices

- User Service
- Product Service
- Order Service
- Notification Service

Each service is implemented using Flask and exposes health-check endpoints for Kubernetes liveness and readiness probes.

## Technologies

- Python / Flask
- Docker
- Docker multi-stage builds
- Kubernetes
- Helm
- Jenkins
- GitHub
- Docker Hub
- Argo CD
- Horizontal Pod Autoscaler (HPA)

## CI/CD Pipeline

1. Developer pushes code to GitHub.
2. Jenkins checks out the repository.
3. Automated tests are executed.
4. Docker images are built using multi-stage Dockerfiles.
5. Images are pushed to Docker Hub.
6. Jenkins updates the image tags in the Helm values file.
7. The updated configuration is pushed back to GitHub.
8. Argo CD detects the Git change.
9. Argo CD synchronizes the Kubernetes deployment.
10. Kubernetes performs a rolling update.

## Kubernetes Features

- Kubernetes Deployments
- ClusterIP Services
- Helm-based deployment
- Liveness probes
- Readiness probes
- Horizontal Pod Autoscaling
- CPU resource requests and limits
- Automated rolling updates

## CI/CD Verification

The pipeline was successfully tested with:

- 4 automated tests passing
- 4 Docker images built
- 4 Docker images pushed to Docker Hub
- Automated Helm image-tag update
- GitHub GitOps commit created by Jenkins
- Argo CD synchronization
- Kubernetes deployment using the new image version

## Running Locally

The project can be deployed to a local Kubernetes cluster using Kind and Helm.

```bash
kind create cluster --name microservices-cluster
helm install microservices ./microservices
