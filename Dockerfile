# 1. Usamos una imagen oficial de Python ultra ligera basada en Alpine Linux
FROM python:3.11-alpine

# 2. Definimos el directorio de trabajo limpio dentro del contenedor
WORKDIR /app

# 3. Copiamos el archivo de nuestra aplicación hacia la ruta de trabajo
COPY app.py .

# 4. Comando ejecutable para arrancar el proceso de la app al encender
CMD ["python", "app.py"]
