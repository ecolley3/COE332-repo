# Ready for Redis
## Description of contents
Creating a Redis database that runs in the background, then use a containerized Flask application that creates said database from meteorite landing data.

## How to Start a Redis Database and Run the Flask App From Docker
1) Open two windows in your shell, and in the first, log into tacc and create a new directory.
2) In the this directory run this command: `docker run -d -p 6379:6379 -v $(pwd)/data:/data:rw --name=<DockerUsername>-redis redis:6 save 1 1`
3) After logging into isp, Use `touch Dockerfile` to create a Dockerfile.
4) Create a new file called `requirements.txt` using `emacs requirements.txt`.
5) In the file, type `Flask 2.0.3` on one line and `redis` on another. Save this file and exit.
6) Use `emacs Dockerfile` to edit the file and type
```bash

FROM python:3.9

RUN mkdir /app
RUN pip3 install --user redis
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /app

ENTRYPOINT ["python"]
CMD ["app.py"]
```
5) After this step, use these commands to open the flask app:
``` bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run -p 5009
```

## Running the App using Curl
1) In the second terminal log into TACC and run the command `curl localhost:5009/data -X POST`. The app should return that the data has been read.
2) Then run the command `curl localhost:5009/data` and data should be outputted and formatted. It should look like this:
 ```bash
 {
        "name": "Mary",
        "id": "10295",
        "recclass": "EH4",
        "mass (g)": "7533",
        "reclat": "-15.7062",
        "reclong": "-19.2370",
        "GeoLocation": "(-15.7062, -19.2370)"
    },
 ```
This contains all of the information on each meteorite sighting with things such as mass, names, and locations.
