pipeline{
  agent any
  stages {
    stage('Build Flask app'){
      steps{
        //sh 'docker build -t myflaskapp .'
        echo 'build falsk app'
      }
    }
    stage('Run docker images'){
      parallel{
        stage('Run Redis'){
          steps{
            //sh 'docker run -d -p 6379:6379 --name redis redis:alpine'
            echo 'run redis'
          }
        }
        stage('Run Flask App'){
          steps{
            //sh 'docker run -d -p 5000:5000 --name myflaskapp_c myflaskapp'
            echo 'run flask app'
          }
        }
      }
    }
    stage('Testing'){
      steps{
        //sh 'python test_app.py'
        echo 'run unit test'
      }
    }
    stage('Docker images down'){
      steps{
        //sh 'docker rm -f redis'
        //sh 'docker rm -f myflaskapp_c'
        //sh 'docker rmi -f myflaskapp'
        echo 'Docker down'
      }
    }
  }
}

