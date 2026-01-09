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
3. Delete the archive on your local machine
4. ssh to the server
5. On the server:
    1. Create a directory for your project `mkdir -p project`
    2. Unzip the archive `unzip -d project project.zip` (replace all files if you're asked)
    3. Run ros2 docker container: `docker run -it --network=host -v ./project:/workspace ros:humble`
    4. In the container:
        1. cd to `workspace` directory: `cd /workspace`
        2. Build the project: `colcon build`
        3. Create a new shell: `bash`
        4. Source the environment: `source ./install/setup.bash`
        5. Run you project using `ros2 run` or `ros2 launch`