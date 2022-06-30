pipeline {
   agent any

   stages {
      stage('Preparation') {
         steps {
            cleanWs()
            git credentialsId: 'github-credentials', url: "https://github.com/abstra-app/hackerforms-examples"
         }
      }

      stage('Upload files') {
         steps {
            sh 'docker build --build-arg EXAMPLES_WORKSPACE_API_TOKEN=$EXAMPLES_WORKSPACE_API_TOKEN -t hackerforms-examples-upload .'
            sh 'docker run hackerforms-examples-upload'
         }
      }
   }
}
