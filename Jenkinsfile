pipeline {
    agent any

    environment {
        PYTHON_EXE = 'C:\\Program Files\\Python311\\python.exe'
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
                bat """
                    "%PYTHON_EXE%" -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate
                    %VENV_DIR%\\Scripts\\pip install --upgrade pip
                    %VENV_DIR%\\Scripts\\pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    echo No tests defined
                """
            }
        }

        stage('Run Flask App') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    set FLASK_APP=app.py
                    set FLASK_ENV=development
                    start /B flask run --host=0.0.0.0 --port=5000
                """
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
