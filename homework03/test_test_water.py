import json
from test_water import *
import pytest

#with open("turbidity_data.json", 'r') as f:
   # water_data = json.load(f)

data ={}
data['info']=[]
data['info'].append( {'cal':1, 'detect': 2})
data['info'].append( {'cal':2, 'detect': 4})
i=0


def test_current_turbidity():
    assert isinstance(current_turbidity(data['info'], 'cal','detect',i), float) == True
    assert current_turbidity(data['info'], 'cal','detect',0)==2
    assert current_turbidity(data['info'], 'cal','detect',1)==8

def test_calc_time():
    assert calc_time(5)==79.66446710032875
    assert calc_time(6)==88.68907721463003
    assert isinstance(calc_time(1), float) == True

    
