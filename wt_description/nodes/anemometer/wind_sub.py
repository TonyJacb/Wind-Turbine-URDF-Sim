#!/usr/bin/env python3
 
import roslib
roslib.load_manifest('wt_description') #PACKAGE NAME
import rospy
from std_msgs.msg import Float64MultiArray, Float64
from gazebo_msgs.srv import ApplyBodyWrench, BodyRequest
from geometry_msgs.msg import Wrench, Point

##Gazebo service for clearing the force on model
def  clear_body_wrench_client(body_name):
    rospy.wait_for_service('gazebo/clear_body_wrenches')
    try:
        clear_body_wrench = rospy.ServiceProxy('gazebo/clear_body_wrenches',BodyRequest)
        clear_body_wrench(body_name)
    except rospy.ServiceException as e:
        print(e)

##this node is to give commands to the yaw controller. First index is wind heading
def yawController(data):
    rospy.loginfo("The yaw is {}".format(data.data[0]))
    pub = rospy.Publisher("/wind_turbine/yaw_controller/command", Float64, queue_size=10)
    pub.publish(data.data[0])

##Force to be applied on blades
def WindonBlades(data):
    rospy.loginfo ("The yaw is {}".format(data.data[1]))
    rospy.wait_for_service('/gazebo/apply_body_wrench')
    apply_wrench = rospy.ServiceProxy('/gazebo/apply_body_wrench', ApplyBodyWrench)
    wrench = Wrench()

    ##Second index of the data packet is wind speed 
    wrench.torque.x = data.data[1]
    reference_point = Point(x=0,y=0,z=0) 
    start_time = rospy.Time(secs=0,nsecs=0)
    duration = rospy.Duration(secs=1,nsecs=0)

    ##Apply the force
    apply_wrench("hub","world",reference_point, wrench,start_time,duration)
    clear_body_wrench_client("hub")


##Switching mechanism between the yaw and the blade must happen for an effective motion. One motion at a time.
def callback(data):
    global count
    global yaw
    yaw1 = data.data[0]
    print ("Yaw1 is {}".format(yaw1))
    print ("Yaw is {}".format(yaw))
    
    if count != 0:
        if yaw != yaw1:
            print ("more than 1 wind is experienced")
        else:
            print ("no new wind is being blown")
            if count <= 20:
                yawController(data)
                WindonBlades(data)
            elif 20 < count <= 50:
                WindonBlades(data)
    yaw = yaw1
    count += 1
    rospy.loginfo(data.data)

def listener():
    rospy.init_node('anemometer2controller',anonymous=True)
    rospy.Subscriber("wind_turbine/anemometer", Float64MultiArray, callback)
    rospy.spin()

if __name__ == "__main__":
    count = 0
    yaw = 0
    listener()
