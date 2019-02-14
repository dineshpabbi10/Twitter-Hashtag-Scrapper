#!/usr/bin/env python
# coding: utf-8

# # <b style='font-family:helvetica;color:green'> Final Year Project </b></br>
# ##  <b style='font-family:helvetica;color:darkgreen'>1.) Scrapping Tweets from Twitter</b> 

# In[10]:


import tweepy
import csv
import pandas as pd
import os


# In[11]:


####input your credentials here
consumer_key = '2cpyupGz4C3gCb5GjPldt4THL'
consumer_secret = 'jhGP3AvcS15oDdeQJ5qfONiC2yiJr0ZpM4yXVzNUZJ6O4Qhzzd'
access_token = '1418613104-3z6xZ2lEbPcFGPx7OGkbV2FZeDVPQhKIWJie6CG'
access_token_secret = 'ynQp9h4oIMGRFNl3XqQjKz2VHpY5duFwEcjwxqxo9aheZ'


# In[12]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


# In[13]:


### Creating Pandas DataFrame to store Tweets
def findtweets(querry):
    t = pd.DataFrame(columns=["Date","Tweets"])
    for tweet in tweepy.Cursor(api.search,q="#"+querry+"",count=100,lang="en",since="2018-04-03").items():
        

        if(tweet.text[:2] == "RT"):
            pass
        else:
            t = t.append({"Date":tweet.created_at,"Tweets":tweet.text.replace("\n"," ")},ignore_index=True)
	 
        if len(t)==50:
            break

## Put the path of the file in the path variable.. Example path = r"G:\sss.csv"
    #path = r"C:\Users\kunalverma\Desktop\""+querry+".csv"

    p=os.path.join('C:\\','Users',os.getlogin(),'Desktop')

    path=r''+p+'\ '+querry+'.csv'
    t.to_csv(path)
    
## Top 10 Tweet Displaying on window
    dateLabel=Label(window,text='Date',font=("Helvetica",10,"bold"),background="white")
    dateLabel.place(x=40,y=160)
    tweetLabel=Label(window,text='Tweets',font=("Helvetica",10,"bold"),background="white")
    tweetLabel.place(x=130,y=160)
    
    top10=t.head(10)
    
    dates=''
    tweets=''
    char_list=''
    tweet=''
    
## Removing those Characters that Tkinter Don't display.
    for j in range(len(top10.Tweets)):
        char_list=''
        for i in range(len(top10.Tweets[j])):
            if (ord(top10.Tweets[j][i]) in range(65536) and top10.Tweets[j][i]!=' '):
                char_list+=top10.Tweets[j][i]
        for k in char_list:
            tweet=tweet+k
        tweets+=tweet+'\n\n'
        tweet=''
        print()
        
    for i in top10.Date:
        temp=str(i)
        n=temp[:10]
        dates+=n+'\n\n'

## Displaying the Data
    tempdate=str(top10.Date[0])
    dLabel1=Label(window,text=dates,font=("Helvetica",10,"bold"),background="white")
    dLabel1.place(x=40,y=205)
    tLabel1=Label(window,text=tweets,font=("Helvetica",10),background="white")
    tLabel1.place(x=130,y=205)
    
    fileaddresslabel=Label(window,text=str("Detailed File Saved at "+path),font=("Helvetica",15,"bold"),background="white")
    fileaddresslabel.place(x=40,y=550)


# # GUI

# In[14]:


from tkinter import *
from tkinter import messagebox
import base64
from urllib.request import urlopen


# In[15]:


image_url = "https://raw.githubusercontent.com/dineshpabbi10/Twitter-Hashtag-Scrapper/master/images/i1.png"
image_byt = urlopen(image_url).read()
image_b64 = base64.encodebytes(image_byt)

image_url1 = "https://raw.githubusercontent.com/dineshpabbi10/Twitter-Hashtag-Scrapper/master/images/cooltext315236238392377%20(7).png"
image_byt1 = urlopen(image_url1).read()
image_b641 = base64.encodebytes(image_byt1)


# In[16]:


def writetweet(topicEntry):
    if (str(topicEntry.get())=='' or not str(topicEntry.get())):
        message="Enter Valid Topic"
        heading="Empty Fields"
        messagebox.showinfo(heading,message)
    else:
        findtweets(str(topicEntry.get()))


# In[17]:


window=Tk()
window.geometry("1200x600+50+100")
window.title("Tweet Scrapping")
window.configure(background='white')
photo=PhotoImage(data=image_b64)
BL=Label(window,image=photo,background='white')
BL.place(x=400,y=-30)

photo1=PhotoImage(data=image_b641)
BL1=Label(window,image=photo1,background='white')
BL1.place(x=620,y=40)

txtlabel=Label(window,text='Enter Topic',font=("Helvetica",15,"bold"),background="white")
txtlabel.place(x=20,y=40)
topicEntry=Entry(window,bd=3,width=40)
topicEntry.place(x=160,y=45)
B1=Button(window,text="Submit",command=lambda: writetweet(topicEntry),bd=5,width=18,height=1)
B1.place(x=180,y=100)

#window.wm_attributes('-transparentcolor', heading['bg'])

window.mainloop()

