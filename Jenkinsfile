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
                echo 'Running tests...'
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
                echo 'Docker push stage will be configured after Docker Hub credentials are added.'
            }
        }
    }
}