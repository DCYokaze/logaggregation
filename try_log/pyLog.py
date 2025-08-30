import time
from datetime import datetime

log_file_path = "alog1/f1.log"  # Change to your log file path

def write_log_entry(level="INFO", message="This is a test log line"):
    """Write a log entry in the specified format"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Include milliseconds
    log_line = f"{timestamp} - {level} - {message}\n"
    return log_line

with open(log_file_path, "a") as f:
    while True:
        # Generate different types of log entries
        log_entries = [
            write_log_entry("INFO", "Application started successfully"),
            write_log_entry("DEBUG", "Processing user request"),
            write_log_entry("WARN", "Memory usage is high"),
            write_log_entry("ERROR", "Database connection failed"),
            write_log_entry("INFO", "This is a test log line"),
        ]
        
        # Write a random log entry
        import random
        log_line = random.choice(log_entries)
        f.write(log_line)
        f.flush()  # Ensure it writes immediately
        print(f"Wrote log: {log_line.strip()}")
        time.sleep(3)