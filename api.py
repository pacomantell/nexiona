import json
from fastapi import FastAPI
import uvicorn
app = FastAPI()


# Create an endpoint with views by url
@app.get('/views')
async def getViews():
    with open('num_views.json', 'r') as openfile:
        return json.load(openfile)


# Create an endpoint with the total views
@app.get('/total_views')
async def getTotalViews():
    with open('tot_views.json', 'r') as openfile:
        return json.load(openfile)

uvicorn.run(app, host='localhost', port=8000)
