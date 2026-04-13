"""
Mobile robot control is handled by the native Gazebo diff drive plugin
(gz-sim-diff-drive-system) loaded directly in the URDF.

There is no controller_manager or ros2_control involved.
To drive the robot, publish directly to /cmd_vel:

  ros2 topic pub -r 10 /cmd_vel geometry_msgs/msg/Twist \
    "{linear: {x: 0.5}, angular: {z: 0.3}}"
"""
from launch import LaunchDescription


def generate_launch_description():
    return LaunchDescription([])
