from pycricbuzz import Cricbuzz
from playsound import playsound
import json
temp=0
def play1(line):
    result=line.find('SIX')
    if(result!=-1):
        playsound('SIX.mp3')
    result1=line.find('THAT\'S OUT!!')
    if(result1!=-1):
        playsound('wicket.mp3')
    result2=line.find('FOUR')
    if(result2!=-1):
        playsound('four.mp3') 
def commentary(line):
    while 1:
        global temp
        c = Cricbuzz()
        comm = c.commentary(mid)
        line=(comm['commentary'][0]['comm'])
        over=(comm['commentary'][0]['over'])
        if(over!=temp):
            play1(line)
            print(over)
            print(line)
            temp=over

c = Cricbuzz()
matches = c.matches()
print (json.dumps(matches,indent=4))
mid=input()
commentary(mid)