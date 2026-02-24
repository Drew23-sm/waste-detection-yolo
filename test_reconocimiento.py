from ultralytics import YOLO
import cv2

# Carga tu modelo entrenado
model = YOLO("best.pt")


video_path = "Video.mp4"  # o 0 si es webcam
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Inference
    results = model(frame)[0]
    
    # Dibujar resultados en el frame
    annotated_frame = results.plot()

    # Mostrar
    cv2.imshow("Detecciones YOLOv11s", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
