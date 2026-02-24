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

        stage('Setup Python') {
            steps {
                bat 'python -m venv %VENV%'
                bat '%VENV%\\Scripts\\pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '%VENV%\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo "No tests configured yet"
                // Example:
                // bat '%VENV%\\Scripts\\pytest'
            }
        }

        stage('Build Successful') {
            steps {
                echo "Pipeline executed successfully!"
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
