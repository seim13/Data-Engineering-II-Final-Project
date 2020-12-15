pipeline{
  agent any
  stages{
    stage('Build Flask Docker Image'){
      steps {
        script{
          if (env.BRANCH_NAME == 'develop') {
            sh 'docker build -t myflaskapp .' 
          }
        } 
      }
    }
  }
}
