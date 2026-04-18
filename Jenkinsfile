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
                    bat "docker build -t %BACKEND_IMAGE%:%TAG% backend"
                    bat "docker build -t %FRONTEND_IMAGE%:%TAG% frontend"

                    // Tag as latest
                    bat "docker tag %BACKEND_IMAGE%:%TAG% %BACKEND_IMAGE%:latest"
                    bat "docker tag %FRONTEND_IMAGE%:%TAG% %FRONTEND_IMAGE%:latest"
                }
            }
        }

        stage('Push Images') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    bat '''
                    echo %PASS% | docker login -u %USER% --password-stdin
                    '''

                    bat "docker push %BACKEND_IMAGE%:%TAG%"
                    bat "docker push %FRONTEND_IMAGE%:%TAG%"

                    bat "docker push %BACKEND_IMAGE%:latest"
                    bat "docker push %FRONTEND_IMAGE%:latest"
                }
            }
        }

        stage('Deploy') {
            steps {
                bat """
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
                        // safer for Windows
                        bat "powershell -Command Invoke-WebRequest http://localhost/health"
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
}
