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

def test_current_turbidity_exceptions():
    with pytest.raises(IndexError):
        current_turbidity( [ {'cal' : 1, 'detect' : 2} ], 'cal',' detector', 1)
    with pytest.raises(NameError):
        current_turbidiy( [ {'cal' : 1, 'detect' : 2} ], 'cal', 'detect', 1)

def test_calc_time():
    assert calc_time(5)==79.66446710032875
    assert calc_time(6)==88.68907721463003
    assert isinstance(calc_time(1), float) == True

def test_calc_time_exceptions():
    with pytest.raises(TypeError):
        calc_time([ { 'cal' : 1}, 1 ])
    with pytest.raises(NameError):
        calc_tim([ {'cal' : 1, 'detect' : 2} ], 1)    
