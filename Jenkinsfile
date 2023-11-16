pipeline {
    agent any 
    environment {
        image2 = "todo-app"
        tag2 = "latest"
    }
    stages {

        stage("checkout to feature branch"){
            steps{
                script{
                     checkout scmGit(branches: [[name: '*/feature']], extensions: [], userRemoteConfigs: [[credentialsId: 'git-webhook', url: 'https://github.com/ShekharRedd/task_management.git']])
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
        stage("merge to develop branch") {
                when {
                    expression {
                        BRANCH_NAME == 'feature'
                    }
                }
                steps {
                    script {
                        dir("/var/jenkins_home/workspace/task-webapp/") {
                            sh "git checkout develop"
                            sh "git pull origin develop"
                            // Attempt to merge the feature branch
                            catchError(buildResult: 'FAILURE') {
                                sh "git merge feature"
                            }
                            // Check if the merge was successful or if there were conflicts
                            def mergeStatus = sh(script: 'git merge-base develop feature', returnStatus: true)
                            
                            if (mergeStatus != 0) {
                                // Merge conflicts occurred
                                error "Merge conflicts occurred. Please resolve conflicts manually and try again."
                            } else {
                                // No conflicts, push the changes to develop
                                sh "git push origin develop"
                            }
                        }
                    }
                }
            }

            stage("Merge to master branch") {
                when {
                    expression {
                        BRANCH_NAME == 'master'
                    }
                }
                steps {
                    script {
                        dir("/var/jenkins_home/workspace/task-webapp/") {
                            sh "Merging the code from develop branh to master "
                            sh "Ready to create a docker images"
                            sh "git checkout master"
                            sh "git reset --hard develop"
                            sh "git merge develop"
                        }
                    }
                }
            }
    }
}
