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
                        sh "ls"
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
                        // def pythonCommand = "${venvPath}/python"
                        def pipCommand = "${venvPath}/coverage"
                        def pytest= "${venvPath}/pytest"

                        // Activate the virtual environment
                        sh ". ${activateScript}"

                        // Change to the workspace directory
                        dir(env.WORKSPACE) {
                            // Run unit.py script
                            // sh "${pythonCommand} unit.py"
                            // sh "${pipCommand} run -m pytest unit.py"
                            // sh "${pipCommand} report -m"
                            // sh "${pipCommand} xml"
                                sh "${pipCommand} run -m pytest unit.py"
                                sh "${pipCommand} xml -o unit_coverage.xml"
                                
                                sh "${pipCommand} run -m pytest integration.py"
                                sh "${pipCommand} xml -o integration_coverage.xml"
                            // Combine XML reports
                                sh "${pipCommand} combine -a unit_coverage.xml -b integration_coverage.xml -o combined_coverage.xml"

                        }
                    }
                }
            }
        }

        // stage('Run Integration Tests') {
        //     steps {
        //         catchError(buildResult: 'FAILURE') {
        //             script {
        //                 def venvPath = "${env.WORKSPACE}/venv/bin"
        //                 def activateScript = "${venvPath}/activate"
        //                 def pythonCommand = "${venvPath}/python"
        //                 def pipCommand = "${venvPath}/coverage"
        //                 def pytest= "${venvPath}/pytest"

        //                 // Activate the virtual environment
        //                 sh ". ${activateScript}"

        //                 // Change to the workspace directory
        //                 dir(env.WORKSPACE) {
        //                     // Run integration.py script
        //                     // sh "${pythonCommand} integration.py"
        //                     sh "${pipCommand} run -m pytest integration.py"
        //                     sh "${pipCommand} report -m"
        //                     sh "${pipCommand} xml"
        //                 }
        //             }
        //         }
        //     }
        // }
          
  //             stage('SonarQube Analysis') {
  //                 steps{
  //                     script{
  //   def scannerHome = tool 'sonarqube';
  //   withSonarQubeEnv() {
  //           sh "${scannerHome}/bin/sonar-scanner  -Dsonar.sources=unit.py,integration.py"
  //   }
  //                 }
  //                 }
  // }
  //   }
        stage('SonarQube Analysis') {
    steps {
        script {
            def scannerHome = tool 'sonarqube'
            withSonarQubeEnv() {
                sh "${scannerHome}/bin/sonar-scanner -Dsonar.sources=unit.py,integration.py -Dsonar.coverageReportPaths=combined_coverage.xml"
            }
        }
    }
}

    
    //     post {
    //     success {
    //         script {
    //             // Capture console logs
    //             def logs = currentBuild.rawBuild.getLog(1000)

    //             // Format the logs for better readability
    //             def formattedLogs = """
    //                 Jenkins Build Log

    //                 Build Status: ${currentBuild.result ?: 'Unknown'}

    //                 Console Output:
    //                 ${logs}
    //             """
    //             // Send formatted logs via email
    //             emailext subject: 'Jenkins Successfully execute , you can raise the pull request',
    //                       body: formattedLogs,
    //                       to: 'shekharreddy1010@gmail.com'
    //         }
    //     }
    //     failure {
    //         script {
    //             // Capture console logs
    //             def logs = currentBuild.rawBuild.getLog(1000)
    //             // Format the logs for better readability
    //             def formattedLogs = """
    //                 Jenkins Build Log
    //                 Build Status: ${currentBuild.result ?: 'Unknown'}
    //                 Console Output:
    //                 ${logs}
    //             """
    //             // Send formatted logs via email
    //             emailext subject: 'Jenkins job failed , Please check the logs and review the code once ',
    //                       body: formattedLogs,
    //                       to: 'shekharreddy1010@gmail.com'
    //         }
    //     }
    // }
}

