# User module imports
import constants as c
import networking

# Python module imports
from time import sleep
from os import environ


# Mock for data collection function
def collect_data():
    print("Service up.")
    while True:
        print("Data Collection Mock.")
        res = networking.fetch_stop(c.kvg_stop_mapping["stops"][0]["id"])
        print(res)
        print(end="", flush=True)
        sleep(c.FECTH_DELAY)


if __name__ == "__main__":
    collect_data()
