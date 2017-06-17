# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:24:58 2017

@author: Pradeep 
"""
###
import urllib2
import json
import demjson
k=0
while True:
#####################bot379578526:AAGDRqKr3d2N8uWj6sHuBC3fS8_mOaEpqkk in the below link have to be raplaced by your bot's token 
    #Gets the data from the user in JSON Format     
    a=urllib2.urlopen('https://api.telegram.org/bot379578526:AAGDRqKr3d2N8uWj6sHuBC3fS8_mOaEpqkk/getUpdates').read(10000)
    b=demjson.decode(a) 
    c=b[u'result']
    d=c[len(c)-1]    
    e=d[u'message']
    f=str(e[u'text'])
    f1=e[u'chat']
    g=f1[u'id']
    if(len(c)!=k):
        if (f=='hi'):
            urllib2.urlopen('https://api.telegram.org/bot379578526:AAGDRqKr3d2N8uWj6sHuBC3fS8_mOaEpqkk/sendmessage?chat_id='+str(g)+'&text=hello sir how are you').read(1000)
        elif(f=='good')or(f=='great'):
            urllib2.urlopen('https://api.telegram.org/bot379578526:AAGDRqKr3d2N8uWj6sHuBC3fS8_mOaEpqkk/sendmessage?chat_id='+str(g)+'&text=Try Asking me for updates').read(1000)
        elif(f=='news' or f=='updates'):
            an=urllib2.urlopen('https://newsapi.org/v1/articles?source=the-hindu&sortBy=top&apiKey=06705564ed41406486025a5ebb1abe50').read(100000)
            urllib2.urlopen('https://api.telegram.org/bot379578526:AAGDRqKr3d2N8uWj6sHuBC3fS8_mOaEpqkk/sendmessage?chat_id='+str(g)+'&text=Please Be Patient as our servers are slow ').read(1000)
            bn=demjson.decode(an) 
            cn=bn[u'articles']
            
            """Hindu"""
            for i in cn:
                try:
                    urllib2.urlopen('https://api.telegram.org/bot379578526:AAGDRqKr3d2N8uWj6sHuBC3fS8_mOaEpqkk/sendmessage?chat_id='+str(g)+'&text='+i[u'description']).read(1000)
                    
                except:
                    pass
        elif(f=='sports news'):
            an=urllib2.urlopen('https://newsapi.org/v1/articles?source=espn&sortBy=top&apiKey=06705564ed41406486025a5ebb1abe50').read(100000)
            urllib2.urlopen('https://api.telegram.org/bot379578526:AAGDRqKr3d2N8uWj6sHuBC3fS8_mOaEpqkk/sendmessage?chat_id='+str(g)+'&text=Please Be Patient as our servers are slow ').read(1000)
            bn=demjson.decode(an) 
            cn=bn[u'articles']
            
            """ESPN"""
            for i in cn:
                try:
                    urllib2.urlopen('https://api.telegram.org/bot379578526:AAGDRqKr3d2N8uWj6sHuBC3fS8_mOaEpqkk/sendmessage?chat_id='+str(g)+'&text='+i[u'description']).read(1000)
                    
                except:
                    pass
            urllib2.urlopen('https://api.telegram.org/bot379578526:AAGDRqKr3d2N8uWj6sHuBC3fS8_mOaEpqkk/sendmessage?chat_id='+str(g)+'&text=Thats All').read(1000)
        
        else:
            urllib2.urlopen('https://api.telegram.org/bot379578526:AAGDRqKr3d2N8uWj6sHuBC3fS8_mOaEpqkk/sendmessage?chat_id='+str(g)+'&text=I am sorry I should learn more ').read(1000)
        k=len(c)
        print(k)
#https://api.telegram.org/bot364810864:AAH4lY0Ru-EYT6ga-OVab3D-GIfq8NHZdUs/getupdates
