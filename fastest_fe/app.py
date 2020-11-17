import os
import socket
from urllib.parse import urljoin

import requests
from fastapi import FastAPI, Request, Body, Query
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="./templates")

app = FastAPI()

BACK_END_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")


@app.get("/")
def root(request: Request, ip: str = Query("")):
    data = {}

    if ip:        
        try:            
            socket.inet_aton(ip)
            url = urljoin(BACK_END_URL, ip)
            print(url)
            data = requests.get(url).json()            
        except socket.error as e:            
            data = dict(error=f"Invalid IP Address: {ip}")
        except Exception as e:
            data = dict(error=e)

    context = {
        "data": data,
        "ip": ip,
        "request": request
    }
    return templates.TemplateResponse("index.html", context)