# SuperModel


# To Run: 
FIRST:
- **$ source ./setup.sh** ... this will set up your bash enviroment

THEN a few python files should be written in the current git directory. 

Change the settings in the file **"init_supermodel.py"** which are specified with the "#modify" comment and run this file (***$ ./init_supermodel.py***)

This will create python files and you will run:

- ***$ ./buildmodels.py***

This will create two model instances of CAM5 and CAM6 that have the names you specified in the **setup.sh** script, as well as the necessary source mods and the fake Data Assimilation scripts. 

## Finally. 

Submit each case individually as you usually do with CAM runs. 

## IF the model crashes

Run ***"./Restart_Model.py"*** and everything should be Gucci. 
