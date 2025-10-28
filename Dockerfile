# Usa una imagen base ligera de Python
FROM python:3.11-slim

# Define el directorio de trabajo
WORKDIR /app

# Copia TODO el contenido del proyecto al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Variables de entorno
ENV FLASK_APP=run.py
ENV FLASK_ENV=production
ENV PYTHONPATH=/app

# Expone el puerto 5000
EXPOSE 5000

# Ejecuta la aplicación usando gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
