pipeline{
    agent any 
    environment{
        image2="ha"
        tag2="latest"
    }
    stages{
        stage("hello")
        {
            steps
            {
                checkout scmGit(branches: [[name: '*/develop']], extensions: [], userRemoteConfigs: [[credentialsId: 'jenkins-github', url: 'https://github.com/ShekharRedd/task_management.git']])
            }
        }
        stage("Build the images "){
            steps{

                script{
                    dir('/var/jenkins_home/workspace/feature_branch')
                    {
                            echo "========Building docker image  ========"
                            withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                            sh "docker build -t ${image2}:${tag2} ."
                            sh 'echo $USER'
                            sh "echo $PASS | docker login -u $USER --password-stdin"
                            sh "docker tag ${image2}:${tag2} $USER/${image2}:${tag2}"
                            sh "docker push $USER/${image2}:${tag2}"
                }   
                    }             
            }
                }
            }
        }
        
    }

 
