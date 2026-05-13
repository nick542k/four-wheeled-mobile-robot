import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription

from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

import xacro


def generate_launch_description():

    # ROBOT NAME
    robot_xacro_name = 'differential_drive_robot'

    # PACKAGE NAME
    package_name = 'mobile_robot'

    # FILE PATHS
    model_file_relative_path = 'model/robot.xacro'
    world_file_relative_path = 'model/empty_world.world'

    # ABSOLUTE PATHS
    path_model_file = os.path.join(
        get_package_share_directory(package_name),
        model_file_relative_path
    )

    path_world_file = os.path.join(
        get_package_share_directory(package_name),
        world_file_relative_path
    )

    # PROCESS XACRO
    robot_description = xacro.process_file(
        path_model_file
    ).toxml()

    # GAZEBO LAUNCH FILE
    gazebo_ros_package_launch = PythonLaunchDescriptionSource(
        os.path.join(
            get_package_share_directory('gazebo_ros'),
            'launch',
            'gazebo.launch.py'
        )
    )

    # GAZEBO
    gazebo_launch = IncludeLaunchDescription(
        gazebo_ros_package_launch,
        launch_arguments={
            'world': path_world_file
        }.items()
    )

    # SPAWN ROBOT
    spawn_model_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',

        arguments=[
            '-topic', 'robot_description',
            '-entity', robot_xacro_name
        ],

        output='screen'
    )

    # ROBOT STATE PUBLISHER
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',

        output='screen',

        parameters=[{
            'robot_description': robot_description,
            'use_sim_time': True
        }]
    )

    # LAUNCH DESCRIPTION
    launch_description_object = LaunchDescription()

    launch_description_object.add_action(gazebo_launch)

    launch_description_object.add_action(spawn_model_node)

    launch_description_object.add_action(node_robot_state_publisher)

    return launch_description_object