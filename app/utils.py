import os
import socket

def container_id():
    return os.environ.get("HOSTNAME") or socket.gethostname()

def s3_public_url(bucket, region, key):
    return f"https://{bucket}.s3.{region}.amazonaws.com/{key}"

