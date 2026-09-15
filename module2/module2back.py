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

# ROWS = 5
# COLUMNS = 5
# BLOCKED = {}

# # функция поворота
# # def yaw()

# def make_pose(nav, x, y, yaw_z=0.0, yaw_w=1.0):
#     # Собираем PoseStamped в системе координат map
#     pose = PoseStamped()
#     pose.header.frame_id = 'map'
#     pose.header.stamp = nav.get_clock().now().to_msg()
#     pose.pose.position.x = x
#     pose.pose.position.y = y
#     pose.pose.orientation.z = yaw_z
#     pose.pose.orientation.w = yaw_w
#     return pose


# class rover(Node):
#     def __init__(self):
#         super().__init__('rover_2')

# def main():
#     rclpy.init()
#     nav = BasicNavigator(namespace='/RMC2')
#     init_pose = make_pose(nav, 0.0, 0.0)
#     goal_pose = make_pose(nav, 2.0, 1.0)

#     nav.setInitialPose(init_pose)
#     nav.waitUntilNav2Active()

#     time.sleep(3.0)

#     nav.goToPose(goal_pose)
#     while not nav.isTaskComplete():
#         feedback = nav.getFeedback()
#         if feedback and Duration.from_msg(feedback.navigation_time).nanoseconds / 1e9 > 600:
#             nav.cancelTask()

#     result = nav.getResult()
#     if result == TaskResult.SUCCEEDED:
#         print('Goal succeeded!')
#     elif result == TaskResult.CANCELED:
#         print('Goal was canceled!')
#     elif result == TaskResult.FAILED:
#         print('Goal failed!')

#     nav.lifecycleShutdown()
#     rclpy.shutdown()


# if __name__ == '__main__':
#     main()

rclpy.init()
node = rclpy.create_node("rover2")
publish_cmdvel = node.create_publisher(Twist, "/RMC2/cmd_vel", 10)

forward = Twist()
stop = Twist()
forward.linear.x = -0.1

def main():
    print("Введите сколько секунд ровер должен проехать назад(10сек = 1метр)")
    # time.sleep(1)
    TIME = int(input())
    print("Началось выполение миссии")
    print(f"movement_start")
   
    try:
        endtime = time.monotonic() + TIME
        while time.monotonic() < endtime:
            print("Ровер движется назад")
            publish_cmdvel.publish(forward)
            time.sleep(0.1)
    finally:
        for _ in range(5):
            publish_cmdvel.publish(stop)
            time.sleep(0.1)

if __name__ == '__main__':
    main()

print(f"Ровер прехал назад и полностью остановлен и ждет приграды")
print(f"movement_stop")
rclpy.shutdown()
node.destroy_node()