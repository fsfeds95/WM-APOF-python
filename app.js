const express = require('express');
const sharp = require('sharp');

const app = express();
const port = 8225;

// Ruta "/backdrop"
app.get('/b', async (req, res) => {
  const { img } = req.query;

  // Verificar si se proporcionó un enlace de imagen
  if (!img) {
    return res.send('Advertencia: No se proporcionó un enlace de imagen');
  }

  try {
    // Escalar la imagen a 1280x720
    const scaledimg = await sharp(img)
      .resize(1280, 720)
      .toBuffer();

    // Agregar marca de agua
    const watermarkedimg = await addWatermark(scaledimg, 'Wtxt-backdrop.png', 1280, 720);

    // Enviar la imagen de salida como JPEG con calidad del 90%
    res.contentType('img/jpeg');
    res.send(watermarkedimg);
  } catch (error) {
    console.error(error);
    res.status(500).send('Error al procesar la imagen');
  }
});

// Ruta "/poster"
app.get('/p', async (req, res) => {
  const { img } = req.query;

  // Verificar si se proporcionó un enlace de imagen
  if (!img) {
    return res.send('Advertencia: No se proporcionó un enlace de imagen');
  }

  try {
    // Escalar la imagen a 720x1280
    const scaledimg = await sharp(img)
      .resize(720, 1280)
      .toBuffer();

    // Agregar marca de agua
    const watermarkedimg = await addWatermark(scaledimg, 'Wtxt-poster.png', 720, 1280);

    // Enviar la imagen de salida como JPEG con calidad del 90%
    res.contentType('img/jpeg');
    res.send(watermarkedimg);
  } catch (error) {
    console.error(error);
    res.status(500).send('Error al procesar la imagen');
  }
});

// Función para agregar marca de agua
async function addWatermark(imgBuffer, watermarkFilename, width, height) {
  const watermarkBuffer = await sharp(watermarkFilename)
    .resize(width, height)
    .toBuffer();

  return sharp(imgBuffer)
    .composite([{ input: watermarkBuffer, gravity: 'southeast', opacity: 0.6 }])
    .toBuffer();
}

// Iniciar el servidor
app.listen(port, () => {
  console.log(`La aplicación está escuchando en el puerto ${port}`);
});