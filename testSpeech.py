import boto3
from pygame import mixer
import os
import time
from random import randint

my_path = os.path.abspath(os.path.dirname(__file__))

print(my_path)

class TextToSpeech:

    
    polly = None
    
    def __init__(self):
        global polly
        polly = boto3.client('polly')


    def TTS(self,text="",voice="Brian",outputFormat="mp3",fileName="output"):
        fileName = fileName+str(randint(100000000,999999999))
        spoken_text = polly.synthesize_speech(Text=text,OutputFormat=outputFormat,VoiceId=voice)
        
        with open(my_path+"/audio/"+fileName+'.'+outputFormat,"wb") as f:
            f.write(spoken_text['AudioStream'].read())
            f.close()
            
        mixer.init()
        mixer.music.load(my_path+"/audio/"+fileName+'.'+outputFormat)
        mixer.music.play()

        while mixer.music.get_busy() == True:
            pass
        mixer.music.stop()
        mixer.quit()
        time.sleep(1)
        try:
            os.remove(my_path+"/audio/"+fileName+'.'+outputFormat)
        except:
            print("")
    
#tt = TextToSpeech() 
#tt.TTS(text="Hello my old friend, I am back and ready to work")

