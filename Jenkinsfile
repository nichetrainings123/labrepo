pipeline {
    agent any
    environment {
        PROJECT_NAME = 'MyLearningProject01'
        NGINX_DIR = '/var/www/html'
    }

    options {
        timestamps()
        skipDefaultCheckout()
    }

    stages {

        stage('Deploy to Nginx') {
            steps {
                echo "Deploying project.zip from workspace to Nginx..."
                
                sh """
                    # Check if project.zip exists
                    if [ ! -f project.zip ]; then
                        echo "Error: project.zip not found in workspace!"
                        exit 1
                    fi

                    # Remove old files
                    sudo rm -rf ${NGINX_DIR}/*

                    # Copy new zip
                    sudo cp project.zip ${NGINX_DIR}/

                    # Unzip in Nginx folder and remove zip
                    cd ${NGINX_DIR} && sudo unzip -o project.zip && sudo rm project.zip

                    # Fix permissions
                    sudo chown -R www-data:www-data ${NGINX_DIR}
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
