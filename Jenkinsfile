// comment
pipeline {
 agent any
 stages {
	stage('clean'){
		step([$class: 'WsCleanup'])
	}


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
        		  source ${WORKSPACE}/entorno_virtual/entorno_virtual/bin/activate && \
                          ${WORKSPACE}/entorno_virtual/bin/python ${WORKSPACE}/entorno_virtual/bin/pip install -r requirements.txt
                  "
                '''
            }
        } 
        stage('Ling') {
            steps {
            	sh '''
		  bash -c " \
        		  source entorno_virtual/bin/activate && \
                          ${WORKSPACE}/entorno_virtual/bin/python ${WORKSPACE}/entorno_virtual/bin/pylint lambda-snapshots.py -s no -E
                  "
                '''
            }
        } 
  }
}



