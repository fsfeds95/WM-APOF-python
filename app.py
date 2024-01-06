import os
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from flask import Flask, request, send_file

app = Flask(__name__)

# Ruta /backdrop
@app.route('/backdrop', methods=['POST'])
def add_watermark_backdrop():
    # Verificar si se proporcionó un enlace
    if 'image_url' not in request.form:
        return "¡Error! No se proporcionó ningún enlace de imagen."

    # Obtener el enlace de la imagen
    image_url = request.form['image_url']

    # Descargar la imagen desde el enlace
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # Reescalar la imagen a 1280x720
    image = image.resize((1280, 720))

    # Agregar marca de agua
    watermark = Image.open('wm-backdeop.png')
    watermark = watermark.resize((1280, 720))
    image.paste(watermark, (0, 0), watermark)

    # Guardar la imagen con marca de agua como JPEG
    image_path = 'WM-AstroPeliculasOf.jpg'
    image.save(image_path, 'JPEG', quality=100)

    return send_file(image_path, mimetype='image/jpeg')

# Ruta /poster
@app.route('/poster', methods=['POST'])
def add_watermark_poster():
    # Verificar si se proporcionó un enlace
    if 'image_url' not in request.form:
        return "¡Error! No se proporcionó ningún enlace de imagen."

    # Obtener el enlace de la imagen
    image_url = request.form['image_url']

    # Descargar la imagen desde el enlace
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # Reescalar la imagen a 720x1280
    image = image.resize((720, 1280))

    # Agregar marca de agua
    watermark = Image.open('wm-poster.png')
    watermark = watermark.resize((720, 1280))
    image.paste(watermark, (0, 0), watermark)

    # Guardar la imagen con marca de agua como JPEG
    image_path = 'WM-AstroPeliculasOf.jpg'
    image.save(image_path, 'JPEG', quality=100)

    return send_file(image_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(port=8225)
