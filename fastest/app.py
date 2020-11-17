import requests
from fastapi import Request
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root(request: Request):
    url = f"http://ip-api.com/json/{request.client.host}"
    response = requests.get(url)
    return response.json()