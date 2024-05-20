pipeline {
    agent any
    stages {
        stage('init') {
            steps {
                echo 'Jenkins started'
            }
        }
        stage('dependencies') {
            steps {
                echo 'Installing dependencies'
                sh 'pip3 install flask'
            }
        }
        stage('test') {
            steps {
                echo Testing
                sh '''python3 liliac/tests/tests_app.py
                python3 liliac/tests/tests_libs.py'''
            }
        }
        stage('deploy') {
            steps {
                echo 'Start server'
                sh 'python3 liliac/liliac.py'
            }
        }
    }
}    
