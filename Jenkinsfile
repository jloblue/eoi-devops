pipeline {
    agent any

    environment {
        registry = 'jloblue/actividad-jenkins-dados'
		registryCredentials='dockerhub'
		project='actividad-jenkins-dados'
		projectVersion='1.0'
		repository='https://github.com/jloblue/eoi-devops.git'
		repositoryCredentials='github'
    
	}

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout code') {
            steps {
				script {
					git branch: 'main',
						credentialsId: repositoryCredentials,
						url: repository
                }
            }
        }

        stage('Build - CreacionContenedor') {
            steps {
                script {
                    dockerImage= docker.build registry
                }
            }
        }

        stage('Prueba y Borrado del Contenedor') {
            steps {
                script {
					try{
                    sh 'docker run --name $project $registry'
                    }
					finally{
					sh 'docker rm $project'
					}
						
				}   
            }
        }
        

        stage('Deploy - Subir Imagen a Docker') {
            steps {
                script {
                    docker.withRegistry('', registryCredentials) {
                        dockerImage.push()
                    }
                }
            }
        }
    
	
		stage('Borrado de Imagen') {
            steps {
                script {
                    sh 'docker rmi $registry'
                }
            }
        }
	
	
	}

    post {
        failure {
            echo 'Detectado Fallo del pileline, revisión requerida.'
        }
    }
}
