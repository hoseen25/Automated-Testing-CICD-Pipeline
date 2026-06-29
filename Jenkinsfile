pipeline {
    agent any

    environment {
        PYTHONDONTWRITEBYTECODE = '1'
    }

    stages {
        stage('Environment Setup') {
            steps {
                echo 'Running Linux setup script...'
                sh 'chmod +x setup_env.sh'
                sh './setup_env.sh'
            }
        }
        
        stage('Code Linting (Pylint)') {
            steps {
                echo 'Running Static Code Analysis with Pylint...'
                sh 'status=0; venv/bin/pylint src/calculator.py || status=$?; echo "Pylint exited with status $status"'
            }
        }
        
        stage('Automated Testing (Pytest)') {
            steps {
                echo 'Executing Automated Unit Tests with Pytest...'
                sh 'venv/bin/pytest tests/test_calculator.py -v'
            }
        }
        
        stage('Artifact Simulation') {
            steps {
                echo 'Packaging application...'
                sh 'tar -czf calculator_package.tar.gz src/'
                echo 'Artifact is ready!'
            }
        }
    }
}