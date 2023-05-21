#!/usr/bin/env python

# ## also make sure to chmod +x this_script.py

import os, sys
import stat
import pandas as pd
import datetime
import shutil
import time
import glob
import xarray as xr


Mod_Cam5_Name = 'CAM5_gotown' #modify
Mod_Cam6_Name = 'CAM6_gotown' #modify

path_to_work_directory = "/glade/work/wchapman"  #modify
path_to_scratch_directory = "/glade/scratch/wchapman" #modify
project_code="P90xP90xP90x" #modify
path_to_this_directory = os.getcwd()

def replace_all_strings_in_file(file_path, search_string, replace_string):
    with open(file_path, 'r') as file:
        content = file.read()
    
    modified_content = content.replace(search_string, replace_string)
    
    with open(file_path, 'w') as file:
        file.write(modified_content)



def _main_func(description):
    
    shutil.copy2('./Super_Model_Files/Fake_DA.py', os.getcwd())
    shutil.copy2('./Super_Model_Files/Restart_Models.py', os.getcwd())
    shutil.copy2('./Super_Model_Files/buildmodels.py', os.getcwd())
    
    
    replace_all_strings_in_file('./Fake_DA.py','/path/to/scratch/directory',path_to_scratch_directory)
    replace_all_strings_in_file('./Fake_DA.py','/path/to/work/directory',path_to_scratch_directory)
    replace_all_strings_in_file('./Fake_DA.py','CAM5_MODNAME',Mod_Cam5_Name)
    replace_all_strings_in_file('./Fake_DA.py','CAM6_MODNAME',Mod_Cam6_Name)
    replace_all_strings_in_file('./Fake_DA.py','P54048000',project_code)
    replace_all_strings_in_file('./Fake_DA.py','/path/to/this/directory',path_to_this_directory)
    
    replace_all_strings_in_file('./Restart_Models.py','/path/to/scratch/directory',path_to_scratch_directory)
    replace_all_strings_in_file('./Restart_Models.py','/path/to/work/directory',path_to_scratch_directory)
    replace_all_strings_in_file('./Restart_Models.py','CAM5_MODNAME',Mod_Cam5_Name)
    replace_all_strings_in_file('./Restart_Models.py','CAM6_MODNAME',Mod_Cam6_Name)
    replace_all_strings_in_file('./Restart_Models.py','P54048000',project_code)
    replace_all_strings_in_file('./Restart_Models.py','/path/to/this/directory',path_to_this_directory)
    
    replace_all_strings_in_file('./buildmodels.py','/path/to/scratch/directory',path_to_scratch_directory)
    replace_all_strings_in_file('./buildmodels.py','/path/to/work/directory',path_to_scratch_directory)
    replace_all_strings_in_file('./buildmodels.py','CAM5_MODNAME',Mod_Cam5_Name)
    replace_all_strings_in_file('./buildmodels.py','CAM6_MODNAME',Mod_Cam6_Name)
    replace_all_strings_in_file('./buildmodels.py','P54048000',project_code)
    replace_all_strings_in_file('./buildmodels.py','/path/to/this/directory',path_to_this_directory)
    
    st = os.stat('./buildmodels.py')
    os.chmod('./buildmodels.py', st.st_mode | stat.S_IEXEC)

    st = os.stat('./Restart_Models.py')
    os.chmod('./Restart_Models.py', st.st_mode | stat.S_IEXEC)
    
    st = os.stat('./Fake_DA.py')
    os.chmod('./Fake_DA.py', st.st_mode | stat.S_IEXEC)
  
    print('...you are now free to move about the cabin...')
    
    return True


if __name__ == "__main__":
    _main_func(__doc__)
