pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python manage.py test'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t openchat:latest .'
            }
        }
        stage('Docker Push') {
            steps {
                withCredentials([string(credentialsId: 'docker-hub-credentials', variable: 'DOCKER_CREDS')]) {
                    sh 'docker login -u $DOCKER_CREDS_USR -p $DOCKER_CREDS_PSW'
                    sh 'docker tag openchat:latest your-docker-repo/openchat:latest'
                    sh 'docker push your-docker-repo/openchat:latest'
                }
            }
        }
    }
}

