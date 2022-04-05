from flask import Flask, request
import json
import redis
import logging

app = Flask(__name__)
meteor_data={}

@app.route('/data',methods=['POST'])
    def load_data():
    """
    Loads data from JSON file and reports when the data is read.
    """
    n=redis.Redis(host='172.17.0.12', port=6379)
    logging.info('loading data')
    global ml_data
    with open('ML_Data_Sample.json' , 'r') as f:
        ml_data =json.load(f)
    for d in ml_data['meteorite_landings']:
        rd.set(d['id'],json.dumps(d))
    return f'Data was loaded\n'

@app.route('/data', methods=['GET'])
def name():
    """
    Passes through list of meteor sites.
    Returns:
    list of sight names
    """
    n = redis.Redis(host='172.17.0.12', port=6379)
    logging.info("Finding site names")
    list_of_data = []
    for i in range(10001, 10301, 1):
        list_of_data.append(json.loads(rd.get(i)))
    return json.dumps(list_of_data, indent=4)+'\n'
