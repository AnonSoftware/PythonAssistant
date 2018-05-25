#print("Open Script loading")
import subprocess
import os
from os import listdir
from os.path import isfile, join
import time
from cmd.scripts.teamspeak.teamspeakApi import teamspeak



definedClients = {}

definedClients["brant"] = "By0Uizfnzk01Lk+JXWeKq1NmlWc="
definedClients["dusty"] = "By0Uizfnzk01Lk+JXWeKq1NmlWc="

definedClients["wizard"] = "jVLl2fZEzhNH9+b3UpmHO3E6ynA="
definedClients["bunny"] = "eUQGpBgh+F2oR1PoKRxA6bFSmxg="
definedClients["banana"] = "ok+szJKYCazfiNzHVhfvOcVIKOY="
definedClients["josh"] = "xPtVJi8O3/SraVcPBTEUxAAHM0A="
definedClients["pro"] = "DuC+tx0JNgh+mh3ieIfe5upSaJ0="
definedClients["rob"] = "tFFFv2IP+QvGvHs2aAt0hCToCTw="

definedClients["neon"] = "frJE2lvkD7aH0cF4EI2lSn+21rE="
definedClients["test"] = "yic4kGqZaWrUnWhaoXEN0/F892M="

    
#definedClients["test"] = "9HLctfKEcH0G44FRSI9hibTfWPY="
definedClients["anon"] = "9HLctfKEcH0G44FRSI9hibTfWPY="
definedClients["me"] = "9HLctfKEcH0G44FRSI9hibTfWPY="
    
ts3Api = None
    
def movechannel(args):
    print(" ")
    print("CMD: Move Channel")
    print(args)
    print(" ")
    
    _target = args[0]
    _endTarg = args[1]
    
    try:
        channelID = teamspeak.getClientChannel(teamspeak,definedClients[_endTarg])
        
        uuid = definedClients[_target]
        teamspeak.moveUUID(teamspeak,_uuid=uuid,_channelID=channelID)
        
    except:
        print("error Teamspeak api")
    
def kickClient(args):
    print(" ")
    print("CMD: Kick client")
    print(args)
    print(" ")
    
    _target = args[0]
    try:
        uuid = definedClients[_target]
        teamspeak.kickUUID(teamspeak,_uuid=uuid,_reasonID=5)
   
    except:
        print("Teamspeak api error")
        
def kickClientChannel(args):
    print(" ")
    print("CMD: Kick client")
    print(args)
    print(" ")
    
    _target = args[0]
    try:
        uuid = definedClients[_target]
        teamspeak.kickUUID(teamspeak,_uuid=uuid,_reasonID=4)
   
    except:
        print("Teamspeak api error")    
    
def bringhere(args):
    print(" ")
    print("CMD: bring client here")
    print(args)
    print(" ")
    _target = args[0]
    
    channelID = teamspeak.getClientChannel(teamspeak,definedClients["anon"])
    
    if _target in definedClients:
        uuid = definedClients[_target]
        teamspeak.moveUUID(teamspeak,_uuid=uuid,_channelID=channelID)
    
        

def init():
    print("Loading program teamspeak")
    teamspeak.init(teamspeak,HOST="ts1.anongaming.com",USERNAME="serveradmin",PASSWORD="streetdance3d",nickname="AnonSlave")
    
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