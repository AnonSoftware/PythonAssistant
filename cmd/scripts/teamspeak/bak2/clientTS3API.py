import ts3
from threading import Thread
import time

class teamspeak:

    ts3conn = None
    
    def keep_ts3_alive(self):
        while True:
            ts3conn.exec_("use")
            time.sleep(5*60)
    
    
    
    def getClient(self,name=""):
        cliList = self.clientList()
        for k in cliList:
            if name.lower() in k['client_nickname'].lower():
                return k
        return None
        
    def getClientUUID(self,uuid=""):
        cliList = self.clientList()
        for k in cliList:
            print(k)
            uuid = self.getUUIDFromCLID(clid=k['clid'])
            print(uuid)
            if uuid == uuid:
                return k
        return None
    
    
    def getUUIDFromCLID(self,clid=0):
        
        return ts3conn.exec_("clientgetuidfromclid",clid=clid)
    
    
    def __init__(self,HOST="localhost",PORT=25639,APIKEY=""):
        global ts3conn
        ts3conn = ts3.query.TS3ClientConnection(HOST,PORT)
        ts3conn.exec_("auth", apikey=APIKEY)
        print("init ran")
        thread = Thread(target=self.keep_ts3_alive)
        thread.start()
    
    def kick(self,clid="",reasonid=4,reasonmsg=""):
        ts3conn.exec_("clientkick",clid=clid,reasonid=reasonid,reasonmsg=reasonmsg)
    
    def move(self,clid=0,cid=0):
        ts3conn.exec_("clientmove",clid=clid,cid=cid)
    
    
    def poke(self,clid=0,msg=""):
        ts3conn.exec_("clientpoke",clid=clid,msg=msg)
    
    
    def channelList(self):
        return ts3conn.exec_("channellist")
    
    
    def clientList(self,):
        return ts3conn.exec_("clientlist")
        
        
    def registerEvent(self,event):
        #event
        ts3conn.exec_("clientnotifyregister", event=event, schandlerid=0)
        
    def eventListen(self):
        return ts3conn.wait_for_event(timeout=10)
        