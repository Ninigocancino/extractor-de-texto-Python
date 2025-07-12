import os
from image_utils import imagen_a_texto

def main():
    print("🖼️  OCR Text Extractor - Extrae texto de imágenes\n")

    ruta_imagen = input("Ruta de la imagen (arrstrala aquí o escribe la ruta): ").strip('"')

    if not os.path.exists(ruta_imagen):
        print("❌ Error: El archivo no existe. Verifica la ruta.")
        return
    
    idioma = input("Idioma (esp=spa, eng=ing, por=por): ").strip().lower() or 'spa'

    print("\n Procesando imagen...")
    texto = imagen_a_texto(ruta_imagen, idioma)

    if not texto:
        print("No se pudo extraer texto. ¿La imagen contiene texto claro?")
        return
    
    nombre_base = os.path.splitext(os.path.basename(ruta_imagen))[0]
    ruta_salida = f"{nombre_base}_texto.txt"

    with open(ruta_salida, 'w', encoding='utf-8') as f:
        f.write(texto)

    print(f"\n ¡Texto extraido con éxito! \n Guardado en: {os.path.abspath(ruta_salida)}")
    print("\n Contenido extraido: \n" + "-"*48)

if __name__ == "__main__":
    main()