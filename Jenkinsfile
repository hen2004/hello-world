pipeline {
    agent any

    stages {
        stage('Clone from GitHub') {
            steps {
                git 'https://github.com/hen2004/hello-world'
            }
        }

        stage('Location') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Install Flask') {
            steps {
                sh 'pip install flask'
            }
        }

        stage('Run Python File') {
            steps {
                sh 'python3 hello-world.py'
            }
        }
    }
}
