import threading

import time
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)


def log_writer():
    while True:
        logging.info('Logging some info...')
        time.sleep(10)

    # Set up a daemon thread for logging


logging_thread = threading.Thread(target=log_writer)
logging_thread.daemon = True
logging_thread.start()

# Main application logic

for i in range(5):
    print(f"Main thread iteration {i}")
    time.sleep(2)

print("Main thread is finishing...")
