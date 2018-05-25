HOST = "vps.anongaming.com"
PORT = 9987
USER = "serveradmin"
PASS = "streetdance3d"
SID = 1

# Modules
# ------------------------------------------------
import time
import ts3


ts3conn = None

channel_create_tags = {}


channel_tags_sets = {}


def client_by_uuid(uuid):
    cliList = ts3conn.clientlist()
    for c in cliList:
        info = ts3conn.clientinfo(clid=c["clid"])
        cuuid = info[0]["client_unique_identifier"]
        if cuuid == uuid:
            #print("Found: "+c["client_nickname"])
            return c



def set_ts3con(ts3con):
	global ts3conn
	ts3conn = ts3con

	
def set_createtags(tags):
	global channel_create_tags
	channel_create_tags = tags
	
def set_chantags(tags):
	global channel_tags_sets
	channel_tags_sets = tags
	
def get_chan_id_name(channelName, id =1):
    channels = ts3conn.channellist()
    for c in channels:
        #print (c["channel_name"])
        if c["channel_name"] == channelName+str(id):
            id = get_chan_id_name(channelName, id+1)
    return id

def move_to_channel(uuid, channelID):
    #client = ts3conn.clientfind(pattern=player)
    #client = [client["clid"] for client in client]
    client = client_by_uuid(uuid)
    
    #print(teamRoom+": "+clientName)
    ts3conn.clientmove(clid=client["clid"], cid=channelID)
    time.sleep(.2)
    

def create_channel(game,channelName):
    channelName = channelName+str(get_chan_id_name(channelName)).capitalize()
    
    
    chan = ts3conn.channelcreate(channel_name=channelName,channel_codec_quality=5,CHANNEL_FLAG_PERMANENT=1,CHANNEL_ORDER=channel_create_tags[game],CHANNEL_MAXFAMILYCLIENTS=5,CHANNEL_MAXCLIENTS
=5,CHANNEL_FLAG_MAXCLIENTS_UNLIMITED=0,CHANNEL_PASSWORD="123123123123123")
    channel_tags_sets[channelName] = chan[0]
    return chan[0]

def temp_channel(channelID,game = ""):
    if game != "":
        ts3conn.channeledit(cid=channelID, CHANNEL_FLAG_PERMANENT=0,CHANNEL_FLAG_TEMPORARY=1)
    else:
        ts3conn.channeledit(cid=channelID, CHANNEL_FLAG_PERMANENT=0,CHANNEL_FLAG_TEMPORARY=1,CHANNEL_ORDER=channel_create_tags[game])
        
        
def move_client_to_team_room(uuid, teamRoom,game):
    try:
        
        client = client_by_uuid(uuid)["clid"]
        #print(teamRoom+": "+clientName)
        ts3conn.clientmove(clid=client, cid=teamRoom)
        time.sleep(.2)
    except:
        return
    
    
def move_team(teamArr=[],teamRoom = "",game=""):
    channels = []
    
	
	
    if teamRoom != "":
        #CreateChannel by game_TeamName
        
        if isinstance(teamRoom, int):
             for player in teamArr:
                move_client_to_team_room(player,teamRoom,game)
        else:
        
            chan = create_channel(game,game+"_"+teamRoom)
            teamRoom = chan["cid"]
            
            for player in teamArr:
                print(player)
                move_client_to_team_room(player,teamRoom,game)
                time.sleep(.5)
            if int(teamRoom) > 40:
                temp_channel(teamRoom,game)
            return teamRoom
    else:
        if teamRoom == "" or teamRoom == None:
            tempChans = ts3conn.channellist()
            for c in tempChans:
                if game in c["channel_name"]:
                    channels.append(c)
                    
        for c in channels:
            if int(c["total_clients"]) == 0:
                teamRoom = c["cid"]
                break
        if teamRoom == "" or teamRoom == None:
            chan = create_channel(game,game+"_Team ")
            teamRoom = chan["cid"]
        
        for player in teamArr:
            move_client_to_team_room(player,teamRoom,game)
            
        
        if int(teamRoom) > 40:
            temp_channel(teamRoom,game)
        return teamRoom
    
    