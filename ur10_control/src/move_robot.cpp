#include "ros/ros.h"
#include "std_msgs/Float64.h"

int main(int argc, char** argv)
{
    ros::init(argc, argv, "move_robot");

    ros::NodeHandle n;

    ros::Publisher joint1_pub = n.advertise<std_msgs::Float64>("/ur10/joint_1_position_controller/command", 10);
    ros::Publisher joint2_pub = n.advertise<std_msgs::Float64>("/ur10/joint_2_position_controller/command", 10);
    ros::Publisher joint3_pub = n.advertise<std_msgs::Float64>("/ur10/joint_3_position_controller/command", 10);
    ros::Publisher joint4_pub = n.advertise<std_msgs::Float64>("/ur10/joint_4_position_controller/command", 10);

    ros::Rate loop_rate(10);

    int start_time, elapsed;

    while (not start_time) {
        start_time = ros::Time::now().toSec();
    }

    while (ros::ok()) {
        // Get ROS elapsed time
        elapsed = ros::Time::now().toSec() - start_time;
        std_msgs::Float64 joint1_angle, joint2_angle , joint3_angle, joint4_angle;
        joint1_angle.data = sin(2 * M_PI * 0.1 * elapsed) * (M_PI / 2);
        joint2_angle.data = sin(2 * M_PI * 0.1 * elapsed) * (M_PI / 2);
        joint3_angle.data = sin(2 * M_PI * 0.1 * elapsed) * (M_PI / 2);
        joint4_angle.data = sin(2 * M_PI * 0.1 * elapsed) * (M_PI / 2);
        // Publish the arm joint angles
        joint1_pub.publish(joint1_angle);
        joint2_pub.publish(joint2_angle);
        joint3_pub.publish(joint3_angle);
        joint4_pub.publish(joint4_angle);
        // Sleep for the time remaining until 10 Hz is reached
        loop_rate.sleep();
    }

    return 0;
}
