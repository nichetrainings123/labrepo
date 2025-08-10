pipeline {
    agent any
    environment {
        PROJECT_NAME = 'MyLearningProject01'
        EMAIL = 'nichetrainings123@gmail.com' // replace with a valid email,
    }

    options {
        timestamps()
        skipDefaultCheckout()
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Cloning Git repository..."
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                echo "Setting up environment variables and dependencies..."
                sh 'echo "Node version:" && node -v || echo Node not installed'
            }
        }

        stage('Build') {
            steps {
                echo "Simulating build process..."
                sh 'mkdir -p build && echo "Compiled Code" > build/output.txt'
            }
        }

        stage('Unit Tests') {
            steps {
                echo "Running unit tests..."
                sh 'echo "All tests passed!"'
            }
        }

        stage('Archive Artifacts') {
            steps {
                echo "Archiving build artifacts..."
                archiveArtifacts artifacts: 'build/**', fingerprint: true
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully."
        }
        failure {
            echo "Pipeline failed. Sending email..."
            mail to: "${EMAIL}",
                 subject: "Jenkins Pipeline Failed: ${PROJECT_NAME}",
                 body: "Check the Jenkins job for details."
        }
        always {
            echo "Cleaning up workspace..."
            cleanWs()
        }
    }
}
