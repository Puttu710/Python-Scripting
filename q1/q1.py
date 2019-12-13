# -*- coding: utf-8 -*-
import math 

overseas_batsman1=[]
indian_batsman1=[]
overseas_bowler=[]
indian_bowler=[]
overseas_wicket=[]
indian_wicket=[]
overseas_allroun=[]
indian_allroun=[]
data_set = {}
with open("data_team.txt") as f:
    for line in f:
        values = line.split(":")
        if(values[0] in data_set):
            data_set[values[0]][1].append(values[2])
            data_set[values[0]][2].append(values[3][:-1])
        else:
            data_set[values[0]] = [values[1],[values[2]],[values[3][:-1]],False]
        if(values[1]!='India' and values[2]=='Batsman'):
            overseas_batsman1.append(values[0])
        if(values[1]=='India' and values[2]=='Batsman'):
            indian_batsman1.append(values[0])
        if(values[1]!='India' and values[2]=='Bowler'):
            overseas_bowler.append(values[0])
        if(values[1]=='India' and values[2]=='Bowler'):
            indian_bowler.append(values[0])
        if(values[1]!='India' and values[2]=='Wicket Keeper'):
            overseas_wicket.append(values[0])
        if(values[1]=='India' and values[2]=='Wicket Keeper'):
            indian_wicket.append(values[0])
        if(values[1]!='India' and values[2]=='All-Rounder'):
            overseas_allroun.append(values[0])
        if(values[1]=='India' and values[2]=='All-Rounder'):
            indian_allroun.append(values[0])
                    
#print(overseas_batsman1)
#print(indian_wicket)
config1={}
with open("config.txt") as f:
    for line in f:
        value1 = line.split(":")
        config1[value1[0]] =[value1[1],value1[2][:-1]]
#print(config1)

config2=[]
with open("config1.txt") as f:
    for line in f:
        value2 = line
        config2.append(value2[:-1])
#print(config2)

#print(max1)   

def create_team(team):
    fd=open("/home/surbhi/pythonQ1/"+team+".txt","w")
    count=0
    max1=config1["overseas"][1]
    min1a=config1["bowlers"][0]
    max1a=config1["bowlers"][1]
    min1b=config1["batsmen"][0]
    max1b=config1["batsmen"][1]
    min1c=config1["allrounders"][0]
    max1c=config1["allrounders"][1]
    min1d=config1["wicketkeepers"][0]
    max1d=config1["wicketkeepers"][1]
    #print(max1)
    while(count<19):
        temp1=math.ceil(int(max1)/4)
        #print(temp1)
        count1=0
        for player in overseas_batsman1:#batsman
            #print()
            if(data_set[player][3]==False):
                fd.write("Player Name: "+player+"\n")
                fd.write("Country: "+data_set[player][0]+"\n")
                fd.write("Ability: Batsman"+"\n")
                ind=data_set[player][1].index("Batsman")
                #print("ind"+str(ind))
                fd.write("Fees: "+data_set[player][2][ind]+"\n")
                fd.write("\n")
                data_set[player][3]=True
                count1+=1
                if(count1==temp1): break
            
        count2=0
        for player in overseas_bowler:#batsman
            #print()
            if(data_set[player][3]==False):
                fd.write("Player Name: "+player+"\n")
                fd.write("Country: "+data_set[player][0]+"\n")
                fd.write("Ability: Bowler"+"\n")
                ind=data_set[player][1].index("Bowler")
                #print("ind"+str(ind))
                fd.write("Fees: "+data_set[player][2][ind]+"\n")
                fd.write("\n")
                data_set[player][3]=True
                count2+=1
                if(count2==temp1): break
            
        count3=0
        for player in overseas_allroun:#batsman
            #print()
            if(data_set[player][3]==False):
                fd.write("Player Name: "+player+"\n")
                fd.write("Country: "+data_set[player][0]+"\n")
                fd.write("Ability: All-Rounder"+"\n")
                ind=data_set[player][1].index("All-Rounder")
                #print("ind"+str(ind))
                fd.write("Fees: "+data_set[player][2][ind]+"\n")
                fd.write("\n")
                data_set[player][3]=True
                count3+=1
                if(count3==temp1): break
        '''  
        temp2=int(max1)-6
        while(temp2>0):
           for player in overseas_wicket:#Wicket keeper(infinite loop)
            #print()
            if(data_set[player][3]==False):
                fd.write("Player Name: "+player+"\n")
                fd.write("Country: "+data_set[player][0]+"\n")
                fd.write("Ability: Wicket Keeper"+"\n")
                ind=data_set[player][1].index("Wicket Keeper")
                #print("ind"+str(ind))
                fd.write("Fees: "+data_set[player][2][ind]+"\n")
                fd.write("\n")
                data_set[player][3]=True 
                temp2=temp2-1
                if(temp2==0): break
        '''
        
        for player in indian_bowler:#bowler
            #print(int(min1a))
            if(data_set[player][3]==False and int(max1a)>=count2 ):
                #print(int(min1a))
                fd.write("Player Name: "+player+"\n")
                fd.write("Country: "+data_set[player][0]+"\n")
                fd.write("Ability: Bowler"+"\n")
                ind=data_set[player][1].index("Bowler")
                #print("ind"+str(ind))
                fd.write("Fees: "+data_set[player][2][ind]+"\n")
                fd.write("\n")
                data_set[player][3]=True
                count2+=1
                if(count2==max1a): break
            
        for player in indian_batsman1:#indian batsman
            #print(int(min1a))
            if(data_set[player][3]==False and int(min1b)>=count1 and int(max1b)>=count1 ):
                #print(int(min1a))
                fd.write("Player Name: "+player+"\n")
                fd.write("Country: "+data_set[player][0]+"\n")
                fd.write("Ability: Batsman"+"\n")
                ind=data_set[player][1].index("Batsman")
                #print("ind"+str(ind))
                fd.write("Fees: "+data_set[player][2][ind]+"\n")
                fd.write("\n")
                data_set[player][3]=True
                count1+=1
                if(count1==max1b): break
            
            
        for player in indian_allroun:#bowler
            #print(int(min1a))
            if(data_set[player][3]==False and int(min1c)>=count3 and int(max1c)>=count3 ):
                #print(int(min1a))
                fd.write("Player Name: "+player+"\n")
                fd.write("Country: "+data_set[player][0]+"\n")
                fd.write("Ability: All-Rounder"+"\n")
                ind=data_set[player][1].index("All-Rounder")
                #print("ind"+str(ind))
                fd.write("Fees: "+data_set[player][2][ind]+"\n")
                fd.write("\n")
                data_set[player][3]=True
                count3+=1
                if(count3==max1c): break
            
        count4=0
        for player in indian_wicket:#bowler
            #print(int(min1a))
            if(data_set[player][3]==False and int(min1d)>=count4 and int(max1d)>=count4 ):
                #print(int(min1a))
                fd.write("Player Name: "+player+"\n")
                fd.write("Country: "+data_set[player][0]+"\n")
                fd.write("Ability: Wicket Keeper"+"\n")
                ind=data_set[player][1].index("Wicket Keeper")
                #print("ind"+str(ind))
                fd.write("Fees: "+data_set[player][2][ind]+"\n")
                fd.write("\n")
                data_set[player][3]=True
                count4+=1
                if(count4==max1d): break
        count=20        
        
        fd.close()
  
 
    
for team in config2:
    create_team(team)
