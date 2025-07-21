import time
from datetime import datetime

log_file_path = "alog1/f1.log"  # Change to your log file path

with open(log_file_path, "a") as f:
    while True:
        log_line = f"{datetime.now().isoformat()} - INFO -----------_____----- This is a test log line\n"
        f.write(log_line)
        f.flush()  # Ensure it writes immediately
        print(f"Wrote log: {log_line.strip()}")
        time.sleep(3)

