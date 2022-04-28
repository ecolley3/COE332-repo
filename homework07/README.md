# Delightful Diagram
## Description
This Diagram contains a simplified version of how the API routes work within my ISS midterm project. When the user calls specific routes within the diagram, my application returns all of the data associated with that route. The user may choose what data to access and how specific they wish their data to be.


![Untitled Diagram drawio](https://user-images.githubusercontent.com/97973860/165677049-863e0e23-d36c-401a-b615-ef4e1a96da2e.png)


## How to read and access the information once the application is downloaded
1) First, two shells will need to be open on isp. In the first shell input only these commands:
```bash 
export FLASK_APP=app.py
export FLASK_ENV=development
flask run -p 5000
```
2) Next, open a second shell and use `curl localhost:5000/load_data -X POST` to load and read all of the data.
3) If you wish to know what each route does, use `curl localhost:5000/help`.

## Accessing the data and specific routes
After running the `curl localhost:5000/load_data -X POST` command, a number of routes can be taken.
### To access EPOCHS data: Run these two commands.
1) `curl localhost:5000/epoch` to access the list of all EPOCHS.
2) `curl localhost:5000/epoch/<epoch>` to access data from a specific EPOCH.
### To access the data from specific places: Run these series of commands.
1) `curl localhost:5000/count` to access the list of all countries.
2) `curl localhost:5000/count/<count>` to access the data from a specific country.
3) `curl localhost:5000/count/<count>/region` to access the list of all regions.
4) `curl localhost:5000/count/<count>/region/<region>` to access the data from a specific region.
5) `curl localhost:5000/count/<count>/region/<region>/city` to access the list of all cities.
6) `curl localhost:5000/count/<count>/region/<region>/city/<city>` to access the data from a specific city.

Each data point accessed represents a different ISS sighting location that can easily be analyzed using the app routes given.
