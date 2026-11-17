import pytest
from app import app, read_root, saludar, health_check

# Pruebas unitarias directas a las funciones
def test_read_root_unit():
    data = read_root()
    assert isinstance(data, dict)
    assert data["status"] == "activo"
    assert data["version"] == "1.0"
    assert data["puerto_asignado"] == 8000
    assert "hostname_contenedor" in data

def test_saludar_unit():
    data = saludar("Emmanuelle")
    assert isinstance(data, dict)
    assert data["version"] == "1.0"
    assert data["saludo"] == "Hola, Emmanuelle. Bienvenido a la API contenerizada."

def test_health_check_unit():
    data = health_check()
    assert isinstance(data, dict)
    assert data["status"] == "ok"
    assert data["servicio"] == "api-docker-ghcr"

# Pruebas de integración HTTP utilizando TestClient (si httpx está disponible)
try:
    from fastapi.testclient import TestClient
    client = TestClient(app)

    def test_http_root():
        response = client.get("/")
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["status"] == "activo"
        assert json_data["version"] == "1.0"

    def test_http_saludar():
        response = client.get("/saludo/Docker")
        assert response.status_code == 200
        json_data = response.json()
        assert "Docker" in json_data["saludo"]

    def test_http_health():
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"

except (ImportError, RuntimeError):
    # Si httpx aún no está instalado en el entorno local, se omiten las pruebas de TestClient
    pass
