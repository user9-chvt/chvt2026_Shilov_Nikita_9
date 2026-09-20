import cv2
from ultralytics import YOLO

model = YOLO("./best.pt")

def main():

    patch = input("Укажите путь до картинки(пример: example_images/04a19a5f-screencopys1.png):")

    results = model.predict(
        source=patch,
        conf=0.5,
        save=True
    )


main()