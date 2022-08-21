## Project Description

NEEDS RABBIT MQ SERVER.

http_server.py runs the HTTP server.

request_server.py creates a connection with the http server and Rabbit MQ.

api.py runs the REST API to create two endpoints: views and total_views.

formatter.py converts the event to a json file to serve the endpoints.

run_server.bat runs all the python scripts

## Dynamic

When starts the http server (localhost/8080), select one of the three pages for try the events.

Then, go to views by url or total views to see the two endpoints created by the api.
