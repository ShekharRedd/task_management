pipeline{
    agent any 
    environment{
        image2="ganesh"
        tag2="latest"
    }
    stages{
        stage("Intro")
        {
            steps
            {
                echo "checkout to develop branch"
                echo "Successfully pulled the changes from the feature branch by reviewing the code through pull request"
                echo "Building the docker image with the changes"
            }
        }
        stage("Build the images "){
            steps{

                script{
                    dir('/var/jenkins_home/workspace/feature_branch')
                    {
                        sh "git status"
                        sh "git branch"
                        echo "========Building docker image  ========"
                        echo "adding echo comand"
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

 
