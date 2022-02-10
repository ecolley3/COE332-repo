import math
import json

with open('site_generate.json', 'r') as f:
    ml_data = json.load(f)

mars_radius = 3389.5    # km

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

def compute_travel(list_of_dicts, latitude, longitude, composition):
    robo_start_lat = 16.0
    robo_start_lon = 82.0   
    travel_time=0
    for i in range(len(list_of_dicts)):
        leg = i        
        distance_point= calc_gcd(robo_start_lat, robo_start_lon, float(list_of_dicts[i][latitude]), float(list_of_dicts[i][longitude]))
        robo_start_lat= float(list_of_dicts[i][latitude])
        robo_start_lon =float(list_of_dicts[i][longitude])
        leg_time=distance_point/10
        
        if(str(list_of_dicts[i][composition])=='stony'):
            sam_time=1
        elif(str(list_of_dicts[i][composition])=='iron'):
            sam_time=2
        elif(str(list_of_dicts[i][composition])=='stony iron'):
            sam_time=3
        travel_time=travel_time+leg_time+sam_time

        print('leg =', i+1, ', travel time = ', leg_time, 'hrs, sample time = ', sam_time, 'hrs')
    print( '5 legs, total time = ', travel_time, 'hrs')
    return(0)

print(compute_travel(ml_data['sites'], 'latitude','longitude','composition'))
