import psutil
import time
import os
import matplotlib.pyplot as plt
from threading import Thread, Event


def monitor_cpu_usage(interval_sec):
    
    def cpu_monitor(cpu_percentages, times, stop_monitor):

        start_time = time.perf_counter()

        while not stop_monitor.is_set():
            cpu_percentages.append(psutil.cpu_percent(interval=interval_sec))
            times.append(time.perf_counter() - start_time)
            time.sleep(interval_sec)

    cpu_percentages = []
    times = []
    stop_monitor = Event()

    monitor_thread = Thread(target=cpu_monitor, args=(cpu_percentages, times, stop_monitor))
    monitor_thread.start()

    return cpu_percentages, times, monitor_thread, stop_monitor

# custom decorator for CPU usage monitoring
def monitor_cpu_decorator(func):

    def wrapper(*args, **kwargs):

        # start monitoring CPU usage
        cpu_percentages, times, monitor_thread, stop_monitor = monitor_cpu_usage(1)

        # call the original function
        result = func(*args, **kwargs)

        # stop monitoring CPU usage
        stop_monitor.set()
        monitor_thread.join()

        # plot CPU usage
        plt.figure(figsize=(10, 6))
        plt.plot(times, cpu_percentages, marker='o')
        plt.title('CPU Usage Over Time')
        plt.xlabel('Time (s)')
        plt.ylabel('CPU Usage (%)')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('../plots/cpu_usage.png')

        return result

    return wrapper
