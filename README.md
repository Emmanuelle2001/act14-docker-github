# Actividad 14 - Docker Image en GitHub (GHCR)

Repositorio preparado para la **Actividad 14: Docker Image en GitHub**, correspondiente a la materia de **Gestión del Proceso de Desarrollo de Software**.

---

## 📋 Descripción de la Actividad
El objetivo es replicar el flujo DevOps completo de Integración y Entrega Continua (CI/CD):
1. **Preparación:**
   - Crear una API en Python (FastAPI).
   - Generar pruebas unitarias (`pytest`).
   - Validar las pruebas en local.
   - Publicar el repositorio en GitHub con `.gitignore`.
   - Crear el workflow de GitHub Actions para ejecución automática de pruebas.
2. **Generación y Despliegue de Imagen Docker:**
   - Separar los requerimientos (`requirements.txt` para la imagen ligera y `requirements-dev.txt` para pruebas).
   - Modificar el workflow `.github/workflows/docker-image.yml` para añadir un segundo job que compile la imagen Docker y la publique en **GitHub Container Registry (`ghcr.io`)**.
   - Validar que ambos jobs se completen exitosamente en GitHub Actions.
   - Descargar la imagen generada en local mediante `docker pull`.
   - Ejecutar el contenedor con `docker run`.
   - Validar que la API esté activa y responda peticiones.

---

## 🧩 1. Solución: Comandos en Consola (Ordenados y Explicados)

Los comandos proporcionados originalmente en la actividad se encontraban desordenados. A continuación se presenta la secuencia lógica exacta:

### Fase 1: Preparación Local y Control de Versiones
```bash
# 1. Instalar requerimientos base de la aplicación
python -m pip install -r requirements.txt

# 2. Instalar requerimientos de desarrollo y testing (pytest, httpx)
python -m pip install -r requirements-dev.txt

# 3. Validar las pruebas unitarias localmente
python -m pytest -v

# 4. Inicializar el repositorio Git local
git init

# 5. Configurar la identidad de Git
git config --local user.name "USUARIO"
git config --local user.email "CORREO_DE_GITHUB"

# 6. Preparar todos los archivos para el commit
git add .
git commit -m "feat: inicializacion de proyecto con pruebas y workflow"
git branch -M main
```

### Fase 2: Publicación de Imagen y Uso con Docker
*(Una vez subido a GitHub y completado el workflow de Actions)*
```bash
# 7. Descargar la imagen generada automáticamente desde GHCR
docker pull [NOMBRE DE IMAGEN]
# Ejemplo: docker pull ghcr.io/emmanuelle2001/act14-docker-github:latest

# 8. Ejecutar el contenedor en segundo plano mapeando el puerto
docker run -d --name [NOMBRE] -p [PUERTO PC]:[PUERTO IMAGEN] [ENLACE DE IMAGEN]
# Ejemplo: docker run -d --name mi-api-act14 -p 8000:8000 ghcr.io/emmanuelle2001/act14-docker-github:latest
```

---

## 🛠️ 2. Solución: Steps en el `.yml` (Corregidos y Estructurados)

El archivo `.github/workflows/docker-image.yml` corrige los siguientes errores intencionales del ejercicio:
1. **Falta de estructura de Jobs:** Los pasos estaban sueltos en una sola lista. Se dividieron en dos jobs: `test` (validación de pruebas) e `imagen` (compilación y subida a GHCR dependiente de `test`).
2. **Dependencias de prueba:** En el paso de instalación para testing se debe utilizar `requirements-dev.txt` para incluir `pytest`.
3. **Permisos de publicación:** Se añadió el bloque `permissions: packages: write` para que el token de GitHub tenga autorización de publicar en `ghcr.io`.
4. **Orden secuencial:** Checkout -> Setup Python / Buildx -> Install / Login -> Run / Push.

---

## 🚀 3. Guía Paso a Paso para la Entrega

### Paso A: Validar pruebas locales
```bash
python -m pytest -v
```

### Paso B: Crear el repositorio en GitHub
1. Ir a [GitHub New Repository](https://github.com/new).
2. Crear un repositorio público llamado: `act14-docker-github`.
3. No inicializarlo con README ni .gitignore (ya están creados en local).

### Paso C: Subir el proyecto a GitHub
```bash
git remote add origin https://github.com/TU_USUARIO/act14-docker-github.git
git push -u origin main
```

### Paso D: Verificar en GitHub Actions
1. Entrar a la pestaña **Actions** en el repositorio.
2. Observar la ejecución de los dos jobs:
   - `Pruebas Unitarias` (debe salir verde ✅)
   - `Construir y Publicar Imagen en GHCR` (debe salir verde ✅)
3. Al terminar, la imagen estará disponible en la pestaña **Packages** de GitHub.
   *(Nota: si el paquete se crea en modo privado, en la configuración del Package se puede cambiar a Público para descargarlo directamente).*

### Paso E: Descargar y ejecutar la imagen con Docker
1. Asegurarse de tener Docker Desktop abierto.
2. Descargar la imagen:
   ```bash
   docker pull ghcr.io/tu_usuario/act14-docker-github:latest
   ```
3. Ejecutar el contenedor:
   ```bash
   docker run -d --name api-act14 -p 8000:8000 ghcr.io/tu_usuario/act14-docker-github:latest
   ```
4. Probar en el navegador:
   - `http://localhost:8000/`
   - `http://localhost:8000/saludo/Emmanuelle`
   - `http://localhost:8000/docs`
