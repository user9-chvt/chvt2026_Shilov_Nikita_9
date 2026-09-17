import time
import rclpy
from rclpy.duration import Duration
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult

import logging
from datetime import datetime

from rclpy.duration import Duration
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from geometry_msgs.msg import Twist

current_time = datetime.now()

logging.basicConfig(filename="logs_last_mission_forward.txt", level=logging.DEBUG)

def make_pose(nav, x, y, yaw_z=0.0, yaw_w=1.0):
    # Собираем PoseStamped в системе координат map
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = nav.get_clock().now().to_msg()
    pose.pose.position.x = x
    pose.pose.position.y = y
    pose.pose.orientation.z = yaw_z
    pose.pose.orientation.w = yaw_w
    return pose


def main():
    rclpy.init()
    node = rclpy.create_node("rover2")
    nav = BasicNavigator(namespace='/RMC1')  # Создание экземпляра контроллера в неймспейсе робота

    publish_cmdvel = node.create_publisher(Twist, "/RMC2/cmd_vel", 10)

    forward = Twist()
    stop = Twist()
    forward.linear.x = 0.1
    back = Twist()
    back.linear.x = -0.1

    print("MISSION_START")
    time.sleep(1)
    input("Введите нужный стеллаж для RMC2:")
    print("Миссия РМС2 Началась...")

    TIME = 21

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

    init_x_rmc1= 5.0
    init_y_rmc1 = 0.0

    init_pose = make_pose(nav, init_x_rmc1, init_y_rmc1)
    goal_pose = make_pose(nav, 1.0, 3.0)

    input("Введите нужный инстурмент для RMC1:")
    print("RMC1 staring...")

    time.sleep(1)
    # nav.setInitialPose(init_pose)             # Задание исходной позиции
    # nav.waitUntilNav2Active()                 # Ждём, пока стек навигации полностью поднимется

    print("RMC1 stop")

    print(f"RMC2 back home")
    logging.debug(f"{time.localtime}: movement_start")
    try:
        endtime = time.monotonic() + TIME
        while time.monotonic() < endtime:
            print("Ровер начал движение вперед")
            publish_cmdvel.publish(back)
            logging.debug(f"{current_time}: RMC2 movement to forward")
            time.sleep(0.1)
    finally:
        for _ in range(5):
            publish_cmdvel.publish(stop)
            time.sleep(0.1)
    # time.sleep(3.0)                           # Пауза перед постановкой цели

    # nav.goToPose(goal_pose)                   # Задать роботу целевую позицию
    # while not nav.isTaskComplete():           # Цикл ожидания выполнения задачи
    #     feedback = nav.getFeedback()          # Информация о ходе выполнения
    #     if feedback and Duration.from_msg(feedback.navigation_time).nanoseconds / 1e9 > 10:
    #         nav.cancelTask()                  # Отмена, если превышен таймаут (600 сек)

    # result = nav.getResult()                  # Получение итогового результата
    # if result == TaskResult.SUCCEEDED:
    #     print('Goal succeeded!')
    # elif result == TaskResult.CANCELED:
    #     print('Goal was canceled!')
    # elif result == TaskResult.FAILED:
    #     print('Goal failed!')

    # nav.lifecycleShutdown()                   # Корректное завершение работы навигации
    print("MISSION_FINISH")
    rclpy.shutdown()


if __name__ == '__main__':
    main()