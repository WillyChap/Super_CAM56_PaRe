# CAM5/CAM6 SuperModel


# To Run: 
FIRST:
- **$ source ./setup.sh** ... this will set up your bash enviroment and set the CESM_ROOT (currently Francine's sandbox)

NEXT:

Change the settings in the file **"init_supermodel.py"** which are specified with the "#modify" comment and run this file (***$ ./init_supermodel.py***)

THEN: 

a few python files should be written in the current git directory. Please run:

- ***$ ./buildmodels.py***

This will create two model instances of CAM5 and CAM6 that have the names you specified in the **setup.sh** script, as well as the necessary source mods and the fake Data Assimilation scripts additionally, folders are created in your work directory and scratch directory which do the data handling. 

## Finally. 

To submit both jobs on one active queue: **./bash submit_models.sh**

## IF the model crashes

Run ***"./Restart_Model.py"*** and everything should be Gucci, submit the models again
