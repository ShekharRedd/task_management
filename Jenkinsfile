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
                     checkout scmGit(branches: [[name: '*/feature']], extensions: [], userRemoteConfigs: [[credentialsId: 'jenkins-github', url: 'https://github.com/ShekharRedd/task_management.git']])
                }
            }
        }
        stage("install") {
            steps {
                catchError(buildResult: 'UNSTABLE') {
                    script {
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
            script {
                // Capture console logs
                def logs = currentBuild.rawBuild.getLog(1000)

                // Format the logs for better readability
                def formattedLogs = """
                    Jenkins Build Log

                    Build Status: ${currentBuild.result ?: 'Unknown'}

                    Console Output:
                    ${logs}
                """
                // Send formatted logs via email
                emailext subject: 'Jenkins Successfully execute , you can raise the pull request',
                          body: formattedLogs,
                          to: 'shekharreddy1010@gmail.com'
            }
        }
        failure {
            script {
                // Capture console logs
                def logs = currentBuild.rawBuild.getLog(1000)
                // Format the logs for better readability
                def formattedLogs = """
                    Jenkins Build Log
                    Build Status: ${currentBuild.result ?: 'Unknown'}
                    Console Output:
                    ${logs}
                """
                // Send formatted logs via email
                emailext subject: 'Jenkins job failed , Please check the logs and review the code once ',
                          body: formattedLogs,
                          to: 'shekharreddy1010@gmail.com'
            }
        }
    }
}

