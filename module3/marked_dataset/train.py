from ultralytics import YOLO

# модель
model = YOLO("yolo11n.yaml")

results = model.train(data="data.yaml", epochs=80, imgsz=640)

def main():
    results