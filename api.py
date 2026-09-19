from fastapi import FastAPI
from system_util import get_system_stats
import boto3

s3 = boto3.resource("s3")

app = FastAPI(title="Learn API Calling")

@app.get("/hello")
def hello():
    """
    this is for demo perpose 
    """
    return {
        "message" : "Hello"
    }

@app.get("/metrics")
def metrics():
    """ This is show the  window information """
    return get_system_stats()

@app.get("/aws/s3")
def get_bucket():
    bucket = []
    for bucket in s3.bucket.all():
        bucket.append(bucket.name)
    return bucket
