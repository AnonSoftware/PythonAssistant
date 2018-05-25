import ts3




class teamspeak:

    
    ts3conn = None
    def __init__(self,HOST="localhost",PORT=10011,USERNAME="",PASSWORD="",nickname=""):
        self.ts3conn = ts3.query.TS3ServerConnection(HOST,PORT)
        self.ts3conn.exec_("login", client_login_name=USERNAME,client_login_password=PASSWORD)
        self.ts3conn.exec_("use",sid=1)
        self.ts3conn.exec_("clientupdate",client_nickname=nickname)
    
    def kick(self,clid="",reasonid=4,reasonmsg=""):
        self.ts3conn.exec_("clientkick",clid=clid,reasonid=reasonid,reasonmsg=reasonmsg)
    
    def move(self,clid=0,cid=0):
        self.ts3conn.exec_("clientmove",clid=clid,cid=cid)
    
    
    def channelList(self):
        return self.ts3conn.exec_("channellist")
    
    
    def clientList(self):
        return self.ts3conn.exec_("clientlist")
        
    
    
    def getClient(self,name=""):
        cliList = self.clientList()
        
        for k in cliList:
            if name.lower() in k["client_nickname"].lower():
                return k
                break
        return None