# User module imports
import constants as c
from sample_processor import SampleProcessor

# Python module imports
from time import sleep


def process_data():

    # Get sample processor
    sample_processor = SampleProcessor.load()

    # Wait for initialization
    sample_processor.wait_for_data_lake()

    # Main loop
    while True:
        # Check for unprocessed samples
        if not sample_processor.data_lake_has_unprocessed_files():
            sleep(c.DATA_LAKE_REFRESH_TIME)
            continue

        # Update all unprocessed samples
        sample_processor.update_database()


if __name__ == "__main__":
    process_data()
