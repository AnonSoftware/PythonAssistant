import os
import sys
from inspect import getmembers, isfunction
import json
import re
import inspect
import numpy as np
import json

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import fetch_20newsgroups
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel


categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']

from sklearn.datasets import fetch_20newsgroups 
twenty_train = fetch_20newsgroups(subset='train',categories=categories, shuffle=True, random_state=42)
#twenty_train.target_names['alt.atheism', 'comp.graphics', 'sci.med', 'soc.religion.christian']

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)

print(count_vect.vocabulary_.get(u'rob'))


numberToString = {}

def stringToArr(str):
    str = str.lower()
    strS = str.split(' ')
    strArr = []
    if len(strS) > 0:
        for s in strS:
            st = count_vect.vocabulary_.get(s)
            if st == None:
                st = 0
            numberToString[st] = s
            strArr.append(st)
    print(str)
    print(strArr)
    
    if len(strArr) < 30:
        dif = 30 - len(strArr)
        for d in range(len(strArr),30):
            strArr.append(0)
    print(strArr)
    return strArr
    
    
##commandLoader

trainingData = []
trainingLabels = []
labelFunctions = []
    
    
clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('feature_selection', SelectFromModel(LinearSVC(penalty="l1", dual=False,tol=1e-3))),('classification', LinearSVC(penalty="l2"))])
    
    
    
    
##Neural Training
convertedTraining = []
convertedLabels = []
    
    
my_path = os.path.abspath(os.path.dirname(__file__))
def loadCommands():
        
    global trainingData
    global trainingLabels
    global labelFunctions
    global convertedLabels
    global convertedTraining
    global clf
    
    print("Loading Commands")
    os.chdir(my_path+"/scripts")
    
    
    script_folders = [d for d in os.listdir('.') if os.path.isdir(d)]
    
    
    for dir in script_folders:
        if dir != "__pycache__":
            print("Loading "+dir)
            dirLoc = my_path+"/scripts/"+dir
            file = open(dirLoc+"/cmd.txt","r")
            jsonCon = file.read()
            file.close()
            
            jsonCon = json.loads(jsonCon)
                
            
            mod = __import__("cmd.scripts."+dir+".__init__",fromlist=[''])  
            
            #print(jsonCon)
            
            if "cmds" in jsonCon:
                all_functions = inspect.getmembers(mod, inspect.isfunction)
                for cmd in jsonCon["cmds"]:
                    if "name" in cmd and "example" in cmd:
                        cmdName = cmd["name"]
                        cmdExamples = cmd["example"]
                        
                        cmdFuction = cmd["function"]
                        cmdFunc = print
                        for cm in all_functions:
                            if cm[0] == cmdFuction:
                                cmdFunc = cm[1]
                        
                        dat = ''.join(str(e+", ") for e in cmdExamples)
                        
                        trainingData.append(dat)
                        
                        trainingLabels.append(len(labelFunctions))
                        labelFunctions.append(cmdFunc)
    #print(trainingData)
    print("Data")   
    
    print(trainingData)
    print(trainingLabels)
    clf = clf.fit(trainingData,trainingLabels)  
  


def runCommand(cmd):
    try:
        #perdict = stringToArr(cmd)
        #pred = int(clf.predict([perdict]))
        pred = clf.predict([cmd])
        print(pred)
        print(labelFunctions[pred[0]])
        try:
            ran = labelFunctions[pred[0]](cmd)
        except:
            ran = False
        
        print(ran)
        if ran == True:
            return True
        
        return False
    except:
        return False
        
        