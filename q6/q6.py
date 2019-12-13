import requests
import schedule
import time
from bs4 import BeautifulSoup
import json
from PyAccessPoint import pyaccesspoint
from pynotifier import Notification
import random

def studybreak():
    Notification(
	title='Study Break',
	description='Study hard for good job',
	icon_path='/home/tushar/Desktop/book.jpg', 
	duration=5,                              
	urgency=Notification.URGENCY_CRITICAL
).send()
    
def waterbreak():
    Notification(
	title='Water Break',
	description='You should drink 3 litre of water',
	icon_path='/home/tushar/Desktop/water.jpeg', 
	duration=5,                              
	urgency=Notification.URGENCY_CRITICAL
).send()
def checktimetable():
    Notification(
	title='Check time table',
	description='Be aware of OS class',
	icon_path='/home/tushar/Desktop/tt.jpeg', 
	duration=5,                              
	urgency=Notification.URGENCY_CRITICAL
).send()     

def print_headlines(response_text):
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = soup.find_all(attrs={"itemprop": "headline"})
    i=1
    for headline in headlines:
        print(i)
        print(headline.text)
        i=i+1
        print('-------------------------------------------------------------')

def hotspot():
    access_point = pyaccesspoint.AccessPoint()
    access_point.start()
def randomchallenege():
    f = open('a.txt', "r")
    lines = f.readlines()
    f.close()
    i=random.randint(0, 5)
    x=lines[i]
    temp=x.split("~")
    pname=temp[0]
    link=temp[1]
    print("Today's programming challenge is:"+" "+ pname)
    print("link for the challenge"+":"+link)


url = 'https://inshorts.com/en/read'
response = requests.get(url)
print_headlines(response.text)
#hotspot()
randomchallenege()
schedule.every(15).minutes.do(waterbreak)
schedule.every().hour.do(studybreak)
schedule.every().day.at("08:00").do(checktimetable)
while True:  
    schedule.run_pending() 
    time.sleep(1)
