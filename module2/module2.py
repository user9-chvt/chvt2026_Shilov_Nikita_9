#primary imports
import time
import rclpy
import threading
from rclpy.node import Node

class rover(Node):
    def __init__(self):
        super().__init__('rover_2')

def main(args=None):
    try:
        with rclpy.init(args=args):
            node = rclpy.create_node('minimal_client')
            cli = node.create_client(AddTwoInts, 'add_two_ints')

            req = AddTwoInts.Request()
            req.a = 41
            req.b = 1
            while not cli.wait_for_service(timeout_sec=1.0):
                node.get_logger().info('service not available, waiting again...')

            future = cli.call_async(req)
            rclpy.spin_until_future_complete(node, future)

            result = future.result()
            node.get_logger().info(
                'Result of add_two_ints: for %d + %d = %d' %
                (req.a, req.b, result.sum))
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()