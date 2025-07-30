pipeline {
    agent any

    stages {
        stage('Location') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Install Flask') {
            steps {
                sh 'pip3 install flask'
            }
        }

        stage('Run Python File') {
            steps {
                sh 'python3 hello-world.py'
            }
        }
    }
}
