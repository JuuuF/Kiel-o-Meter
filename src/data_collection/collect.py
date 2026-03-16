from time import sleep
from os import environ
from functools import cache

# Read the Reddit API secret
@cache
def get_api_secret():
    with open("/run/secrets/reddit_api_secret", "r") as f:
        return f.read().strip()


# Mock for data collection function
def collect_data():
    print("Service up.")
    while True:
        print("Data Collection Mock.")
        print(f"Variable test: {(t := environ.get('DC__DEV__TEST_VAR'))} ({bool(t)})")
        print(f"Secret: {bool(get_api_secret())}, len={len(get_api_secret())}")
        print(end="", flush=True)
        sleep(5)


if __name__ == "__main__":
    collect_data()
