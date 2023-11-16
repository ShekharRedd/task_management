pipeline{
    agent any 
    environment{
        image2="todo-app"
        tag2="latest"
    }
    stages{
            stage("commit is happen in feature branch") {
            steps {
                checkout scmGit(branches: [[name: '*/feature']], extensions: [], userRemoteConfigs: [[credentialsId: 'git-webhook', url: 'https://github.com/ShekharRedd/task_management.git']])
            }
        }

        stage("checkout feature branch") {
            steps {
                script {
                    dir('/var/jenkins_home/workspace/test-webapp/') {
                        echo "hello world"
                        sh "git checkout feature"
                        sh "git pull origin feature"
                        def unit = sh(script: 'python unit.py', returnStatus: true)
                        if (unit == 0) {
                            echo "successfully completed the unit test and proceeding to integration test"
                            def integration = sh(script: 'python integration.py', returnStatus: true)
                            if (integration == 0) {
                                echo "Successfully executed integration test"
                                echo "Proceeding to merge the feature branch to master branch"
                                // Add your merge steps here if needed
                            } else {
                                error "Integration test failed. Check the feature branch for issues."
                            }
                        } else {
                            error "Failed unit test. Check the feature branch for issues."
                        }
                    }
                }
            }
        }

        // Add your other stages here as needed

    


        // stage("Checkout and Merge Feature Branch") {
        //     steps {
        //         script {
        //             dir('/var/jenkins_home/workspace/build-jenkins-pipeline') {
        //                 sh "git checkout main"
        //                 // sh "git pull origin main"

        //                 // Attempt to merge the feature branch
        //                 def mergeExitCode = sh(script: 'git merge feature', returnStatus: true)
                        
        //                 if (mergeExitCode == 0) {
        //                     echo "Merge successful. Committing changes and pushing to main."
        //                     sh "git add ."
        //                     sh 'git commit -m "merging from feature branch"'
        //                     sh "git push origin main"
        //                 } else {
        //                     error "Merge failed. Please resolve conflicts manually and try again."
        //                     // Add any additional actions or notifications here
        //                 }
        //             }
        //         }
        //     }
        // }
        // stage("Building docker image"){
        //     steps{
        //         script{
        //         dir('/var/jenkins_home/workspace/build-jenkins-pipeline/'){
        //         echo "========executing A========"
        //         withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
        //         sh "git checkout main"
        //         sh "cd /var/jenkins_home/workspace/build-jenkins-pipeline/FifthReact/ &&  docker build -t ${image2}:${tag2} ."
        //         sh 'echo $USER'
        //         sh "echo $PASS | docker login -u $USER --password-stdin"
        //         sh "docker tag ${image2}:${tag2} $USER/${image2}:${tag2}"
        //         sh "docker push $USER/${image2}:${tag2}"
        //         }                
                
        //         }
        //     }
        //         }
        //     }
        }
        
    }