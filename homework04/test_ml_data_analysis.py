import json
from ml_data_analysis import *
import pytest

data ={}
data['info']=[]
data['info'].append( {'a_key_string':1})
data['info'].append( {'a_key_string':2})


def test_compute_average_mass():
    assert isinstance(compute_average_mass(data['info'],'a_key_string'), float) == True
    assert compute_average_mass(data['info'], 'a_key_string')==1.5
    assert isinstance(compute_average_mass(data['info'], 'a_key_string'),str)==False
def test_compute_average_mass_exceptions():
    with pytest.raises(KeyError):
        compute_average_mass([{'a_key_string':1}],'a_key_strng')
    with pytest.raises(NameError):
        compute_averae_mass([{'a_key_string':1}],'a_key_string')
def test_check_hemisphere():
    assert check_hemisphere(1.5,2)== 'Northern & Eastern'
    assert check_hemisphere(1.5,-0.5)== 'Northern & Western'
    assert check_hemisphere(-0.5,2)== 'Southern & Eastern'
    assert check_hemisphere(-0.5,-0.5)== 'Southern & Western'
def test_check_hemisphere_exceptions():
    with pytest.raises(NameError):
        check_hemsphere([{2,0.5}])
def test_count_classes():
    assert isinstance(count_classes(data['info'], 'a_key_string'),dict)==True
    assert isinstance(count_classes(data['info'], 'a_key_string'),float)==False
    assert isinstance(count_classes(data['info'], 'a_key_string'),str)==False
def test_count_classes_exceptions():
    with pytest.raises(KeyError):
        count_classes([{'a_key_string':1}],'a_key_strng')
    with pytest.raises(NameError):
        count_clases([{'a_key_string':1}],'a_key_string')
