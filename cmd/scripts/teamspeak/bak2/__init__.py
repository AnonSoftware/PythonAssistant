#print("Open Script loading")
import subprocess
import os
from os import listdir
from os.path import isfile, join
import time
from cmd.scripts.teamspeak.clientTS3API import teamspeak
from cmd.scripts.teamspeak.testSpeech import TextToSpeech
import threading
import api.teamspeak as ts3Api



definedClients = {}
#definedClients["test"] = "9HLctfKEcH0G44FRSI9hibTfWPY="
definedClients["anon"] = "Anon_Gaming"
definedClients["me"] = "Anon_Gaming"

#ts3Api = teamspeak(APIKEY="M62Q-EVWC-ZJG6-J5A7-Z5DS-GLSZ")
#ts3Api.registerEvent("notifyclientpoke")

textTSpeech = TextToSpeech()




def pokeListen():

    while True:
        try:
            event = ts3Events.eventListen()
            for e in event:
                if "msg" in e and "invokername" in e:
                    print(e["invokername"]+" Has sent you a message of: "+e["msg"])
                    if e["msg"] == "":
                        textTSpeech.TTS(text=e["invokername"]+", Has poked you")
                    else:
                        textTSpeech.TTS(text=e["invokername"]+", Has poked you a message of: "+e["msg"],fileName=e['invokername'])
                    
                #print(e)
        except:
            print("")


def movechannel(args):
    print(" ")
    print("CMD: Move Channel")
    print(args)
    print(" ")
    
    _target = args[0]
    _endTarg = args[1]
    
    if _target in definedClients:
        _target = definedClients[_target]
        
    _targCli = ts3Api.getClient(name=_target)
    
    if _endTarg in definedClients:
        _endTarg = definedClients[_endTarg]
        
    _endCli = ts3Api.getClient(name=_endTarg)
    
    ts3Api.move(clid=_targCli['clid'],cid=_endCli['cid'])
    
    if _target != "Anon_Gaming":
        textTSpeech.TTS(text="You moved "+_targCli['client_nickname'])
    else:
        textTSpeech.TTS(text="You joined "+_endCli['client_nickname']+"'s Channel")
        
def joinchannel(args):
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
    
    if _target != "Anon_Gaming":
        textTSpeech.TTS(text="You moved "+_targCli['client_nickname'])
    else:
        textTSpeech.TTS(text="You joined "+_endCli['client_nickname']+"'s Channel")
    
def kickClient(args):
    print(" ")
    print("CMD: Kick client")
    print(args)
    print(" ")
    
    _target = args[0]
    if _target in definedClients:
        _target = definedClients[_target]
    _targCli = ts3Api.getClient(name=_target)
    
    ts3Api.kick(clid=_targCli['clid'],reasonid=5)
    
    if _target != "Anon_Gaming":
        textTSpeech.TTS(text=_target+" Was kicked from teamspeak")
    else:
        textTSpeech.TTS(text="You kicked yourself from teamspeak")
    
def kickClientChannel(args):
    print(" ")
    print("CMD: Kick client")
    print(args)
    print(" ")
    _target = args[0]
    if _target in definedClients:
        _target = definedClients[_target]
    _targCli = ts3Api.getClient(name=_target)
    
    ts3Api.kick(clid=_targCli['clid'],reasonid=4)
    if _target != "Anon_Gaming":
        textTSpeech.TTS(text=_target+", Was kicked from the channel")
    else:
        textTSpeech.TTS(text="You kicked yourself from a channel")
    
    
def bringhere(args):
    print(" ")
    print("CMD: bring client here")
    print(args)
    print(" ")
    _target = args[0]
    _targCli = ts3Api.getClient(name=_target)
    _endCli = ts3Api.getClient(name="Anon_Gaming") 
    
    ts3Api.move(clid=_targCli['clid'],cid=_endCli['cid'])
    textTSpeech.TTS(text="You brought "+_target)

def init():
    print("Loading program ts3Api")
    
    #RecogThread = threading.Thread(target=pokeListen) #recog(audio)
    #RecogThread.start()  
    
    #movechannel(["wizard","bunny"])
    
    #kickClient(["anon"])
    
    #bringhere(["dusty"])
    
    #cli = ts3Api.getClient("By0Uizfnzk01Lk+JXWeKq1NmlWc=")
    #ts3Api.move(cli['clid'],11)
    
    
def runScript(args):
    print("Close script Running")
    _prog = args[0].lower()
    if _prog.lower() in custom_programs:
        print("TASKKILL /F /IM "+custom_programs[_prog.lower()])
        subprocess.call("TASKKILL /F /IM "+custom_programs[_prog.lower()])
    else:
        subprocess.call("TASKKILL /F /IM "+_prog+".exe")