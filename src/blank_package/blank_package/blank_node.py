#!/usr/bin/python3
import os
import rclpy
from rclpy.node import node

# Fill in something for msg type imports
# from duckietown_msgs.msg import SOMETHING
# from std_msgs.msg import SOMETHING

class SkeletonNode(node):
    def __init__(self):
        super().__init__('blank_node')
        #Create publishers and subscribers in init, use callback
        pass
    
    #Define callback functions here


def main():
    print('In main')
    rclpy.init()
    node = SkeletonNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
