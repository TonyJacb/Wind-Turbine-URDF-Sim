#!/usr/bin/env python3
 
import roslib
roslib.load_manifest('wt_description') #PACKAGE NAME
import rospy
import math
import tf
import geometry_msgs.msg._TransformStamped #Message type. Depends on what kind of data you're working with.

if __name__ == "__main__":
    rospy.init_node('nacelle_tf_listener')

    listener = tf.TransformListener() #listens to the tf thrown

    #Takes in the topic to which you want to publish, Msg Type
    nacelle_yaw = rospy.Publisher('/wind_turbine/nacelle_yaw',geometry_msgs.msg.TransformStamped,queue_size=1)
    rate = rospy.Rate(1.0)

    while not rospy.is_shutdown():
        try:
            #returns a translation and rotation vector. Arguments hold parent to child
            (trans,rot) = listener.lookupTransform('/barge', '/nacelle', rospy.Time())
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue    
        
        #create an object of the message type and change values accordingly to publish
        cmd = geometry_msgs.msg.TransformStamped()
        cmd.transform.translation.x = trans[0]
        cmd.transform.translation.y = trans[1]
        cmd.transform.translation.z = trans[2]

        cmd.transform.rotation.w = rot[0]
        cmd.transform.rotation.x = rot[1]
        cmd.transform.rotation.y = rot[2]
        cmd.transform.rotation.z = rot[3]

        #publish the Msg through the node.
        nacelle_yaw.publish(cmd)

        rate.sleep()
