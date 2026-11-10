# Pipeline Canal de Ventas 🏭

Este proyecto consolida el flujo completo de **Integración Continua y Despliegue Continuo (CI/CD)** para el backend corporativo del canal de ventas, automatizando la transición del código desde el repositorio del desarrollador hasta la producción en el clúster.

## 🔄 El Flujo de Automatización (CI/CD)

1.  **Integración Continua (GitHub Actions / Jenkins)**: Al detectar un cambio en el código fuente de `app.py`, el pipeline dispara un agente automatizado.
2.  **Construcción e Inyección (Docker)**: Compila y empaqueta de forma segura la nueva versión de la imagen y la distribuye de manera pública hacia Docker Hub.
3.  **Despliegue Continuo (Kubernetes)**: Aplica una estrategia de actualización progresiva (*Rolling Update*) sobre los manifiestos (`deployment.yaml`, `configmap.yaml`, `red-ventas.yaml`) para inyectar la nueva versión sin causar interrupciones del servicio.

## ⚙️ Archivos Base del Pipeline
*   **`Jenkinsfile` & `.github/workflows/`**: Orquestadores de las etapas del pipeline.
*   **`app.py`**: Código del microservicio integrado con endpoints de salud (`/healthz`) y métricas (`/metrics`).
