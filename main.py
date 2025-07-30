from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Template
import uvicorn
import json

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_dashboard():
    with open("dashboard.html", "r", encoding="utf-8") as f:
        template = Template(f.read())
    with open("event_data.json", "r", encoding="utf-8") as f:
        events = json.load(f)
    return template.render(events=events)

@app.get("/health")
def health_check():
    return {"status": "OK"}