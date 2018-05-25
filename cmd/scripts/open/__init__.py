#print("Open Script loading")
import subprocess
import os
from os import listdir
from os.path import isfile, join
import time
from cmd.scripts.open.customprograms import custom_programs
import webbrowser
import json


global program_list
program_list = None


my_path = os.path.abspath(os.path.dirname(__file__))
my_path = my_path.replace("cmd\scripts\open","")
print(my_path)


def removeFilters(inputString,filterWords):
    replaceString = ""
    
    inputString = inputString.split(' ')
    
    for k in inputString:
        rem = False
        for f in filterWords:
            if k.lower() == f.lower():
                rem = True
        if rem == False:
            replaceString = replaceString+" "+k.strip()
    
    # for k in filterWords:
        # replaceString = replaceString.replace(k,"").strip()
    replaceString = replaceString.strip()
    replaceString = replaceString.replace('  ',' ')
    arr =  replaceString.split(' ')
    return arr

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
    print("Searchign "+os.environ["PROGRAMFILES(x86)"])
    global program_list
    try:
    
        f = open(my_path+"config/programs.txt","r")
        jsonString = f.read()
        
        program_list = json.loads(jsonString)
    except:
        print("Error getting programs")
        program_list = []
#read()


def init():
    #init function
    print("Finding Programs")
    findPrograms()
    print("Programs Found")
    
    
def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None
    
def runScript(argString):
    stopWords = [
    "open",
    "please",
    "now"
    ]
    filtered = removeFilters(argString,stopWords)
    print(filtered)
    _prog = filtered[0]
    #subprocess.call("start",prog+".exe")
    
    print("Searching for "+_prog)
    
    programExecuted = False
    
    if _prog.lower() in custom_programs:
        print("Prog in custom")
        
        if len(custom_programs[_prog.lower()]) == 2:
            loc = custom_programs[_prog.lower()][0]
            print('"'+loc+'"')
            if custom_programs[_prog.lower()][1] == True:
                webbrowser.open(custom_programs[_prog.lower()][0])
            else:
                subprocess.call('"'+loc+'"',shell=True)
        else:
            loc = custom_programs[_prog.lower()][0]
            print('"'+loc+'"')
            p = subprocess.Popen('"'+loc+'"',shell=True,stdin=None,stdout=None,stderr=None,close_fds=True,creationflags=DETACHED_PROCESS)
            print(p)
            programExecuted = True
    
    else:
        print("Find file")
        if program_list == None:
            findPrograms()
            
        DETACHED_PROCESS = 0x00000008
        
        for k in program_list:
            for p in k[1]:
                compaireProg = _prog.lower()+".exe"
                if compaireProg.lower() == p.lower():
                    #subprocess.call(k[0]+"/"+p,shell=True)
                    
                    p = subprocess.Popen(k[0]+"/"+p,shell=True,stdin=None,stdout=None,stderr=None,close_fds=True,creationflags=DETACHED_PROCESS)
                    print(p)
                    programExecuted = True
                    
                    
                    
                    
    return programExecuted
        