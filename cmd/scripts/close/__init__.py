#print("Open Script loading")
import subprocess
import os
from os import listdir
from os.path import isfile, join
import time
from cmd.scripts.close.customprograms import custom_programs


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


def init():
    print("Loading program closer")
    
def runScript(argString):
    stopWords = [
    "open",
    "please",
    "now"
    ]
    filtered = removeFilters(argString,stopWords)
    print(filtered)
    _prog = filtered[0]
    if _prog.lower() in custom_programs:
        print("TASKKILL /F /IM "+custom_programs[_prog.lower()])
        subprocess.call("TASKKILL /F /IM "+custom_programs[_prog.lower()])
    else:
        subprocess.call("TASKKILL /F /IM "+_prog+".exe")