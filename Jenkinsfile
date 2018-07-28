pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        git(credentialsId: 'practicaljenkins', branch: 'master', url: 'https://github.com/b2jude/Jenkinspipeline.git', poll: true)
      }
    }
    stage('build') {
      steps {
        sh 'python ./app/*.py'
      }
    }
  }
}