pipeline{
  agent any
  stages {
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
  }
}

