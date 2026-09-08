pipeline {
    agent any

    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker run --rm \
                      --volumes-from jenkins \
                      -w "$WORKSPACE" \
                      python:3.13-slim \
                      sh -c "pip install -q -r test-requirements.txt && pytest -q"
                '''
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                    docker build -t rihan10/user-service:$IMAGE_TAG ./services/user-service
                    docker build -t rihan10/product-service:$IMAGE_TAG ./services/product-service
                    docker build -t rihan10/order-service:$IMAGE_TAG ./services/order-service
                    docker build -t rihan10/notification-service:$IMAGE_TAG ./services/notification-service
                '''
            }
        }

        stage('Push Docker Images') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_PASSWORD'
                )]) {
                    sh '''
                        echo "$DOCKERHUB_PASSWORD" | docker login -u "$DOCKERHUB_USER" --password-stdin

                        docker push "$DOCKERHUB_USER/user-service:$IMAGE_TAG"
                        docker push "$DOCKERHUB_USER/product-service:$IMAGE_TAG"
                        docker push "$DOCKERHUB_USER/order-service:$IMAGE_TAG"
                        docker push "$DOCKERHUB_USER/notification-service:$IMAGE_TAG"

                        docker logout
                    '''
                }
            }
        }

        stage('Update GitOps') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'github-gitops',
                    usernameVariable: 'GITHUB_USER',
                    passwordVariable: 'GITHUB_TOKEN'
                )]) {
                    sh '''
                        sed -i "s/tag: \\"[0-9.]*\\"/tag: \\"$IMAGE_TAG\\"/g" microservices/values.yaml

                        git config user.name "Jenkins"
                        git config user.email "jenkins@localhost"

                        git add microservices/values.yaml
                        git commit -m "Update image tags to $IMAGE_TAG"

                        git remote set-url origin "https://$GITHUB_USER:$GITHUB_TOKEN@github.com/Rihan286/microservices-cicd-platform.git"
                        git push origin HEAD:main

                        git remote set-url origin "https://github.com/Rihan286/microservices-cicd-platform.git"
                    '''
                }
            }
        }
    }
}