pipeline {
    agent any
    environment {
        PROJECT_NAME = 'MyLearningProject01'
        NGINX_DIR = '/var/www/html'
        GIT_REPO = 'https://github.com/nichetrainings123/labrepo.git' // replace with your repo
    }

    options {
        timestamps()
        skipDefaultCheckout()
    }

    stages {

        stage('Deploy from Git to Nginx') {
            steps {
                echo "Deploying project.zip from Git to Nginx..."
                
                sh """
                    set -e

                    # Clone repo to temporary folder
                    git clone ${GIT_REPO} temp_repo

                    # Check if project.zip exists
                    if [ ! -f temp_repo/project.zip ]; then
                        echo "project.zip not found in Git repo!"
                        rm -rf temp_repo
                        exit 1
                    fi

                    # Remove old files in Nginx folder
                    sudo rm -rf ${NGINX_DIR}/*

                    # Copy new zip
                    sudo cp temp_repo/project.zip ${NGINX_DIR}/

                    # Unzip and remove zip
                    cd ${NGINX_DIR} && sudo unzip -o project.zip && sudo rm project.zip

                    # Fix permissions
                    sudo chown -R www-data:www-data ${NGINX_DIR}

                    # Clean up temp repo
                    rm -rf temp_repo
                """
            }
        }

    }

    post {
        success {
            echo "Pipeline executed successfully."
        }

        failure {
            echo "Pipeline failed."
        }

        always {
            echo "Cleaning up workspace..."
            cleanWs()
        }
    }
}
