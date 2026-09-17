#primary imports
# import time
import rclpy
# import threading
from rclpy.node import Node
# import numpy

#topics
# from std_msgs import String
# # from geometry_msgs import Twist
# from rclpy.duration import Duration
# from geometry_msgs.msg import PoseStamped
# from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from geometry_msgs.msg import Twist

from flask import Flask

app = Flask("__name__")
# PORT = 5000

import logging
from datetime import datetime

rclpy.init()
# current_time = datetime.now()
node = rclpy.create_node("web_api")

# logging.basicConfig(filename="logs_last_mission_forward.txt", level=logging.DEBUG)
publisher = node.create_publisher(Twist, "/RMC2/cmd_vel", 10)


# URL = "http://localhost/api/forward"

@app.after_request
def cors(request):
    request.headers["Access-Controll-Allow-Origin"] = "*"
    return(request)

@app.post("/api/forward")
def forward():
    # rclpy.init()
    # forward = Twist()
    # stop = Twist()
    # forward.linear.x = 0.1
    # try:
    #     endtime = time.monotonic() + 10
    #     while time.monotonic() < endtime:
    #         publish_cmdvel.publish((forward))
    #         logging.debug(f"{current_time}: RMC2 movement to forward")
    #         time.sleep(0.1)
    # finally:
    #     for _ in range(5):
    #         publish_cmdvel.publish(stop)
    #         time.sleep(0.1)

    speed = Twist()
    speed.linear.x = 0.1

    for _ in range(40):
        publisher.publish(speed)
        rclpy.spin_once(node, timeout_sec=0.05)

    for _ in range(5):
        publisher.publish(Twist())
        rclpy.spin_once(node, timeout_sec=0.05)

    return "ok"

app.run(host="0.0.0.0", threaded=False, port=8000)
