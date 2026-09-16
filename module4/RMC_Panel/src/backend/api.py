#primary imports
import time
import rclpy
import threading
from rclpy.node import Node

#topics
# from std_msgs import String
# from geometry_msgs import Twist
from rclpy.duration import Duration
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from geometry_msgs.msg import Twist

from flask import Flask

app = Flask("__name__")


import logging
from datetime import datetime

current_time = datetime.now()

logging.basicConfig(filename="logs_last_mission_forward.txt", level=logging.DEBUG)

rclpy.init()
node = rclpy.create_node("rover2")
publish_cmdvel = node.create_publisher(Twist, "/RMC2/cmd_vel", 10)

forward = Twist()
stop = Twist()
forward.linear.x = 0.1

@app.after_request
def cors(request):
    request.headers["ALLOW_CONTROL_ACCES_ORIGIN"]
    return(request)

@app.post("http://api/forward")
def forward():
    print("Введите сколько секунд ровер должен проехать вперед(10сек = 1метр)")
    # time.sleep(1)
    TIME = int(input())
    print("Началось выполение миссии")
    print(f"movement_start")
    logging.debug(f"{time.localtime}: movement_start")
    try:
        endtime = time.monotonic() + TIME
        while time.monotonic() < endtime:
            print("Ровер начал движение вперед")
            publish_cmdvel.publish(forward)
            logging.debug(f"{current_time}: RMC2 movement to forward")
            time.sleep(0.1)
    finally:
        for _ in range(5):
            publish_cmdvel.publish(stop)
            time.sleep(0.1)

if __name__ == '__main__':
    forward()
