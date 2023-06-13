# CAM5/CAM6 SuperModel

Clone this to your home directory ... and run with a bash shell please

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

To submit both jobs on one active queue: **qsub ./submit_models.sh**

## A BIG NOTE: 
THE PBS FILE (submit_models.sh) and the settings in the buildmodels.py have to match! So if you change Job_WALLCLOCK_TIME in one, then you must change it in the other)!!!

## IF you reach the end of a run and want to keep going or the model crashes

Run ***"./Restart_Model.py"*** and everything should be Gucci, submit the models again

## IF YOU WANT TO ERASE AND START OVER: 

Run ***"./HARD_Restart.py"*** but warning this erases data and starts back in 1979


