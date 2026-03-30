# Python module imports
from time import sleep


def process_data():
    while True:
        print("Mocking data processing...", flush=True)
        sleep(5)


if __name__ == "__main__":
    process_data()
