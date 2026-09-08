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
                bat '"C:\\Users\\Dell\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m pytest -v'
            }
        }
        stage('Check Docker') {
    steps {
        bat 'docker --version'
    }
    }

    post {
        success {
            echo 'All tests passed successfully.'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}