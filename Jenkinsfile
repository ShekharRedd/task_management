pipeline {
    agent any 
    environment {
        image2 = "ganesh"
        tag2 = "latest"
    }
    stages {
        stage("checkout to feature branch") {
            steps {
                script {
                    echo "welcome to feature branch"
                    echo "hello world feature branch"
                    echo "hi welocme"
                    //  checkout scmGit(branches: [[name: '*/feature']], extensions: [], userRemoteConfigs: [[credentialsId: 'jenkins-github', url: 'https://github.com/ShekharRedd/task_management.git']])
                }
            }
        }
        stage("install") {
            steps {
                catchError(buildResult: 'UNSTABLE') {
                    script {
                        echo "hi"
                        sh 'python3 -m venv venv'
                        def venvPath = "${env.WORKSPACE}/venv/bin"
                        def pythonCommand = "${venvPath}/python"
                        def pipCommand = "${venvPath}/pip"

                        // Activate the virtual environment
                        sh ". ${venvPath}/activate"

                        // Install required packages using pip in the virtual environment
                        sh "${pipCommand} install -r requirements.txt"   
                    }
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
            catchError(buildResult: 'FAILURE') {
                
                    script {
                        def venvPath = "${env.WORKSPACE}/venv/bin"
                        def activateScript = "${venvPath}/activate"
                        def pythonCommand = "${venvPath}/python"

                        // Activate the virtual environment
                        sh ". ${activateScript}"

                        // Change to the workspace directory
                        dir(env.WORKSPACE) {
                            // Run unit.py script
                            sh "${pythonCommand} unit.py"
                        }
                    }
                }
            }
        }

        stage('Run Integration Tests') {
            steps {
                catchError(buildResult: 'FAILURE') {
                    script {
                        def venvPath = "${env.WORKSPACE}/venv/bin"
                        def activateScript = "${venvPath}/activate"
                        def pythonCommand = "${venvPath}/python"

                        // Activate the virtual environment
                        sh ". ${activateScript}"

                        // Change to the workspace directory
                        dir(env.WORKSPACE) {
                            // Run integration.py script
                            sh "${pythonCommand} integration.py"
                        }
                    }
                }
            }
        }
    }

    post {
        success {
            def buildLog = currentBuild.rawBuild.getLog().join('\n')
            script {
                
                emailext subject: 'Jenkins Pipeline Successful',
                          body: "The Jenkins pipeline has completed successfully.\n\nBuild Log:\n${buildLog}",
                // recipientProviders: [[$class: 'CulpritsRecipientProvider']],
                        to: 'shekharreddy1010@gmail.com'
            }
        }   
        failure {
            def buildLog = currentBuild.rawBuild.getLog().join('\n')
            script {
                emailext subject: 'Jenkins Pipeline Successful',
                          body: "The Jenkins pipeline has completed successfully.\n\nBuild Log:\n${buildLog}",
                // recipientProviders: [[$class: 'CulpritsRecipientProvider']],
                to: 'shekharreddy1010@gmail.com'
            }
        }
    }
}
