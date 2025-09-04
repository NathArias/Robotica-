from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pubsub',
            namespace='turtlesim1',
            executable='pub1',
            name='sim'
        ),
        Node(
            package='pubsub',
            namespace='turtlesim2',
            executable='sub1',
            name='sim'
        ),

        Node(
            package='pubsub',
            namespace='turtlesim2',
            executable='inter',
            name='sim'
        )
    ])