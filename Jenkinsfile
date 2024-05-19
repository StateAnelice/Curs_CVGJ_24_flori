pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python3 -m unittest discover'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                
            }
        }
    }
}