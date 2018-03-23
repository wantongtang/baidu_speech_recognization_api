#!/usr/bin/env python
# coding: utf-8
import urllib2
import json
import base64
import  os


baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
grant_type = "client_credentials"
client_id = "DugZt412RfX1ZloH39eIs9i7"
client_secret = "62e0d6c023b7bf0b01c87d22b797a062"

url = baidu_server+"grant_type="+grant_type+"&client_id="+client_id+"&client_secret="+client_secret

# get tocken
res = urllib2.urlopen(url).read()
data = json.loads(res)
token = data["access_token"]
print token

# sample 8000 ,pcm  wav opus,speex,amr
VOICE_RATE = 8000
WAVE_FILE = "org.wav" 

USER_ID = "hail_hydra" 
WAVE_TYPE = "wav"

# open wav file  base64 encoding
f = open(WAVE_FILE, "r")
speech = base64.b64encode(f.read())
size = os.path.getsize(WAVE_FILE)
update = json.dumps({"format":WAVE_TYPE, "rate":VOICE_RATE, 'channel':1,'cuid':USER_ID,'token':token,'speech':speech,'len':size})
headers = { 'Content-Type' : 'application/json' } 
url = "http://vop.baidu.com/server_api"
req = urllib2.Request(url, update, headers)

r = urllib2.urlopen(req)


t = r.read()
result = json.loads(t)
print result
if result['err_msg']=='success.':
    word = result['result'][0].encode('utf-8')
    if word!='':
        if word[len(word)-3:len(word)]=='£¬':
            print word[0:len(word)-3]
        else:
            print word
    else:
        print "not found wav"
else:
    print "error"
