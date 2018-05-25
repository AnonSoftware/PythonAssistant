import ts3
from threading import Thread
import time

class teamspeak:

    ts3conn = None
    
    def keep_ts3_alive():
        while True:
            ts3conn.send_keepalive()
            time.sleep(5*60)
    
    def init(self,HOST="",PORT=10011,USERNAME="",PASSWORD="",SID=1,nickname=""):
        global ts3conn
        ts3conn = ts3.query.TS3Connection(HOST,PORT)
        ts3conn.login(client_login_name=USERNAME, client_login_password=PASSWORD)
        ts3conn.use(sid=SID)
        if nickname != "":
            ts3conn.clientupdate(client_nickname=nickname)
        print("init ran")
        thread = Thread(target=self.keep_ts3_alive)
        thread.start()
    
    def moveUUID(self,_uuid, _channelID):
        #Move Client By UUID
        client = self.getClient(self,_uuid)
        ts3conn.clientmove(clid=client['clid'],cid=_channelID)
        
    def move(self,_clid,_channelID):
        #move by client ID
        print("Move")
        ts3conn.clientmove(clid=_clid,cid=_channelID)
     
    def kick(self,_clid, _reason=""):
        #kick client form teamspeak
        client = self.getClient(self,_uuid)
        
    def kickUUID(self,_uuid,_reasonID=5):
        #Move Client By UUID
        client = self.getClient(self,_uuid)    
        ts3conn.clientkick(clid=client['clid'],reasonid=_reasonID)
   
    def UUIDFromName(self,name):
        #get client UUID from name
        client = getClientByName(name)
        info = ts3conn.clientinfo(clid=client['clid'])
        
    def getClient(self,uuid):
        #get client var from UUID
        cliList = ts3conn.clientlist()
        for c in cliList:
            info = ts3conn.clientinfo(clid=c["clid"])
            cuuid = info[0]["client_unique_identifier"]
            if cuuid == uuid:
                #print("Found: "+c["client_nickname"])
                return c
        return None
                
    def getClientByName(self,name):
        #get client var from Name
        cliList = ts3conn.clientlist()
        for c in cliList:
            if c["client_nickname"] == name:
                return c
        return None
        
    def getClientChannel(self,_uuid):
        cli = self.getClient(self,_uuid)
        return cli['cid']
        
        