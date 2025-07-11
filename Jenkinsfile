pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Vasantha-Meghana/Daily_Mood_Tracker_Flask_App.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    # Add your test commands here
                    echo "No tests defined"
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    export FLASK_APP=app.py
                    export FLASK_ENV=development
                    flask run --host=0.0.0.0 --port=5000 &
                '''
            }
        }
    }

    post {
        success {
            echo 'Flask App Deployed Successfully!'
        }
        failure {
            echo 'Something went wrong.'
        }
    }
}
