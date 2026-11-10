from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Canal de Ventas FastAPI")

@app.get("/")
def home():
    return {"status": "Ventas Operando", "version": "v1-fastapi"}

@app.get("/comprar")
def comprar():
    return {"message": "Compra procesada exitosamente"}

# ⬇️ ESTA MAGIA ACTIVA LA RUTA /metrics AUTOMÁTICAMENTE PARA PROMETHEUS
Instrumentator().instrument(app).expose(app)
