import psutil

print("CPU Usage:", psutil.cpu_percent(interval=1), "%")



import psutil
import time

while True:
    print("CPU Usage:", psutil.cpu_percent(interval=1), "%")