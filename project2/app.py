import time
from datetime import datetime

while True:
    with open("/data/log.txt", "a") as f:
        f.write(f"Log entry at {datetime.now()}\n")
    time.sleep(5)
