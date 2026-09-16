import cv2
import rclpy
from ultralytics import YOLO

from rclpy.node import Node

from pathlib import Path
from threading import Thread

from rclpy import qos_overriding_options

from sensor_msgs.msg import Image

#for logs
import logging
from datetime import datetime
current_time = datetime.now()

# HERE = Path.resolve().parent("best.pt")
CAMERA = "/RMC1/arm95/svcam/right"
# HAND = 
MODEL = ("./best.pt")

class hand(Node):
    def __init__(self):
        super().__init__("hand")
        self.create_subscription(Image, CAMERA, 10)  

    def main():
        logging.debug(f"{current_time}: mission_start")
        rclpy.init()
        rclpy.spin()

    