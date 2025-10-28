from flask import Blueprint, jsonify, render_template
import random
from .models import pokeneas
from .utils import container_id, s3_public_url
import os

bp = Blueprint("main", __name__)

S3_BUCKET = os.environ.get("S3_BUCKET")
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")

@bp.route("/api/pokenea")
def api_pokenea():
    p = random.choice(pokeneas)
    response = {
        "id": p["id"],
        "nombre": p["nombre"],
        "altura": p["altura"],
        "habilidad": p["habilidad"],
        "container_id": container_id()
    }
    return jsonify(response)

@bp.route("/show")
def show_pokenea():
    p = random.choice(pokeneas)
    imagen_url = s3_public_url(S3_BUCKET, AWS_REGION, p["imagen"])
    return render_template(
        "show.html",
        nombre=p["nombre"],
        frase=p["frase"],
        imagen=imagen_url,
        container_id=container_id()
    )


@bp.route("/")
def index():
    return """
    <h1>Pokeneas App</h1>
    <ul>
        <li><a href='/api/pokenea'>Ver Pokenea (API)</a></li>
        <li><a href='/show'>Mostrar Pokenea (HTML)</a></li>
    </ul>
    """
