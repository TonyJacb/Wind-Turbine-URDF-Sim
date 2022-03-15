#!/usr/bin/env python3
 
import roslib
roslib.load_manifest('wt_description') #PACKAGE NAME
import rospy
from std_msgs.msg import Float64MultiArray
import random

def generate_wind():
    wind_heading = random.uniform(0,3.14)
    wind_speed = random.randint(0,100)
    pub = rospy.Publisher('wind_turbine/anemometer', Float64MultiArray, queue_size=10)
    rospy.init_node('anemometer_pub',anonymous=True)
    rate=rospy.Rate(10)
    
    ##heading and speed to be packaged as a Float64
    data_array = [wind_heading, wind_speed]
    data = Float64MultiArray()
    data.data = data_array
    while not rospy.is_shutdown():
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        generate_wind()
    except rospy.ROSInterruptException:
        pass
