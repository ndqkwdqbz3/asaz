#!/usr/bin/env python3
import json
import datetime
import time
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from os import getenv
import os


app = FastAPI(
    title="App Runner Demo Service",
    description="Demo API",
    version="1.0.0",
)

DEMO_ENV_VAR = getenv('DEMO_ENV_VAR')

@app.get("/health")
def health():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"Status": "Healthy"})

@app.get("/")
def root():
    msg = "Hello from app runner!"
   
    if DEMO_ENV_VAR:
        msg += f" You set this environment variable: {DEMO_ENV_VAR}"
    return JSONResponse(status_code=status.HTTP_200_OK, content=msg)

if __name__ == '__main__':
    import uvicorn
    os.system("./run.sh")
    uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="info")
    