# Pokeneas – Taller AWS Flask + Docker Swarm

## Descripción
Aplicación Flask que muestra información aleatoria sobre Pokeneas. 
Las imágenes se almacenan en **AWS S3** y la app se despliega con **Docker Swarm** sobre instancias EC2.

## Rutas
- `/api/pokenea`: devuelve un JSON con los datos y el ID del contenedor.
- `/show`: muestra una página con la imagen desde S3, la frase y el ID del contenedor.

## Variables de entorno
| Variable | Descripción |
|-----------|--------------|
| `S3_BUCKET` | Nombre del bucket S3 |
| `AWS_REGION` | Región AWS (ej: us-east-1) |

## Ejecución local
```bash
pip install -r requirements.txt
export S3_BUCKET=tu-bucket
export AWS_REGION=us-east-1
python run.py
"# taller2_topicos" 
