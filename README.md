## Project Description

NEEDS RABBIT MQ SERVER.

http_server.py runs the HTTP server.

request_server.py creates a connection with the http server and Rabbit MQ.

api.py runs the REST API to create two endpoints: views and total_views.

formatter.py converts the event to a json file to serve the endpoints.

run_server.bat runs all the python scripts

## Dynamic

When starts the http server (localhost/8080), just introduce an url in the browser.

Then, go to localhost/8000 (the API port) and go to the views endpoint or total_views endpoint.