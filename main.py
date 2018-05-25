#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class





import threading

import speech_recognition as sr
import pyaudio
import wave
import audioop
import cmd.commandmanager as cm
import time
import socket
from testSpeech import TextToSpeech

import json

# obtain audio from the microphone
r = sr.Recognizer()

print("Load Commands")
cm.loadCommands()
input("Continue?")
time.sleep(1)

ttls = TextToSpeech()


def listen(sock):
    while True:
        data = sock.recv(1024)
        data = data.decode()
        print(data)
        
        data = json.loads(data)
        
        if data["cmd"] == True:
            print("Run Command")
            ran = cm.runCommand(data["cmd"])
        else:
            ttls.TTS(text=data["text"])

            
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#sock.connect(("54.37.16.172",4545))
#sock.connect(("192.168.1.5",4545))
#sock.send(str.encode("register anon"))
#t = threading.Thread(target=listen,args=[sock])
#t.start()

            
            
            
def recog(audio):
        
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        returnText = r.recognize_google(audio)
        print("Google: " + returnText)
        
        ran = cm.runCommand(returnText)
        if ran == False:
            #Send CMD to server
            pass
        
        
        #sock.send(str.encode(returnText))
        
        
        #tempS = returnText.split(" ")
        
        #cm.runCommand("open",[tempS[1]])
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
#
p = pyaudio.PyAudio()
inputIndex  = 0
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print ("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
        if "SteelSeries" in p.get_device_info_by_host_api_device_index(0, i).get('name'):
            inputIndex = i
            print("Found index ",i)
    
    
def waitForTap():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    
    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=inputIndex)
    dataArr = []
    
    countDown = False
    count = 0
    
    waveFile = wave.open("recording.wav", 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(p.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    print("Recording")
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        rms = audioop.rms(data, 2)    # here's where you calculate the volume
        #print(rms)
        
        waveFile.writeframes(data)
        if (rms > 150):
            print("Vol: "+str(rms))
            #print("allow count down")
            countDown = True
            count = 0
            dataArr.append(data)
            
        else:
            if (countDown == True) :
                count = count + 1
                #print(count)
           
        if (count > 50):
            stream.stop_stream()
            stream.close()
            p.terminate()
            break
    #print(dataArr)
    print("Saving")
    waveFile.close()

    if (len(dataArr) > 0):
        return True
    else:
        return False
    
useVoice = input("Enable Voice (y/n):")
    
voice = False
if useVoice == "y":
    voice = True    
    
    
while True:
    
    #print("Listening for audio")
    
    #recorded = waitForTap()
    
    
    
    
    
    if voice == False:
    
        cmd = input("Query: ")
        
        ran = cm.runCommand(cmd)
        
        if ran == False:
            #Send CMD to server
            pass
            #cm.runCommand(cmdList[0],cmdList[1])
    
    else:
        
        recorded = waitForTap()
        if recorded == True:
        
            with sr.WavFile("recording.wav") as source:
                audio = r.record(source)
                print("Recog Audio")
                #recog(audio)
                RecogThread = threading.Thread(target=recog,args=[audio]) #recog(audio)
                RecogThread.start()
        else:
            print("No audio recorded")
            
            
            