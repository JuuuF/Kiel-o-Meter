# User module imports
import constants as c

# Python module imports
import json
import requests


# Fetch a single stop, based on ID
def fetch_stop(id: int) -> str:

    # Build url
    url = c.kvg_stop_url
    params = [
        f"stop={id}",
        "mode=departure",
    ]
    request_url = f"{url}?{'&'.join(params)}"

    # Fetch results
    resp = requests.get(request_url)
    if not resp.ok:
        print("[ERROR] Invalid response after fetching:", resp.status_code)
        return "{}"

    return json.loads(resp.text)
