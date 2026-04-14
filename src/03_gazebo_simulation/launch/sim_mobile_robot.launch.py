import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    pkg_share = get_package_share_directory('gazebo_simulation')
    ros_gz_sim_share = get_package_share_directory('ros_gz_sim')

    urdf_path  = os.path.join(pkg_share, 'urdf', 'mobile_robot.urdf')
    world_path = os.path.join(pkg_share, 'worlds', 'mobile_robot.sdf')
    rviz_config = os.path.join(pkg_share, 'config', 'mobile_robot.rviz')

    with open(urdf_path, 'r') as f:
        robot_description = f.read()

    return LaunchDescription([
        # Gazebo Fortress (worlds/mobile_robot.sdf = empty.sdf + Sensors system for gpu_lidar)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(ros_gz_sim_share, 'launch', 'gz_sim.launch.py')
            ),
            launch_arguments=[('gz_args', f'-r {world_path}')],
        ),

        # Bridge topics between ROS 2 and Gazebo
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
                '/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist',
                '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry',
                '/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V',
                '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan',
            ],
            output='screen',
        ),

        # Joint states: Gazebo publishes to /world/empty/model/mobile_robot/joint_state
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                '/world/empty/model/mobile_robot/joint_state@sensor_msgs/msg/JointState[gz.msgs.Model',
            ],
            remappings=[
                ('/world/empty/model/mobile_robot/joint_state', '/joint_states'),
            ],
            output='screen',
        ),

        # If Gazebo emits scan with frame_id "mobile_robot/laser_frame" instead of "laser_frame"
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'laser_frame', 'mobile_robot/laser_frame'],
            parameters=[{'use_sim_time': True}],
            output='screen',
        ),

        # Publish robot description
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description, 'use_sim_time': True}],
            output='screen',
        ),

        # Spawn robot
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=['-topic', 'robot_description', '-name', 'mobile_robot', '-z', '0.11'],
            output='screen',
        ),

        # RViz
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config],
            parameters=[{'use_sim_time': True}],
            output='screen',
        ),

        # Drive robot and publish trajectory
        Node(
            package='gazebo_simulation',
            executable='cmd_vel_publisher',
            output='screen',
        ),
    ])
