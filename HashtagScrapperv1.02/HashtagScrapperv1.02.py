import tweepy
import csv
import pandas as pd
from pathlib import Path
from tkinter import *
from tkinter import messagebox
import base64
from urllib.request import urlopen

## Loading Background Image for label online from the given URL
image_url = "https://i.imgur.com/W5Xc8cK.png"
image_byt = urlopen(image_url).read()
image_b64 = base64.encodebytes(image_byt)

## Module for fetching the tweets of the given topic
def getTweets(querry,number_of_tweets,consumer_key,consumer_secret_key,access_key,access_secret_key):
    
    ##Authentication
    try:
        number=int(number_of_tweets)
    except ValueError:
        message="Invalid Number of Tweets Entered"
        heading="Invalid Value"
        messagebox.showinfo(heading,message)
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
        auth.set_access_token(access_key, access_secret_key)
        api = tweepy.API(auth,wait_on_rate_limit=True)
    except:
        message="Invalid Authentication"
        heading="Invalid Keys"
        messagebox.showinfo(heading,message)
        
        
    ## Fetching n tweets recent Tweets
    try:
        t = pd.DataFrame(columns=["Date","Tweets"])
        i = 0
        for tweet in tweepy.Cursor(api.search,q="#"+querry+"",count=100,tweet_mode="extended",lang="en",since="2018-04-03").items():
            if(tweet.full_text[:2] == "RT"):
                pass
            else:
                t = t.append({"Date":tweet.created_at,"Tweets":tweet.full_text.replace("\n"," ")},ignore_index=True)
                i+=1
            if i==int(number_of_tweets):
                break
        try:
            path = Path.cwd().joinpath(querry+".csv")
            t.to_csv(path)
        except:
            message="Invalid Path"
            heading="Invalid Path"
            messagebox.showinfo(heading,message)
    
    
    
        resultLabel=Label(window,text="Total "+str(number_of_tweets)+" tweets stored in the File\n Location :\n "+str(path))
        resultLabel.config(width=32,background='#40E0D0',height=15)
        resultLabel.place(x=20,y=130)
        
    except:
        message="Bad Request"
        heading="Invalid Keys"
        messagebox.showinfo(heading,message)

## Validating the TextFields for empty values.
def validate(topicEntry,topicEntry1,consumer_keyEntry,consumer_secret_keyEntry,access_keyEntry,access_secret_keyEntry):
    if (str(topicEntry.get())=='' or not str(topicEntry.get())):
        message="Enter Valid Topic"
        heading="Empty Fields"
        messagebox.showinfo(heading,message)
    elif (str(topicEntry1.get())=='' or not str(topicEntry1.get())):
        message="Enter Valid Number of Tweets"
        heading="Empty Fields"
        messagebox.showinfo(heading,message)
    elif (str(consumer_keyEntry.get())=='' or not str(consumer_keyEntry.get())):
        message="Enter Valid Consumer Key"
        heading="Empty Fields"
        messagebox.showinfo(heading,message)
    elif (str(consumer_secret_keyEntry.get())=='' or not str(consumer_secret_keyEntry.get())):
        message="Enter Valid Consumer Secret Key"
        heading="Empty Fields"
        messagebox.showinfo(heading,message)
    elif (str(access_keyEntry.get())=='' or not str(access_keyEntry.get())):
        message="Enter Valid Access Key"
        heading="Empty Fields"
        messagebox.showinfo(heading,message)
    elif (str(access_secret_keyEntry.get())=='' or not str(access_secret_keyEntry.get())):
        message="Enter Valid Access Secret Key"
        heading="Empty Fields"
        messagebox.showinfo(heading,message)
    else:
        getTweets(str(topicEntry.get()),str(topicEntry1.get()),str(consumer_keyEntry.get()),str(consumer_secret_keyEntry.get()),str(access_keyEntry.get()),str(access_secret_keyEntry.get()))


## Main Graphical window Initiation
window=Tk()
window.geometry("620x500+350+100")
window.title("Tweet Scrapping")
window.configure(background='white')
photo=PhotoImage(data=image_b64)
BL=Label(window,image=photo,background='white')
BL.place(x=320,y=190)
    
txtlabel=Label(window,text='Topic',font=("Helvetica",10,"bold"),background="white")
txtlabel.place(x=20,y=40)
topicEntry=Entry(window,bd=3,width=20)
topicEntry.place(x=120,y=40)
    
txtlabel1=Label(window,text='No. Of Tweets',font=("Helvetica",10,"bold"),background="white")
txtlabel1.place(x=20,y=70)
topicEntry1=Entry(window,bd=3,width=20)
topicEntry1.place(x=120,y=70)
    
    ## Authentication Fields
consumer_keylabel=Label(window,text='Consumer Key',font=("Helvetica",10,"bold"),background="white")
consumer_keylabel.place(x=260,y=40)
consumer_keyEntry=Entry(window,bd=3,width=30,show="*")
consumer_keyEntry.place(x=410,y=40)
    
consumer_secret_keylabel=Label(window,text='Consumer Secret Key',font=("Helvetica",10,"bold"),background="white")
consumer_secret_keylabel.place(x=260,y=70)
consumer_secret_keyEntry=Entry(window,bd=3,width=30,show="*")
consumer_secret_keyEntry.place(x=410,y=70)
    
    
    
access_keylabel=Label(window,text='Access Key',font=("Helvetica",10,"bold"),background="white")
access_keylabel.place(x=260,y=100)
access_keyEntry=Entry(window,bd=3,width=30,show="*")
access_keyEntry.place(x=410,y=100)
    
access_secret_keylabel=Label(window,text='Access Secret Key',font=("Helvetica",10,"bold"),background="white")
access_secret_keylabel.place(x=260,y=130)
access_secret_keyEntry=Entry(window,bd=3,width=30,show="*")
access_secret_keyEntry.place(x=410,y=130)
    
    
    ## Result Entry
resultLabel=Label(window)
resultLabel.config(width=32,background='#40E0D0',height=15)
resultLabel.place(x=20,y=130)
    
B1=Button(window,text="Submit",command=lambda: validate(topicEntry,topicEntry1,consumer_keyEntry,consumer_secret_keyEntry,access_keyEntry,access_secret_keyEntry),bd=5,width=18,height=1)
B1.place(x=60,y=400)
    

window.resizable(False,False)
window.mainloop()
