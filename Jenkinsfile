pipeline {
    agent any

    stages {
        stage('Clonar código') {
            steps {
                git branch: 'main', url: 'https://github.com/usuario/repositorio.git'
            }
        }

        stage('Construir') {
            steps {
                echo 'Compilando proyecto...'
            }
        }

        stage('Pruebas') {
            steps {
                echo 'Ejecutando pruebas...'
            }
        }
    }
}
