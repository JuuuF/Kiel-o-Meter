# User module imports
import constants as c
import networking
import storage

# Python module imports
import json
from time import sleep
from datetime import datetime


# Print the system status variables
def print_status():
    print(f"[INFO] Fetching every {c.FETCH_DELAY} seconds.")
    print(f"[INFO] Fetching timeout: {c.FETCH_TIMEOUT} seconds.")
    print(flush=True)


# Mock for data collection function
def collect_data():
    print("Service up.")
    print_status()

    while True:
        print("Fetching data...", flush=True)
        data = networking.fetch_all_stops()

        data_dict = storage.convert_fetched_data_to_dict(data)

        storage.store_data(data_dict)

        print(end="", flush=True)
        sleep(c.FETCH_DELAY)


if __name__ == "__main__":
    collect_data()
