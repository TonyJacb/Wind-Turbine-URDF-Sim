#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def rotate():
    blade = rospy.Publisher('/wind_turbine/blade_controller/command', Float64, queue_size=10)
    rospy.init_node("blade",anonymous=True)
    while not rospy.is_shutdown():
        blade.publish(45)

if __name__ == '__main__':
    try:
       rotate()
    except rospy.ROSInterruptException:
        pass