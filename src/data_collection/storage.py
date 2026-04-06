# User module imports
import constants as c

# Python module imports
import json
from datetime import datetime
from io import BytesIO
from minio import Minio
from zlib import compress

# ------------------------------------------------------------------------
# Initialization

# Initialize Client
client = Minio(
    endpoint="minio:9000",
    access_key=c.MINIO_ROOT_USER,
    secret_key=c.MINIO_ROOT_PASSWORD,
    secure=False,
)


# Initialize bucket if not existing
if not client.bucket_exists(c.MINIO_BUCKET_RAW):
    client.make_bucket(c.MINIO_BUCKET_RAW)
    print(f"Created MinIO bucket {c.MINIO_BUCKET_RAW} for raw API data.", flush=True)

# ------------------------------------------------------------------------


def get_storage_path() -> str:
    """
    Get the file path for uploading into the data lake.

    The file is comprised of the current time.
    """
    now = datetime.now()

    base_dir = "raw"
    date_dir = f"date={now:%Y-%m-%d}"
    data_file = f"file_{now:%Y-%m-%d_%H-%M-%S}.data"
    return "/".join([base_dir, date_dir, data_file])


def store_data(data_dict: dict) -> None:
    """
    Store data dict as compressed JSON file in the data lake.
    """

    # Convert to JSON
    json_data = json.dumps(data_dict)
    # Compress JSON string
    json_data_compressed = compress(json_data.encode())
    # Convert to BytesIO
    json_data_compressed_bytes = BytesIO(json_data_compressed)
    # Upload to data lake
    client.put_object(
        bucket_name=c.MINIO_BUCKET_RAW,
        object_name=get_storage_path(),
        data=json_data_compressed_bytes,
        length=len(json_data_compressed_bytes.getvalue()),
    )


def store_data_file(
    data_dict: dict,
    filepath: str = "/opt/data_collection/output.json",
) -> bool:
    """
    Store data as JSON file.
    """

    try:
        json.dump(
            data_dict,
            open(filepath, "w"),
            ensure_ascii=False,
        )
        return True
    except Exception as e:
        print(f"[ERROR] Could not save data: {e}")
        return False
