pipeline {
   
   agent any
   
   stages {
       stage('Build'){
          steps {
            echo 'Building..,'
			script{
               python ./app/my_source.py
			   }
          }
       }
       stage('Test'){
           steps {
            echo 'Testing...'
           }
       }  
       stage ('Deploy'){
           steps {
             echo 'Deploying...'
           }
       }       
   
   }
  
}