pipeline {
    agent any

    stages {
        stage('Clonar código') {
            steps {
                git branch: 'main', url: 'https://github.com/ExpertQuasar/MiProyecto.git'
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
