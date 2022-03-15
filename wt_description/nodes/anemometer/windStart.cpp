#include "ros/ros.h"
#include "std_msgs/Float64MultiArray.h"
#include <ros/console.h>
#include <sstream>

void generateWind();

int main(int argc, char **argv)
{
    ros::init(argc, argv, "windcreator");
    generateWind();
}

void generateWind()
{
    float windHeading = 0 + static_cast <float> (rand()) /( static_cast <float> (RAND_MAX/(3.14-0)));
    float windSpeed = 0 + static_cast <float> (rand()) /( static_cast <float> (RAND_MAX/(100-0)));
    
    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<std_msgs::Float64MultiArray>("/wind_data", 10);

    std_msgs::Float64MultiArray data;
    data.data = {windHeading,windSpeed};
    ros::Rate loop_rate(10);
    while (ros::ok())
    {
        pub.publish(data);
        ros::spinOnce;
    }
}