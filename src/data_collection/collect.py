from time import sleep


# Mock for data collection function
def collect_data():
    print("Service up.")
    while True:
        print("Data Collection Mock.", flush=True)
        sleep(5)


if __name__ == "__main__":
    collect_data()
