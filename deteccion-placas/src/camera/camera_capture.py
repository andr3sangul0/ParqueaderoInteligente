import cv2
import os
import time

# Cargar el clasificador de cascada para placas
cascade_path = "/haarcascade_russian_plate_number.xml"  # Asegúrate de que esta ruta sea correcta
plate_cascade = cv2.CascadeClassifier(cascade_path)

# Crear la carpeta de imágenes si no existe
output_dir = "imagenes_placas"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Contador de fotos
foto_count = 0
max_fotos = 3  # Número máximo de fotos

# Iniciar la captura de video
cap = cv2.VideoCapture(0)

while True:
    # Leer el cuadro de la cámara
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir a escala de grises para mejorar la detección
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar las placas en la imagen
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 25))

    # Recorrer cada placa detectada
    for (x, y, w, h) in plates:
        # Dibujar un rectángulo alrededor de la placa detectada
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Solo toma la foto si no se ha alcanzado el máximo
        if foto_count < max_fotos:
            
            # Tomar una foto de la región de la placa
            plate_img = frame[y:y + h, x:x + w]

            # Generar un nombre único para la imagen usando la fecha y hora actual
            filename = os.path.join(output_dir, f"placa_{int(time.time())}.jpg")

            # Guardar la imagen en la carpeta
            cv2.imwrite(filename, plate_img)
            print(f"Imagen de la placa guardada en: {filename}")
            foto_count += 1
            
    # Mostrar el video en tiempo real con las placas resaltadas
    cv2.imshow("Detección de Placas", frame)

    # Presionar 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
