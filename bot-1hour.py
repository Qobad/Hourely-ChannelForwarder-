




## Install python packeges
##        telethon
##        python-decouple
##        python-socks



## Set socks proxy on 3080 or change port in  this app




APP_ID="your app ID"
API_HASH="your App hash"
source=-100..........

destination=-100..........




import time
from datetime import datetime, timedelta,timezone
from telethon.sync import TelegramClient
from telethon import functions, types
from decouple import config
from telethon.sessions import StringSession
from telethon.tl.types import 	InputMessagesFilterVideo,InputMessagesFilterDocument


#++++++++++++++++++++++++++++++++++++

def uploader(mediatype,date_of_post,last_date_of_post):
    print("Fetching Data ")
    
    if mediatype=="Doc" :
        allmessages=client.iter_messages(source , filter=InputMessagesFilterDocument,offset_date=date_of_post,reverse=True)

    else:
        allmessages=client.iter_messages(source , filter=InputMessagesFilterVideo,offset_date=date_of_post,reverse=True)

    
    print("\n")

    counter=0
    
    for event in allmessages:
        if  event.date < last_date_of_post and  event.media.document.mime_type!='image/jpeg':
            media = event.media.document
            counter +=1
            print("uploaded  :", str(counter) + '\r', end='')
            client.forward_messages(destination, event)
    print('  from  ' ,date_of_post ,' to ',last_date_of_post, counter,  mediatype , '  uploaded ')
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            
print(datetime.now(tz=timezone.utc))
with TelegramClient('my robot', APP_ID, API_HASH,proxy=("socks5", '127.0.0.1', 3080)) as client:

    uploading=False
    while True:
        thisminute=datetime.now(tz=timezone.utc).strftime("%H:%M:%S")[3:5]
        
        if thisminute=="00" and not uploading:
            date_of_post = datetime.now(tz=timezone.utc)- timedelta(hours=1)
            date_of_post=date_of_post.replace(minute=0,second =0, microsecond =0)
            last_date_of_post=date_of_post+timedelta(hours=1)
            print(thisminute)
            uploading=True
            uploader("Doc",date_of_post,last_date_of_post)
            uploader("Vid",date_of_post,last_date_of_post)
            
        elif thisminute=="55":
            uploading=False

        time.sleep(30)
        print("waiting  :", str(datetime.now(tz=timezone.utc).time().strftime("%H:%M:%S")) + '\r', end='')

