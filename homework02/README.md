METEORITE DATA AND ROBOT TRAVEL

 Repository containing homework02 files : meteorite_list.py, robot.py, site_generate.json

  Meteorite_list.py contains functions that randomly generate latitude, longitude, and compositon for meteorites 5 times. 
This information is then composed into a list and stored in site_generate.json.
Site_generate.json can vary in contents, this version is just a sample of my json file after the code was compiled.


Robot.py takes the information from site_generate.json and reads it, outputting the trip data of a robot that would travel and sample each meteorite. (robot starts at lat=16.0   and lon=82.0)
 
  In order to use the files in linux, use "python3 meteorite_list.py" to create the site_generate.json list.
Then use "python3 robot.py" to output the robot trip data. The data for each leg of the robots trip should be given, as well as the values for the total trip time and distance.
