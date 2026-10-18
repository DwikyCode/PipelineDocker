pipeline {
    agent any
    environment {
        IMAGE_NAME = 'dwikyrahman/simple-app'
        REGISTRY_CREDENTIALS = 'dockerhub-credentials'
        
        DOCKER_HOST = 'tcp://127.0.0.1:2375' 
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Melakukan checkout dari SCM...'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                bat 'echo "Mulai build aplikasi di Windows"'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Membangun Docker image...'
                bat "docker build -t %IMAGE_NAME%:%BUILD_NUMBER% ."
            }
        }
        stage('Push Docker Image') {
            steps {
                echo 'Push image ke Docker Hub...'
                withCredentials([usernamePassword(credentialsId: REGISTRY_CREDENTIALS,
                    usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    bat 'docker login -u %USER% -p %PASS%'
                    bat "docker push %IMAGE_NAME%:%BUILD_NUMBER%"
                    bat "docker tag %IMAGE_NAME%:%BUILD_NUMBER% %IMAGE_NAME%:latest"
                    bat "docker push %IMAGE_NAME%:latest"
                }
            }
        }
    }
    post {
        always {
            echo 'Selesai build 🏁'
        }
    }
}