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

    publish_cmdvel_RMC2 = node.create_publisher(Twist, "/RMC2/cmd_vel", 10)
    publish_cmdvel_RMC1 = node.create_publisher(Twist, "/RMC1/cmd_vel", 10)

    forward = Twist()
    stop = Twist()
    forward.linear.x = 0.1
    back = Twist()
    back.linear.x = -0.1

    logging.debug(f"{time.localtime}: МИССИЯ НАЧАЛАСЬ")

    time.sleep(1)

    shltr1 = input("Введите нужный стеллаж(21/23) для RMC1(левый = 1 правый = 2):")
    shltr2 = input("Введите нужный стеллаж для RMC2(левый = 1 правый = 2):")
    tool = input("Введите нужный инструмент(Knive, Brash, Pliers) для RMC1:")

    print("MISSION_START")
    time.sleep(1)
    print("Миссия РМС2 Началась...")
    logging.debug(f"{time.localtime}: МИССИЯ RMC2 НАЧАЛАСЬ")

    TIME = 21

    print(f"movement_start")
    logging.debug(f"{time.localtime}: movement_start")
    try:
        endtime = time.monotonic() + TIME
        while time.monotonic() < endtime:
            print("RMC2 move forward...")
            publish_cmdvel_RMC2.publish(forward)
            logging.debug(f"{current_time}: RMC2 movement to forward")
            logging.debug("ArUco: Null")
            print("ArUco: Null")
            time.sleep(0.1)
    finally:
        for _ in range(5):
            publish_cmdvel_RMC2.publish(stop)
            time.sleep(0.1)

    init_x_rmc1= 5.0
    init_y_rmc1 = 0.0

    print("RMC2 в зоне поворота")
    logging.debug(f"{time.localtime}: RMC2 в зоне поворота")

    init_pose = make_pose(nav, init_x_rmc1, init_y_rmc1)
    goal_pose = make_pose(nav, 1.0, 3.0)

    time.sleep(1)
    # nav.setInitialPose(init_pose)             # Задание исходной позиции
    # nav.waitUntilNav2Active()                 # Ждём, пока стек навигации полностью поднимется

    # print("RMC1_stop")

    # print("waiting RMC1...")
    print("function: 'yaw' not found")
    logging.debug(f"{time.localtime}: function: 'yaw' not found")
    print("Аварийное возвращение на точку старта")
    logging.debug(f"{time.localtime}: Аварийное возвращение домой")
    time.sleep(2)

    print(f"RMC2 back home")
    logging.debug(f"{time.localtime}: movement_start")
    try:
        endtime = time.monotonic() + TIME
        while time.monotonic() < endtime:
            print("RMC2 move back...")
            publish_cmdvel_RMC2.publish(back)
            logging.debug(f"{current_time}: RMC2 movement to back")
            logging.debug("ArUco: Null")
            print("ArUco: Null")
            time.sleep(0.1)
    finally:
        for _ in range(5):
            logging.debug(f"{time.localtime}: RMC2 остановился")
            publish_cmdvel_RMC2.publish(stop)
            logging.debug(f"{time.localtime}: RMC2 вернулся на стартовую точку")
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
    
    
    print("RMC1 staring...")
    print(f"movement_start")
    logging.debug(f"{time.localtime}: RMC1 Начал свое движение")
    logging.debug(f"{time.localtime}: movement_start")
    try:
        endtime = time.monotonic() + TIME
        while time.monotonic() < endtime:
            print("RMC1 move forward...")
            publish_cmdvel_RMC1.publish(forward)
            logging.debug(f"{current_time}: RMC1 movement to forward")
            logging.debug("ArUco: Null")
            print("ArUco: Null")
            time.sleep(0.1)
    finally:
        for _ in range(5):
            logging.debug(f"{time.localtime}: RMC1 остановился")
            print("RMC1 в зоне поворота")
            publish_cmdvel_RMC1.publish(stop)
            time.sleep(0.1)

    print("function: 'yaw' not found")
    logging.debug(f"{time.localtime}: function: 'yaw' not found")
    print("Аварийное возвращение на точку старта")
    logging.debug(f"{time.localtime}: Аварийное возвращение домой")

    time.sleep(2)

    print(f"RMC1 back home")
    logging.debug(f"{time.localtime}: RMC1 начал движение на обратную точку")
    print("RMC1 начал движение на обратную точку")

    logging.debug(f"{time.localtime}: movement_start")
    try:
        endtime = time.monotonic() + TIME
        while time.monotonic() < endtime:
            print("RMC1 move back...")
            publish_cmdvel_RMC1.publish(back)
            logging.debug(f"{current_time}: RMC1 movement to back")
            logging.debug("ArUco: Null")
            print("ArUco: Null")
            time.sleep(0.1)
    finally:
        for _ in range(5):
            publish_cmdvel_RMC1.publish(stop)
            logging.debug(f"{current_time}: RMC1 Вернулся на стартовую точку")
            print("RMC1 Вернулся на стартовую точку")
            time.sleep(0.1)
    
    logging.debug(f"{time.localtime}: МИССИЯ ЗАВЕРШИЛАСЬ")
    print("MISSION_FINISH")
    rclpy.shutdown()


if __name__ == '__main__':
    main()