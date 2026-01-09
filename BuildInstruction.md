# How to build the project:
1. Zip your project:
    1. Window: use GUI
    2. Mac/Linux: run the following line in the terminal in the root of the project:
        ```shell
        zip -r project.zip ./
        ```
2. Copy the project to a server:
   ```shell
   scp project.zip user@rpi-server.local:~
   ```
3. Delete the zip file on your local machine
4. ssh to the server with ```ssh user@rpi-server.local``` and the password is `quackquack`
5. On the server:
    1. Create a directory for your project `mkdir -p project`
    2. Unzip the archive `unzip -d project project.zip` (replace all files if you're asked)
    3. Run ros2 docker container ```docker run -it --network=host -v ./project:/workspace ros:humble```
    4. In the container:
        1. Go to workspace directory: `cd /workspace`
        2. Only the first time,
            3. source ROS `source /opt/ros/humble/setup.bash`
        4. Build the project: `colcon build`
        5. Create a new shell: `bash`
        6. Source the environment: `source ./install/setup.bash`
        7. Set environment variables (according to your duckie)
            1. `export VEHICLE_NAME=duckie01`
            2.  `export USER_NAME=anyname`
        8. To run:
            1. With non-MacOS or without joystick on MacOS, use this format: ```ros2 run package node``` or ```ros2 launch launchPackage launch.xml```
            2. With joystick on MacOS, use the MacOS joystick guide we have provided
