pipeline {
    agent any
    environment {
        PROJECT_NAME = 'MyLearningProject01'
        EMAIL = 'nichetrainings123@gmail.com' // replace with a valid email
        NGINX_DIR = '/var/www/html'
        GIT_REPO = 'https://github.com/nichetrainings123/labrepo.git' // replace with your repo
    }

    options {
        timestamps()
        skipDefaultCheckout()
    }

    stages {

        stage('Clone Project Zip') {
            steps {
                echo "Cloning project.zip from Git repository..."
                sh """
                    git clone ${GIT_REPO} temp_repo
                    cp temp_repo/project.zip .
                    rm -rf temp_repo
                """
            }
        }

        stage('Deploy to Nginx') {
            steps {
                echo "Deploying project.zip to Nginx default folder..."
                // Remove old files
                sh "sudo rm -rf ${NGINX_DIR}/*"
                // Copy new zip
                sh "sudo cp project.zip ${NGINX_DIR}/"
                // Unzip in Nginx folder
                sh "cd ${NGINX_DIR} && sudo unzip -o project.zip && sudo rm project.zip"
                // Fix permissions
                sh "sudo chown -R www-data:www-data ${NGINX_DIR}"
            }
        }

    }

    post {
        success {
            echo "Pipeline executed successfully."
        }
########################################################
        failure {
            echo "Pipeline failed. Sending email..."
            mail to: "${EMAIL}",
                 subject: "Jenkins Pipeline Failed: ${PROJECT_NAME}",
                 body: "Check the Jenkins job for details."
        }
########################################################
        always {
            echo "Cleaning up workspace..."
            cleanWs()
        }
    }
}
