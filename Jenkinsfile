pipeline {
    agent any 
    environment {
        image2 = "ganesh"
        tag2 = "latest"
    }
    stages {
        // stage("checkout to feature branch"){
        //     steps{
        //         script{
        //              checkout scmGit(branches: [[name: '*/feature']], extensions: [], userRemoteConfigs: [[credentialsId: 'jenkins-github', url: 'https://github.com/ShekharRedd/task_management.git']])
        //         }
        //     }
        // }
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
            // post {
            //     success {
            //         echo 'Successfully completed the Unit Test proceding to Intergation test'
            //         // Additional actions for success
            //     }
            //     failure {
            //         echo 'Failed Unit test check it once'
            //         // Additional actions for failure
            //     }
            // }
                
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

//         stage('checkout to develop branch'){
//             when {
//                 expression {
//                     BRANCH_NAME == 'feature'
//                 }
//             }
//             steps{
//                 script{
//                 checkout scmGit(branches: [[name: '*/develop']], extensions: [], userRemoteConfigs: [[credentialsId: 'jenkins-github', url: 'https://github.com/ShekharRedd/task_management.git']])
//                 }

//             }            
            
//         }
//         stage("Creating build image "){
//             // when{
//             //     expression{
//             //         BRANCH_NAME == 'develop' && currentBuild.changeSets.any { cs -> cs.branch == 'origin/develop'}
//             //     }
//             // }
//             steps{
//                 script{
//                     dir('/var/jenkins_home/workspace/'){
//                         sh 'git checkout develop '
//                         sh 'git pull origin develop'
//                         echo "======== Creating Docker image  ========"
//                         //     withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
//                         //     sh 'docker build -t ${image2}:${tag2} .'
//                         //     sh 'echo $USER'
//                         //     sh "echo $PASS | docker login -u $USER --password-stdin"
//                         //     sh "docker tag ${image2}:${tag2} $USER/${image2}:${tag2}"
//                         //     sh "docker push $USER/${image2}:${tag2}                    
//                         // }
//                     }
//                 }
//         }

// }
}

}
