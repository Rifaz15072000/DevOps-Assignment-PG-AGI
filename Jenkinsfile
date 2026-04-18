pipeline {
    agent any

    environment {
        DOCKER_HUB = "rifaz15072000"
        BACKEND_IMAGE = "${DOCKER_HUB}/fastapi-backend"
        FRONTEND_IMAGE = "${DOCKER_HUB}/nextjs-frontend"
        TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Build Images') {
            steps {
                script {
                    bat """
                    docker build -t %BACKEND_IMAGE%:%TAG% backend
                    docker build -t %FRONTEND_IMAGE%:%TAG% frontend

                    docker tag %BACKEND_IMAGE%:%TAG% %BACKEND_IMAGE%:latest
                    docker tag %FRONTEND_IMAGE%:%TAG% %FRONTEND_IMAGE%:latest
                    """
                }
            }
        }

        stage('Push Images') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    
                    bat """
                    docker login -u %USER% -p %PASS%

                    docker push %BACKEND_IMAGE%:%TAG%
                    docker push %FRONTEND_IMAGE%:%TAG%

                    docker push %BACKEND_IMAGE%:latest
                    docker push %FRONTEND_IMAGE%:latest
                    """
                }
            }
        }

stage('Deploy') {
    steps {
        bat """
        docker rm -f backend || exit 0
        docker rm -f frontend || exit 0
        docker rm -f nginx || exit 0

        docker-compose down
        docker pull %BACKEND_IMAGE%:latest
        docker pull %FRONTEND_IMAGE%:latest
        docker-compose up -d
        """
    }
}

        stage('Health Check') {
            steps {
                script {
                    timeout(time: 2, unit: 'MINUTES') {
                        bat "curl -f http://localhost/health"
                    }
                }
            }
        }

        stage('Cleanup') {
            steps {
                bat "docker system prune -f"
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs above.'
        }
    }
}
