pipeline {
    agent any

    environment {
        VENV_PATH = './venv'
    }

    stages {
        stage('Location') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Create Virtual Env & Install Flask') {
            steps {
                sh '''
                    python3 -m venv $VENV_PATH
                    . $VENV_PATH/bin/activate
                    pip install --upgrade pip
                    pip install flask
                '''
            }
        }

        stage('Run Python File') {
            steps {
                sh '''
                    . $VENV_PATH/bin/activate
                    python hello-world.py
                '''
            }
        }
    }
}
