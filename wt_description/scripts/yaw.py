#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def yaw():
    nacelle = rospy.Publisher('/wind_turbine/yaw_controller/command', Float64, queue_size=10)
    rospy.init_node("nacelle",anonymous=True)
    while not rospy.is_shutdown():
        nacelle.publish(45)

if __name__ == '__main__':
    try:
       yaw()
    except rospy.ROSInterruptException:
        pass