// comment
pipeline {
 agent any
 stages {
        stage('Checkout-git'){
               steps{
		git poll: true, url: 'git@github.com:videocursoscloud/lambda-snapshots.git'
               }
        }
       stage('CreateVirtualEnv') {
            steps {
            	sh '''
		  bash -c " \
			  virtualenv entorno_virtual && \
        		  source entorno_virtual/bin/activate && \
                          pip install -r requirements.txt
                  "
                '''
            }
        } 
  }
}



//pylint lambda-snapshots.py -s no -E
