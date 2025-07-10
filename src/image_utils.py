
from PIL import Image, ImageEnhance

def preprocesar_imagen(ruta_imagen):

#Función que realiza el procesamiento de imágenes

    try: 
        img = Image.open(ruta_imagen)
        img = img.convert('L')
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2.0)
        return img
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")
        return None