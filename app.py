from flask import Flask, request, send_file
from PIL import Image

app = Flask(__name__)

# Ruta "/poster"
@app.route("/poster")
def add_watermark_to_poster():
    # Verificar si se proporcionó un enlace
    if 'link' not in request.args:
        return "¡Advertencia! No se proporcionó un enlace."

    # Obtener la imagen desde el enlace
    image_url = request.args['link']
    image = Image.open(image_url)

    # Reescalar la imagen a 720px x 1280px
    image = image.resize((720, 1280))

    # Agregar marca de agua
    watermark = Image.open("wm-poster.png")
    watermark = watermark.resize((720, 1280), Image.ANTIALIAS)
    image.paste(watermark, (0, 0), watermark)

    # Guardar la imagen resultante como JPEG con calidad al 100%
    image.save("WM-AstroPeliculasOf.jpg", "JPEG", quality=100)

    # Mostrar la imagen en el navegador sin descarga automática
    return send_file("WM-AstroPeliculasOf.jpg", mimetype='image/jpeg')

# Ruta "/backdrop"
@app.route("/backdrop")
def add_watermark_to_backdrop():
    # Verificar si se proporcionó un enlace
    if 'link' not in request.args:
        return "¡Advertencia! No se proporcionó un enlace."

    # Obtener la imagen desde el enlace
    image_url = request.args['link']
    image = Image.open(image_url)

    # Reescalar la imagen a 1280px x 720px
    image = image.resize((1280, 720))

    # Agregar marca de agua
    watermark = Image.open("wm-backdrop.png")
    watermark = watermark.resize((1280, 720), Image.ANTIALIAS)
    image.paste(watermark, (0, 0), watermark)

    # Guardar la imagen resultante como JPEG con calidad al 100%
    image.save("WM-AstroPeliculasOf.jpg", "JPEG", quality=100)

    # Mostrar la imagen en el navegador sin descarga automática
    return send_file("WM-AstroPeliculasOf.jpg", mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(port=8225)