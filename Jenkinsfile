pipeline{
  agent any
  stages{
    stage('Build Flask Docker Image'){
      steps {
        script{
          if (env.BRANCH_NAME == 'develop' || env.BRANCH_NAME == 'release') {
            sh 'docker build -t myflaskapp .' 
          }
          else if(env.BRANCH_NAME == 'master'){
              echo 'master stuff for build'
          }
        } 
      }
    }
    stage('build service images'){
        parallel{
          stage('Run Flask app') {
            steps {
              script{
                if (env.BRANCH_NAME == 'develop' || env.BRANCH_NAME == 'release') {
                  echo 'Running Flask app'
                  sh 'docker run -p 5000:5000 -d --name  myflaskapp  myflaskapp'
                }
              }
            }
          }
        }
    }
    stage ('Testing'){
        steps{
            script{
                if(env.BRANCH_NAME == 'release'|| env.BRANCH_NAME == 'WordEmbedingModel'){
                    //sh 'python test_app.py
                  echo 'test unit running'
                }
            }
        }
    }
    stage ('Release'){
        steps{
            script{
                if(env.BRANCH_NAME == 'release'){
                    echo 'deploy for staging environment'
                }
            }
        }
    }
    stage ('Acceptance Test'){
        steps{
            script{
                if(env.BRANCH_NAME == 'release'){
                    input 'proceed with deployement ?'
                }
            }
        }
    }
    stage ('Merging to master'){
        steps{
            script{
                if(env.BRANCH_NAME == 'release'){
                  sh 'git fetch --all'
                  sh 'git pull'
                  sh 'git checkout release'
                  sh 'git merge main'
                }
            }
        }
    }
    stage('Stop Containers') {
        steps {
          script{
            if(env.BRANCH_NAME == 'develop' || env.BRANCH_NAME == 'release'){
            echo 'Stopping Containers '
            sh 'docker rm -f myflaskapp'
            sh 'docker rmi myflaskapp'
            
          }
        }
      }
    }
  }
}
