# Skeleton Code for Project

In this template repo we have a blank package and blank node structure with some relatively standard edits. This is a good starting place for the project and you can add all your own functionalities by duplicating blank nodes and packages etc. The structure is similar to the example repo structures:

```
src                   ← ROS workspace
└── blank_package/           ← ROS package
    ├── blank_package/       ← Python module 
    │   └── blank_node.py    ← Your actual ROS node code
    ├── resource/
    │   └── blinker       
    ├── package.xml          ← ROS metadata (we add dependencies)
    ├── setup.py             ← Python packaging + ROS entry points (manually add line for each node)
    └── setup.cfg        
```


### This is a template repo so the steps are a bit different. You can copy and clone it as follows:
- One person per team do this (they will be the owner of the repo):
  - In Github web, click the green ``Use this template" button and then click ``Create a new repository".
  - Have the owner be yourself (you personal github account) and name the repository ``MIT GTL Project"
  - Make visibility public (if not already)
  - Click the green ``Create repository" button.
  - Go to ``Setting" in the navigation bar.
  - Click ``Collaborator" on the left and add you teammates' emails via the ``Add people".
- All other teammates accept the invite. Now everyone has full access to the repo.
- Everyone now clone as before:
  - Open terminal
  - Navigate to where you want to put your cloned repo
  - (hopefully you have an SSH key from in class activity, if not follow instruction on Google)
  - From Github web, click green code button and copy SSH link
  - In terminal, do ``` git clone [INSERT LINK] ```


### Here are relevent git commands interact with the repo and make/receive updates:
- ```git pull``` to get latest changes on main branch 
- To put your own changes into the repo:
    - ```git add .``` to stage all files changed
    - ```git status``` to check which files are going to be sent to the repo
    - ```git commit -m "[INFORMATIVE MESSAGE]"``` to explain what you're going send
    - ```git push``` to finally send everything
- Be careful with merge conflict if multiple people work on the same file and try to push conflicting things. These may have to be manually resolved - it's annoying to handle!



### Here are the steps to run things:
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
    3. Run ros2 docker container ```docker run -it --network=host -v /project:/workspace ros:humble```
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




### MacOS joystick guide
- Download XQuartz and restart your computer.
- Open XQuartz terminal
- ssh to the server with ```ssh user@rpi-server.local``` and the password is `quackquack`
- 

        
          
*Do see cheat sheet as well for more commands
