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
                sh 'pip install flask'
            }
        }

        stage('Run Python File') {
            steps {
                sh 'python hello-world.py'
            }
        }
    }
}
