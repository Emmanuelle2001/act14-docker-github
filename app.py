from fastapi import FastAPI
import socket
import datetime

app = FastAPI(
    title="API Docker - Actividad 14",
    description="API para generación de imagen en GitHub Container Registry (GHCR) y ejecución en Docker",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "mensaje": "¡Hola Mundo desde Docker y GitHub Actions!",
        "version": "1.0",
        "puerto_asignado": 8000,
        "hostname_contenedor": socket.gethostname(),
        "status": "activo",
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {
        "saludo": f"Hola, {nombre}. Bienvenido a la API contenerizada.",
        "version": "1.0"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "servicio": "api-docker-ghcr"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
