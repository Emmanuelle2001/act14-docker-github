# Imagen base oficial y ligera de Python
FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar únicamente los requerimientos de la imagen e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el archivo de la aplicación
COPY app.py .

# Puerto expuesto por el contenedor
EXPOSE 8000

# Comando para ejecutar la API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
