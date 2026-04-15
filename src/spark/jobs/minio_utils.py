"""
File for MinIO communication for spark jobs.
"""

import boto3
from functools import cache
from botocore.client import Config

# ------------------------------------------------------------------------
# MinIO connectivity


@cache
def get_minio_client() -> boto3.client:
    client = boto3.client(
        "s3",
        endpoint_url="http://minio:9000",
        aws_access_key_id="minioadmin",
        aws_secret_access_key="minioadmin",
        config=Config(signature_version="s3v4"),
        region_name="eu-central-1",
    )
    return client
