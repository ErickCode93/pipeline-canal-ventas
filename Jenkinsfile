pipeline {
    agent any // Indica que puede correr en cualquier servidor esclavo de Jenkins disponible

    environment {
        IMAGE_NAME = 'canal-ventas'
    }

    stages {
        // Etapa 1: Preparación del entorno
        stage('Descarga de Codigo') {
            steps {
                echo 'Descargando la última versión del repositorio...'
                checkout scm
            }
        }

        // Etapa 2: Control de Calidad / Pruebas
        stage('Pruebas Estaticas') {
            steps {
                echo 'Validando sintaxis de código con Python...'
                sh 'python3 -m py_compile app.py'
            }
        }

        // Etapa 3: Compilación y empaquetado
        stage('Construccion Docker') {
            steps {
                echo 'Iniciando compilacion de contenedor Docker...'
                sh "docker build -t ${IMAGE_NAME}:jenkins-${BUILD_NUMBER} ."
            }
        }

        // Etapa 4: Simulación de Despliegue en Kubernetes
        stage('Despliegue a Produccion') {
            steps {
                echo 'Aplicando manifiestos en el clúster de Kubernetes...'
                sh 'kubectl apply -f deployment.yaml'
            }
        }
    }

    // Acciones automáticas que se ejecutan al finalizar todo el pipeline
    post {
        success {
            echo '🎉 [SLA SEGURO] El pipeline de Jenkins finalizó con éxito. Todo desplegado.'
        }
        failure {
            echo '🚨 [ALERTA] Falló el pipeline. Revisar logs de la etapa afectada de inmediato.'
        }
    }
}
