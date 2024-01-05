from flask import Flask, request, send_file
from PIL import Image

app = Flask(__name__)

@app.route('/backdrop')
def backdrop():
    image_url = request.args.get('image')

    if not image_url:
        return '¡Ups! Parece que no has proporcionado un enlace de imagen.'

    try:
        image = Image.open(image_url)
        scaled_image = image.resize((1280, 720))
        watermark = Image.open('wm-backdeop.png')
        watermark = watermark.resize((1280, 720))
        watermark.putalpha(int(0.6 * 255))
        scaled_image.paste(watermark, (0, 0), watermark)
        scaled_image.save('WM-AstroPeliculasOf.jpg', 'JPEG', quality=100)
        return send_file('WM-AstroPeliculasOf.jpg', mimetype='image/jpeg')
    except Exception as e:
        print(e)
        return 'Ha ocurrido un error al procesar la imagen.'

@app.route('/poster')
def poster():
    image_url = request.args.get('image')

    if not image_url:
        return '¡Ups! Parece que no has proporcionado un enlace de imagen.'

    try:
        image = Image.open(image_url)
        scaled_image = image.resize((720, 1280))
        watermark = Image.open('wm-poster.png')
        watermark = watermark.resize((720, 1280))
        watermark.putalpha(int(0.6 * 255))
        scaled_image.paste(watermark, (0, 0), watermark)
        scaled_image.save('WM-AstroPeliculasOf.jpg', 'JPEG', quality=100)
        return send_file('WM-AstroPeliculasOf.jpg', mimetype='image/jpeg')
    except Exception as e:
        print(e)
        return 'Ha ocurrido un error al procesar la imagen.'

if __name__ == '__main__':
    app.run(port=8225)