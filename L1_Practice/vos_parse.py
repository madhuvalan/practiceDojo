import json
import re
from collections import Counter

with open ('consul_response.txt') as fin:
        p = Counter(fin.read().split())
        j =1  
        for i in list(p.elements()):
             r1 = re.findall("(VLocationId_[1-9]+)",i)
             r2 = re.findall("ServiceID\":\"\d+",i) 
             r3 = re.findall("Serf\s+Health\s+Status\W+Status\W+passing",i)        
             if r1:
                print('{} {}'.format(j,r1))
             if r2:
                print('{} {}'.format(j,r2))
             if r3:
                print('{} {}'.format(j,r3))
             j+=1                
                 
                


           




