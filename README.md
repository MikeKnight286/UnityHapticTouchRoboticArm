# UnityHapticTouchRoboticArm
Test project for Touch 3D using robotic arm connected to ROS
## Table of Contents

- [Docker Installation](#docker-installation)
- [ROS Docker Setup Guide for Robotic Arm](#ros-docker-setup-guide-for-robotic-arm)
- [Unity Setup](#unity-setup)
- [Credits](#credits)
- [Contact Information](#contact-information)
- [Screenshots and Media](#screenshots-and-media)

## Docker Installation 

Install Docker to host a server for ROS connection

[Install Docker Engine] (https://docs.docker.com/engine/install/)https://docs.docker.com/engine/install/)

## ROS Docker Setup Guide for Robotic Arm 

1. **Link "ros-docker-server" File to Docker Container** 
- Use the following command to link "ros-docker-server" file to the Docker container (replace `(USER_PATH)` with the actual path to this file):
     ```bash
     docker run -v (USER_PATH):/home/ubuntu/catkin_ws:cached -p 6080:80 -p 10000:10000 --shm-size=1024m tiryoh/ros-desktop-vnc:noetic 
     ```
   - Alternatively, you can open a Docker container without linking to user files with the following command:
     ```bash
     docker run -p 6080:80 -p 10000:10000 --shm-size=1024m tiryoh/ros-desktop-vnc:noetic 
     ```
2. **Use the ROS Workspace in Virtual Ubuntu Desktop**
- [Virtual Desktop] (http://127.0.0.1:6080/)
- Open System Tools -> LXTerminal from left bottom corner of the GUI
- Use the following command to run ROS Server for Robotic Arm 
     ```bash
     roslaunch my_robot_arm_service my_robot_arm_server.launch
     ```

## Unity Setup

Assign Goal in TrajectoryPlanner Script to Desired GameObject (In Sample Video, assigned to HapticCollider of HapticTouch3D Device)

# Credits

Unity ではじめるロボットプログラミンング実践入門

# Contact Information

bhonetaybusiness@gmail.com

# Screenshot and Media

https://github.com/MikeKnight286/UnityHapticTouchRoboticArm/assets/136081708/e702cee9-4251-4812-af30-0cdaae4d6570



