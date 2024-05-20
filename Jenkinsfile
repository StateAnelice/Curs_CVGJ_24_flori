node {
    sh 'echo Jenkins started'
}

node {
    sh '''echo Installing Dependencies
    pip3 install flask'''
}

node {
    sh '''echo Testing
    python3 liliac/tests/tests_app.py
    python3 liliac/tests/tests_libs.py'''
}

node {
    sh '''echo Start server
    python3 liliac/liliac.py'''
}
