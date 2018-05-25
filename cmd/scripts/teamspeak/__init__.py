#print("Open Script loading")
import subprocess
import os
from os import listdir
from os.path import isfile, join
import time
from cmd.scripts.teamspeak.teamspeakApi import teamspeak as ts3ApO

from random import randint

definedClients = {}
#definedClients["test"] = "9HLctfKEcH0G44FRSI9hibTfWPY="
definedClients["anon"] = "Anon_Gaming"
definedClients["me"] = "Anon_Gaming"

    
#ts3Api = None
    
ts3Api = ts3ApO(HOST="ts1.anongaming.com",USERNAME="serveradmin",PASSWORD="streetdance3d",nickname="QueryBot"+str(randint(0,9999)))



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
    
    
def movechannel(argString):
    stopWords = [
    "move",
    "teamspeak",
    "to",
    "in",
    "channel",
    ]
    args = removeFilters(argString,stopWords)
    
    print(args)
    _target = args[0]
    if len(args) > 1:
        _endTarg = args[1]
    else:
        _endTarg = "Anon_Gaming"
        
    if _target in definedClients:
        _target = definedClients[_target]
        
    _targCli = ts3Api.getClient(name=_target)
    print(_targCli)
    
    if _endTarg == "out":
       ts3Api.kick(clid=_targCli['clid'],reasonid=4) 
       return
    
    if _endTarg in definedClients:
        _endTarg = definedClients[_endTarg]
        
        
    _endCli = ts3Api.getClient(name=_endTarg)
    
    ts3Api.move(clid=_targCli['clid'],cid=_endCli['cid'])
    
        
def joinchannel(clientHandle,args):
    print(" ")
    print("CMD: Join Channel")
    print(args)
    print(" ")
    
    _target = "Anon_Gaming"
    _endTarg = args[0]
    
    if _target in definedClients:
        _target = definedClients[_target]
        
    _targCli = ts3Api.getClient(name=_target)
    
    if _endTarg in definedClients:
        _endTarg = definedClients[_endTarg]
        
    _endCli = ts3Api.getClient(name=_endTarg)
    
    ts3Api.move(clid=_targCli['clid'],cid=_endCli['cid'])
    
def kickClient(argString):
    stopWords = [
    "kick",
    "from",
    "the",
    "in"
    ]
    args = removeFilters(argString,stopWords)
    print(args)
    
    
    _target = args[0]
    if _target in definedClients:
        _target = definedClients[_target]
    _targCli = ts3Api.getClient(name=_target)    
        
    if "channel" in args:
        ts3Api.kick(clid=_targCli['clid'],reasonid=4)
    else:
        ts3Api.kick(clid=_targCli['clid'],reasonid=5)
    
    
def kickClientChannel(args):
    pass
    
    
def bringhere(argString):
    stopWords = [
    "bring",
    "to",
    "channel",
    "my",
    "me",
    "this",
    "in",
    "teamspeak"
    ]
    args = removeFilters(argString,stopWords)
    print(args)
    
    
    _target = args[0]
    if _target in definedClients:
        _target = definedClients[_target]
    _targCli = ts3Api.getClient(name=_target)  
    
    _endCli = ts3Api.getClient(name="Anon_Gaming")
    ts3Api.move(clid=_targCli['clid'],cid=_endCli['cid'])
    
        

def init():
    print("Loading program teamspeak")
    #ts3Api.init(ts3Api,HOST="ts1.anongaming.com",USERNAME="serveradmin",PASSWORD="streetdance3d",nickname="AnonSlave3")
    
    
    
    #movechannel(["wizard","bunny"])
    
    #kickClient(["anon"])
    
    #bringhere(["dusty"])
    
    #cli = teamspeak.getClient("By0Uizfnzk01Lk+JXWeKq1NmlWc=")
    #teamspeak.move(cli['clid'],11)
    
    
def runScript(args):
    print("Close script Running")
    _prog = args[0].lower()
    if _prog.lower() in custom_programs:
        print("TASKKILL /F /IM "+custom_programs[_prog.lower()])
        subprocess.call("TASKKILL /F /IM "+custom_programs[_prog.lower()])
    else:
        subprocess.call("TASKKILL /F /IM "+_prog+".exe")