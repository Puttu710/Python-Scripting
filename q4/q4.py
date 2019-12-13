#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 08:25:13 2019

@author: surbhi
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

my_url='https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=12b73a3f-652d-4966-87a3-6c38c1049100'

def url_print(my_url,i):
    url_next = my_url+"&page="+str(i)
    uclient=ureq(url_next)
    page_html=uclient.read()
    uclient.close()
    return page_html	

def specif(container):
     speci1=container.findAll("li",{"class":"tVe95H"})
     speci1a=speci1[0].text
                
     speci1b=speci1[1].text
                
     speci1c=speci1[2].text
     speci1d=speci1[3].text
     return speci1a,speci1b,speci1c,speci1d
                  
filename="collection1.csv"
f=open(filename,"w")

header="MOBILE_NAME RATING PRICE RAM SIZE CAMERA  BATTERY PROCESSOR  CHARGE\n"
f.write(header)

for x in range(1,5):
    for i in range(1,15):
        page_html1=url_print(my_url,i)       
        page_soup=soup(page_html1,"html.parser")
        containers=page_soup.findAll("div",{"class" : "_3O0U0u"})
        try:
            container =containers[0]
        except IndexError:
                print("index error happened")
                
        for container in containers:
            name=container.findAll("div",{"class":"_3wU53n"})
            name1=name[0].text

            try:
                price=container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
                price1=price[0].text
            except Exception as inst:
                print (type(inst))
            try:        
                
                speci1a,speci1b,speci1c,speci1d=specif(container)
                '''
                trim_price1=''.join(price1.split(','))
                rm_rupee1=trim_price1.split("₹")
                add_rs_price1="Rs."+rm_rupee1[1]
                split_price1=add_rs_price1.split('N')#REMOVING no cost EMI
                final_price1=split_price1[0]
        	'''
                #split_rating1=rating1.split(" ")
                #final_rating1=split_rating1[0]
            
                #print(name1.replace(",","|")+" , "+final_price1+" , "+final_rating1+"\n")
                #f.write(name1.replace(",","|")+","+final_price1+","+","+speci1a+","+speci1b+","+speci1c+","+speci1d+","+speci1e+","+speci1f+","+"\n")
                f.write(name1.replace(",","|")+","+price1+","+","+speci1a+","+speci1b+","+speci1c+","+speci1d+","+"\n")
                f.write("\n")
                
            except Exception as inst:
                print (type(inst))
            
f.close();

