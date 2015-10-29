#!/usr/bin/env python


import urllib,json
import unicodedata
import pprint
import time

#insert your Google API key
APIkey=''

     


def translateToFile(word):
    translatedList=[]
    data=""
    
    
    for language in listOflanguages:
        url=  "https://www.googleapis.com/language/translate/v2?q=" + word + "&?client=t&target=" + language + "&format=text&source=en&key=" + APIkey
        
        #calling the Google Translate API for each Slavic language
        result = json.load(urllib.urlopen(url))
      
        #extracting the word from JSON result  
        text = result['data']['translations'][0]['translatedText']
        
        #handling special characters
        text=text.encode('utf-8')
        
        translatedList.append(text)
    
    #saving each translation in format [lang],[original word],[translated word] for future analysis in MS Excel
    for i in range(0,12):
        
        data=data+listOflanguages[i]+','+word+','+translatedList[i]
    
            
        data=data+',\n'
    
    text_file = open("translated_words.txt", "a")

    text_file.write(data)

    text_file.close()
    
 


#START

#Words will be loaded from Swadesh list. This list is containing 207 basic words which were standardised by linquist Morris Swadesh.
#It is in English, so this scripts translates from English to target languages
mainlist = []
infile = open('swadesh_list.txt','r')
for line in infile:
    mainlist.append(line.strip())

infile.close()

#This is Google Translate API's naming of languages which are parameters inserted to query
listOflanguages=["cs","pl","hr","sl","ru","uk","sr","bg","be","sk","bs","mk"]

listTranslated=[]

for word in mainlist:
    print word
    translateToFile(word)
    
    #You can delete time sleep, but I didn't want to send many requests at once from my API
    time.sleep(3)
    
    