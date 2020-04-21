from time import sleep
from sensor_msgs.msg  import LaserScan
import rclpy

from rclpy.qos import QoSProfile

def main(args=None):
    rclpy.init()

    node = rclpy.create_node('scanPublisher')

    chatter_pub = node.create_publisher(LaserScan, 'scan', QoSProfile(depth=10))

    msg = LaserScan()

    i = 1
    while True:
        msg.angle_min = float(i)
        i += 0.5
        print('Publishing: "{0}"'.format(msg.angle_min))
        chatter_pub.publish(msg)
        sleep(1)

if __name__ == '__main__':
    main()
