pipeline {

    agent any

    stages {

        stage('Check Python') {
            steps {
                bat '"C:\\Users\\Dell\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Dell\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\Dell\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m pytest -v --junitxml=test-results.xml'
            }
        }

        stage('Check Docker') {
            steps {
                bat 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t calculator-microservice:1.0 .'
            }
        }
    }

    post {
        success {
            echo 'Tests passed and Docker image built successfully.'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}