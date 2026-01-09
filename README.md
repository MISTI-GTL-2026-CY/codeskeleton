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


This is a template repo so the steps are a bit different. You can copy and clone it as follows:
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


Here are the steps to run things:
- fill
-


Here are relevent git commands interact with the repo and make/receive updates:
- ```git pull``` to get latest changes on main branch 
- To put your own changes into the repo:
    - ```git add .``` to stage all files changed
    - ```git status``` to check which files are going to be sent to the repo
    - ```git commit -m "[INFORMATIVE MESSAGE]"``` to explain what you're going send
    - ```git push``` to finally send everything
- Be careful with merge conflict if multiple people work on the same file and try to push conflicting things. These may have to be manually resolved - it's annoying to handle!



*Do see cheat sheet as well for more commands
