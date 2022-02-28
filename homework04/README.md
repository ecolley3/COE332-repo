# The Joys of Containerization with Docker 

## Description
This project asked us to update the ml_data_analysis.py file, then to make a test file and put both of them into a conatiner on Docker. (As well as Meteorite_Landings.json)
The test and changes to ml_data_analysis are then run in Docker so that anyone may pull them and be able to run them from the container.

## Files
`ml_data_analysis.py` has been modified to be able to run without using the python3 command, and it also dislplays meteorite data such as average mass, location, and class in a much more simple and concise manner.
`test_ml_data_analysis.py` has been written to do unit testing for the functions in the previous file, all tests should pass if the code is working properly.
`Meteorite_Landings.json` contains all the the data pertaining to the meteorites that will be read and outputted when `ml_data_analysis.py` runs.

## How to Run the Code Using Docker
1)To get access to the files, use `docker pull ecolley3/ml_data_analysis:hw04`\
2)Next, run `docker build -t ecolley3/ml_data_analysis:hw04 .` to build your container. It should give an output of: 
```bash 
docker build -t ecolley3/ml_data_analysis:hw04 .
Sending build context to Docker daemon  36.86kB
Step 1/10 : FROM centos:7.9.2009
 ---> eeb6ee3f44bd
Step 2/10 : RUN yum update -y
 ---> Using cache
 ---> f412cd73b2c4
Step 3/10 : RUN yum install -y python3
 ---> Using cache
 ---> 9754c2b75a6c
Step 4/10 : RUN pip3 install pytest==7.0.0
 ---> Using cache
 ---> f78a483af15c
Step 5/10 : COPY ml_data_analysis.py /code/ml_data_analysis.py
 ---> Using cache
 ---> ac66c467f9f1
Step 6/10 : COPY test_ml_data_analysis.py /code/test_ml_data_analysis.py
 ---> Using cache
 ---> a6800a61d195
Step 7/10 : COPY Meteorite_Landings.json /code/Meteorite_Landings.json
 ---> Using cache
 ---> 30458c5b65b0
Step 8/10 : RUN chmod +rx /code/ml_data_analysis.py
 ---> Using cache
 ---> e9a7871711b5
Step 9/10 : RUN chmod +rx /code/test_ml_data_analysis.py
 ---> Using cache
 ---> 1511bcfe07c4
Step 10/10 : ENV PATH "/code:$PATH"
 ---> Using cache
 ---> 3385eeceaae1
Successfully built 3385eeceaae1
``` 
\
3) After this, use the `docker run --rm -it -v $PWD:/data ecolley3/ml_data_analysis:hw04 /bin/bash` To open the container, and then `cd /code` to open the directory with your files. Type `ml_data_analysis.py /data/Meteorite_Landings.json` to run the code using the data in the container, and the output should look like this:
``` bash 
Average mass of the meteors are:
 83857.3 grams


Summary of Hemisphere data:
There were  21  meteors found in the Northern and Eastern quadrant
There were  6  meteors found in the Northern and Western quadrant
There were  0  meteors found in the Southern and Eastern quadrant
There were  3  meteors found in the Southern and Western quadrant
Class summary data:
The L5 class was found 1 times
The H6 class was found 1 times
The EH4 class was found 2 times
The Acapulcoite class was found 1 times
The L6 class was found 6 times
The LL3-6 class was found 1 times
The H5 class was found 3 times
The L class was found 2 times
The Diogenite-pm class was found 1 times
The Stone-uncl class was found 1 times
The H4 class was found 2 times
The H class was found 1 times
The Iron-IVA class was found 1 times
The CR2-an class was found 1 times
The LL5 class was found 2 times
The CI1 class was found 1 times
The L/LL4 class was found 1 times
The Eucrite-mmict class was found 1 times
The CV3 class was found 1 times
```
\
4)To use your own data, use the `wget` command followed by whatever the link to the data is, and then use the command `ml_data_analysis.py /data/yourlink` to get an output similar to the last.\
5) After you have run the code, you may run the unit test by using the `pytest` command. While still in the `/code` directory, just type in `pytest` and the unit tests should run correctly.

## Input Data
If you plan to use wget to use your own input data, keep in my that it should be formatted in a certain way. The format gives the specific keys needed so that the code may analyze the data, and it looks as follows:
``` bash 
"meteorite_landings": [
    {
      "name": "Gerald",
      "id": "10001",
      "recclass": "H4",
      "mass (g)": "5754",
      "reclat": "-75.6691",
      "reclong": "60.6936",
      "GeoLocation": "(-75.6691, 60.6936)"
    },
```
The code uses these keywords to find the specific values it needs for each data point.
