# -*- coding: utf-8 -*-
import requests
import os
import random
import time

current_dir = os.path.dirname(os.path.realpath(__file__))
weatherPayload = {"APPID":"13c533755c6d8fcaad6aeb927075068a", "q":"Hyderabad, in" }
responseObj = requests.get("https://api.openweathermap.org/data/2.5/weather", params = weatherPayload)
weatherInfo = responseObj.json()

weatherDescrip = weatherInfo["weather"][0]["main"]


while (1):
	# Create a list of images for the current time of day
    file_names = []
    
    current_hour = time.localtime().tm_hour
    if weatherDescrip == "Thunderstorm":
        if (current_hour >= 4 and current_hour <= 7):
            current_time_of_day= "sunrise"
        elif (current_hour >= 8 and current_hour <= 11):
            current_time_of_day= "morning"
        elif (current_hour >= 12 and current_hour <= 16):
            current_time_of_day= "afternoon"
        elif (current_hour >= 17 and current_hour <= 19):
            current_time_of_day= "sunset"
        elif (current_hour >= 20 or current_hour <= 3):
            current_time_of_day= "night"
            
    current_hour = time.localtime().tm_hour 
    if weatherDescrip == "Drizzle":
        if (current_hour >= 4 and current_hour <= 7):
            current_time_of_day= "sunrise"
        elif (current_hour >= 8 and current_hour <= 11):
            current_time_of_day= "morning"
        elif (current_hour >= 12 and current_hour <= 16):
            current_time_of_day= "afternoon"
        elif (current_hour >= 17 and current_hour <= 19):
            current_time_of_day= "sunset"
        elif (current_hour >= 20 or current_hour <= 3):
            current_time_of_day= "night"
            
    current_hour = time.localtime().tm_hour        
    if weatherDescrip == "Rain":
        if (current_hour >= 4 and current_hour <= 7):
            current_time_of_day= "sunrise"
        elif (current_hour >= 8 and current_hour <= 11):
            current_time_of_day= "morning"
        elif (current_hour >= 12 and current_hour <= 16):
            current_time_of_day= "afternoon"
        elif (current_hour >= 17 and current_hour <= 19):
            current_time_of_day= "sunset"
        elif (current_hour >= 20 or current_hour <= 3):
            current_time_of_day= "night"
            
    current_hour = time.localtime().tm_hour        
    if weatherDescrip == "Snow":
        if (current_hour >= 4 and current_hour <= 7):
            current_time_of_day= "sunrise"
        elif (current_hour >= 8 and current_hour <= 11):
            current_time_of_day= "morning"
        elif (current_hour >= 12 and current_hour <= 16):
            current_time_of_day= "afternoon"
        elif (current_hour >= 17 and current_hour <= 19):
            current_time_of_day= "sunset"
        elif (current_hour >= 20 or current_hour <= 3):
            current_time_of_day= "night"
            
    current_hour = time.localtime().tm_hour        
    if weatherDescrip == "Clouds":
        if (current_hour >= 4 and current_hour <= 7):
            current_time_of_day= "sunrise"
        elif (current_hour >= 8 and current_hour <= 11):
            current_time_of_day= "morning"
        elif (current_hour >= 12 and current_hour <= 16):
            current_time_of_day= "afternoon"
        elif (current_hour >= 17 and current_hour <= 19):
            current_time_of_day= "sunset"
        elif (current_hour >= 20 or current_hour <= 3):
            current_time_of_day= "night"
            
    current_hour = time.localtime().tm_hour        
    if weatherDescrip == "Mist":
        if (current_hour >= 4 and current_hour <= 7):
            current_time_of_day= "sunrise"
        elif (current_hour >= 8 and current_hour <= 11):
            current_time_of_day= "morning"
        elif (current_hour >= 12 and current_hour <= 16):
            current_time_of_day= "afternoon"
        elif (current_hour >= 17 and current_hour <= 19):
            current_time_of_day= "sunset"
        elif (current_hour >= 20 or current_hour <= 3):
            current_time_of_day= "night"
    for path, dirs, files in os.walk(current_dir + "/wallpapers/" + current_time_of_day):
        for file in files:
            file_names.append(file)

	# Choose a random wallpaper for the current time of day every 30 minutes
    image_name = random.choice(file_names)
    image_path = current_dir + "/wallpapers/" + current_time_of_day + "/" + image_name
    
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri '" + "file://" + image_path + "'")	
    time.sleep(30)