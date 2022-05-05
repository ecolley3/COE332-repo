# Operation Kubert Storm
## Description
This assignment uses kubernetes to store and run multiple server applications. Our Flask and Redis applications are deployed and run in the kubernetes server. Used Dockerfile and app.py from hw5 and created deployment, service, and pvc files for redis. Also created deployment and service files for Flask api.

## Instructions
1) Run `kubectl apply -f ecolley3-test-flask-deployment.yml`
2) Run `kubectl apply -f ecolley3-test-flask-service.yml`
3) Run pods using `kubectl get pods -o wide` This should output information about your pods, including IP addresses.
4) Run `kubectl get services`
5) Run `kubectl exec -it ecolley3-test-flask-deployment-` your number ID `--/bin/bash`. This should put you in the root.
6) Use `pip3 install redis` in the root then use curl and the IP address given by your pods to run your `app.py` with -X POST to get the data. Example: `curl "newIP":5000/data -X POST`
7) Run `curl "newIP":5000/data` to output your data. The final data should look similar to this:
``` bash
{
    "name": "Christina",
    "id": "10300",
    "recclass": "H5",
    "mass (g)": "4291",
    "reclat": "-38.1533",
    "reclong": "-46.7127",
    "GeoLocation": "(-38.1533, -46.7127)"
  }
  ```
