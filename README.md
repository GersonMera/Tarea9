Proyecto: Filtro de Cómic para Imágenes
Descripción
Este proyecto utiliza OpenCV y Python para aplicar un filtro de cómic a una imagen. El filtro convierte una imagen original en un estilo artístico similar al cómic, mejorando los bordes y creando un efecto visual único. Además, el código incluye funciones para mostrar tanto la imagen original como la imagen procesada.

Requisitos
Python 3.x

OpenCV

Numpy

Instalación
Clonar el repositorio o descarga el código:
Si estás trabajando con un repositorio, puedes clonarlo usando Git:

bash
Copiar
git clone https://github.com/tu_usuario/nombre_del_repositorio.git
Instalar las dependencias:

Asegúrate de tener Python instalado y luego instala las bibliotecas necesarias usando pip:

bash
Copiar
pip install opencv-python numpy
Uso
Coloca la imagen que deseas procesar en el mismo directorio que el script, o ajusta la ruta del archivo de imagen en el código.

Ejecute el script para aplicar el filtro cómic:

bash
Copiar
python filtro_comic.py
El script procesará la imagen y mostrará dos ventanas:

Imagen original: la imagen sin cambios.

Imagen con filtro cómic: la imagen procesada con el efecto cómic.

La imagen procesada será guardada con el nombre TheWeeknd_comic.jpg.

Ejemplo de salida
Imagen original: Muestra la imagen antes de aplicar el filtro.

Imagen con filtro cómic: Muestra la imagen después de aplicar el filtro cómic, con un estilo de borde y suavizado.

Guardado de resultados
El script guardará la imagen con el filtro cómic en un archivo llamado TheWeeknd_comic.jpg.

Código
python
Copiar
import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('TheWeeknd.jpg')
if imagen is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

# Aplicar filtro tipo cómic
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
gris = cv2.medianBlur(gris, 7)
bordes = cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)
color = cv2.bilateralFilter(imagen, 9, 250, 250)
comic = cv2.bitwise_and(color, color, mask=bordes)

cv2.putText(comic, 'Filtro Comic', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(imagen, 'Imagen original', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Mostrar la imagen original y la imagen con filtro cómic
cv2.imshow('Imagen original', imagen)
cv2.imshow('Imagen con Filtro Comic', comic)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guardar la imagen con el filtro cómic
cv2.imwrite('TheWeeknd_comic.jpg', comic)
print("Imagen con filtro comic guardada como 'TheWeeknd_comic.jpg'")  # Mensaje de éxito
Autor
Gerson Mera
