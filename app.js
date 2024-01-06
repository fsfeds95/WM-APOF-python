const express = require('express');
const sharp = require('sharp');

const app = express();
const port = 8225;

// Ruta "/backdrop"
app.get('/backdrop', async (req, res) => {
  const { image } = req.query;

  // Verificar si se proporcionó un enlace de imagen
  if (!image) {
    return res.send('Advertencia: No se proporcionó un enlace de imagen');
  }

  try {
    // Escalar la imagen a 1280x720
    const scaledImage = await sharp(image)
      .resize(1280, 720)
      .toBuffer();

    // Agregar marca de agua
    const watermarkedImage = await addWatermark(scaledImage, 'wm-backdrop.png', 1280, 720);

    // Enviar la imagen de salida como JPEG con calidad del 90%
    res.contentType('image/jpeg');
    res.send(watermarkedImage);
  } catch (error) {
    console.error(error);
    res.status(500).send(`Error al procesar la imagen: ${error.message}`);
  }
});

// Ruta "/poster"
app.get('/poster', async (req, res) => {
  const { image } = req.query;

  // Verificar si se proporcionó un enlace de imagen
  if (!image) {
    return res.send('Advertencia: No se proporcionó un enlace de imagen');
  }

  try {
    // Escalar la imagen a 720x1280
    const scaledImage = await sharp(image)
      .resize(720, 1280)
      .toBuffer();

    // Agregar marca de agua
    const watermarkedImage = await addWatermark(scaledImage, 'wm-poster.png', 720, 1280);

    // Enviar la imagen de salida como JPEG con calidad del 90%
    res.contentType('image/jpeg');
    res.send(watermarkedImage);
  } catch (error) {
    console.error(error);
    res.status(500).send(`Error al procesar la imagen: ${error.message}`);
  }
});

// Función para agregar marca de agua
async function addWatermark(image, watermarkPath, width, height) {
  try {
    // Cargar la marca de agua
    const watermark = await jimp.read(watermarkPath);

    console.log('Imagen original:', image); // Agregar este console.log para ver la imagen original
    console.log('Marca de agua:', watermark); // Agregar este console.log para ver la marca de agua

    // Procesar la imagen con la marca de agua
    const processedImage = await jimp.read(image)
      .resize(width, height)
      .composite(watermark, 0, 0, {
        mode: jimp.BLEND_SOURCE_OVER,
        opacitySource: 0.5,
      })
      .getBufferAsync(jimp.MIME_JPEG);

    return processedImage;
  } catch (error) {
    console.error('Error al agregar la marca de agua:', error);
    throw error;
  }
}