pipeline {
    agent any

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
              -v "$WORKSPACE:/workspace" \
              -w /workspace \
              python:3.13-slim \
              sh -c "pip install -q -r test-requirements.txt && pytest -q"
        '''
    }
}

        stage('Build Docker Images') {
            steps {
                sh '''
                    docker build -t rihan10/user-service:2.0 ./services/user-service
                    docker build -t rihan10/product-service:2.0 ./services/product-service
                    docker build -t rihan10/order-service:2.0 ./services/order-service
                    docker build -t rihan10/notification-service:2.0 ./services/notification-service
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

                        docker push "$DOCKERHUB_USER/user-service:2.0"
                        docker push "$DOCKERHUB_USER/product-service:2.0"
                        docker push "$DOCKERHUB_USER/order-service:2.0"
                        docker push "$DOCKERHUB_USER/notification-service:2.0"

                        docker logout
                    '''
                }
            }
        }
    }
}