import time
import csv
from datetime import datetime
import pygetwindow as gw

def get_active_window():
    try:
        window = gw.getActiveWindow()
        if window:
            return window.title
        return "Unknown"
    except:
        return "Unknown"

def log_activity():
    with open("data.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        print("Tracking started... Press Ctrl+C to stop.\n")

        while True:
            window = get_active_window()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            writer.writerow([timestamp, window])
            print(f"{timestamp} → {window}")

            time.sleep(5)  # logs every 5 seconds

if __name__ == "__main__":
    log_activity()