import json
from random import seed
import random

def rand_comp():
    list=['stony','iron','stony-iron']
    val= random.choice(list)
    return val

def rand_lat():
    val = random.random()*2
    val = 16 + val
    return val
def rand_long():
    val = random.random()*2
    val =82 +val
    return val


meteorite_data={}
meteorite_data['sites']=[]
for i in range(1,6):
    meteorite_data['sites'].append({'site_id' : i, 'latitude' : rand_lat() , 'longitude' : rand_long() , 'composition' : rand_comp()})

with open('site_generate.json', 'w') as out:
    json.dump(meteorite_data,out,indent=2)

