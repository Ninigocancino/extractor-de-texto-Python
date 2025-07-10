
from PIL import Image, ImageEnhance
import pytesseract


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
    


def imagen_a_texto(ruta_imagen, idioma= 'spa'):
    #Función que extrae texto de la imagen 

    try:
        img = preprocesar_imagen(ruta_imagen)
        if img: 
            texto = pytesseract.image_to_string(img, lang=idioma)
            return texto.strip()
        return None
    except Exception as e: 
        print(f"Error en OCR: {e}")
        return None