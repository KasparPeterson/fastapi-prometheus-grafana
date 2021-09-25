import time
import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
import some_logger

app = FastAPI()
logger = some_logger.get()


@app.get("/")
def home():
    logger.debug("request to /")
    time.sleep(random.randint(0, 5))
    logger.debug("response to / - Hello World")
    return "Hello World"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Instrumentator().instrument(app).expose(app)
