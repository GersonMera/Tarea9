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
