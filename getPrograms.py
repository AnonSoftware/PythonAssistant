import os
from os import listdir
from os.path import isfile, join
import time
import json


global program_list
program_list = []

my_path = os.path.abspath(os.path.dirname(__file__))

def findExe(path,subdirs = -1):
    #loop through files for .exe
    #loop sub folders
    files = {}
    
    #print(subdirs)
    #print(path)
    try:
        os.chdir(path)
        program_folders = [d for d in os.listdir('.') if os.path.isdir(d)]
        onlyfiles = [f for f in listdir('.') if isfile(join(path, f)) and f.endswith(".exe")]
       # print(program_folders)
        #print(program_folders)
        if len(program_folders) > 0:
            for d in program_folders:
                next = findExe(path+"/"+d)
            
        if len(onlyfiles) > 0:
            #print(onlyfiles)
            program_list.append([path,onlyfiles])
            return onlyfiles
    except:
        return []
    return []    
    
def findPrograms():
    print("Finding Programs")
    print("Searching "+os.environ["PROGRAMFILES"])
    print(program_list)
    findExe(os.environ["PROGRAMFILES"])
    print(program_list)
    print("Searchign "+os.environ["PROGRAMFILES(x86)"])
    findExe(os.environ["PROGRAMFILES(x86)"])
    
    print(program_list)
    
    progStr = json.dumps(program_list)
    
    f = open(my_path+"/config/programs.txt","w")
    f.write(progStr)
    f.close()
    
    time.sleep(10)
    
    
    
findPrograms()