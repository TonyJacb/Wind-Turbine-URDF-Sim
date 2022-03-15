#!/usr/bin/env python3
 
import roslib
roslib.load_manifest('wt_description') # PACKAGE DESCRIPTION
import rospy
import math
import tf
import geometry_msgs.msg._TransformStamped #Msg Type


#Computational Function
def Q2EuRadians(data):
    w = data.transform.rotation.w
    x = data.transform.rotation.x
    y = data.transform.rotation.y
    z = data.transform.rotation.z

    yaw = math.atan2(2.0*(y*z + w*x), w*w - x*x - y*y + z*z)
    pitch = math.asin(-2.0*(x*z - w*y))
    roll = math.atan2(2.0*(x*y + w*z), w*w + x*x - y*y - z*z)

    rospy.loginfo("The yaw in radians: %f",yaw)
    

def listener():
    rospy.init_node('tfSubscriber',anonymous=True)

    #Subscribe to this topic, you should get this Msg. Once recieved, do this
    rospy.Subscriber("/wind_turbine/nacelle_yaw",geometry_msgs.msg.TransformStamped,Q2EuRadians)

    rospy.spin()

if __name__ == '__main__':
    listener()
