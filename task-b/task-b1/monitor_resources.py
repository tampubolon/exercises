import time
import psutil
from typing import Callable


def MonitorResources(stop_event, bars=20):
    """Function to monitor system resources like CPU and memory usage."""
    print("\nMonitoring system resources. Press Ctrl+C to stop.\n")
    while not stop_event.is_set():
        cpu_usage = psutil.cpu_percent(interval=0.5)
        mem_usage = psutil.virtual_memory().percent

        cpu_percent = (cpu_usage / 100.0)
        cpu_bar = '█' * int(cpu_percent * bars) + '_' * (bars - int(cpu_percent * bars))

        mem_percent = (mem_usage / 100.0)
        mem_bar = '█' * int(mem_percent * bars) + '_' * (bars - int(mem_percent * bars))

        print(
            f"\rCPU_USAGE: |{cpu_bar}| {cpu_usage:.2f}%   MEM_USAGE: |{mem_bar}| {mem_usage:.2f}%   ",
            end="", flush=True
        )
        time.sleep(0.5)
