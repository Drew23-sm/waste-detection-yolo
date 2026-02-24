from ultralytics import YOLO

# Load pretrained YOLO model
model = YOLO("yolo11n.pt")

# Train model
results = model.train(
    data="data.yaml",   # dataset config file
    epochs=125,
    imgsz=640
)

print("Training finished")