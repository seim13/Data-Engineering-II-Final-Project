pipeline{
  agent any
  stages {
    stage('Build Flask app'){
      steps{
        //sh 'docker build -t myflaskapp .'
	echo ' suppose to run the docker build'
      }
    }
    stage('Run docker images'){
        stage('Run Flask App'){
          steps{
            //sh 'docker run -d -p 5000:5000 --name myflaskapp_c myflaskapp'
		echo 'suppose to run the flask app'
          }
        }
      }
    }
    stage('Testing'){
      steps{
        sh 'python test_app.py'
      }
    }
	stage('Build') {
      // Run the Taurus build
   }
   stage('Performance Tests') {
    parallel(
        BlazeMeterTest: {
            dir ('Taurus-Repo') {
                sh 'bzt stress_test.yml -report'
            }
        },
        Analysis: {
            sleep 60
        })
   }

   stage(‘Deploy’) {
   }
}
    stage('Docker images down'){
      steps{
        //sh 'docker rm -f myflaskapp_c'
        //sh 'docker rmi -f myflaskapp'
	      echo 'suppose to down docker'
      }
    }
  }
}
