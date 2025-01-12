# monitor_resources.py
import time
import psutil

def MonitorResources(stop_event, bars=50):
    while not stop_event.is_set():
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        cpu_percent = (cpu_usage / 100.0)
        cpu_bar = '█' * int(cpu_percent * bars) + '_' * (bars - int(cpu_percent * bars))

        mem_percent = (mem_usage / 100.0)
        mem_bar = '█' * int(mem_percent * bars) + '_' * (bars - int(mem_percent * bars))

        # Print the resource usage with no buffering
        print(f"\r CPU_USAGE: |{cpu_bar}| {cpu_usage:.2f}%   MEM_USAGE: |{mem_bar}| {mem_usage:.2f}%  ", end="\r", flush=True)

        time.sleep(1)  # Sleep for 1 second to allow the monitoring to update
