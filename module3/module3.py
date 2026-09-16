import cv2
import rclpy
from rclpy import Node

from pathlib import Path

from threading import Thread

#for logs
import logging
from datetime import datetime

HERE = Path.resolve().parent("best.pt")
CAMERA = "/RMC1/arm95/svcam/right"
# HAND = 

class hand(Node):
    def __init__(self):
        super().__init__("hand")
        
    def main():
        rclpy.init()

    