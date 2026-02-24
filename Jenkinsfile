pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Debug Environment') {
            steps {
                bat 'echo Checking Python installation...'
                bat 'where python'
                bat 'python --version'
                bat 'dir'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat 'python -m venv %VENV%'
            }
        }

        stage('Upgrade Pip') {
            steps {
                bat '%VENV%\\Scripts\\python -m pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '%VENV%\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Verify Installation') {
            steps {
                bat '%VENV%\\Scripts\\pip list'
            }
        }

        stage('Build Success') {
            steps {
                echo "Build completed successfully 🚀"
            }
        }
    }

    post {
        success {
            echo 'Build Success ✅'
        }
        failure {
            echo 'Build Failed ❌'
        }
    }
}
