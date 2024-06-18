import psutil
import time
import os
import matplotlib.pyplot as plt
from threading import Thread, Event


def monitor_cpu_usage(interval_sec: int) -> tuple[list[float], list[float], Thread, Event]:
    
    '''
    Monitors the CPU usage at specified intervals.

    Args:
        interval_sec (int): Interval in seconds at which CPU usage is measured.

    Returns:
        Tuple[List[float], List[float], Thread, Event]: A tuple containing:
            - List of CPU usage percentages
            - List of timestamps corresponding to the CPU usage measurements
            - Thread object running the CPU monitoring
            - Event object to signal the monitoring thread to stop
    '''

    def cpu_monitor(cpu_percentages: list[float], times: list[float], stop_monitor: Event):

        '''
        Records CPU usage percentages and timestamps at regular intervals.

        Args:
            cpu_percentages (List[float]): List to store CPU usage percentages.
            times (List[float]): List to store timestamps.
            stop_monitor (Event): Event to signal when to stop monitoring.
        '''

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


def monitor_cpu_decorator(func: callable) -> callable:

    '''
    Decorator to monitor CPU usage while executing the decorated function.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function with CPU usage monitoring.
    '''

    def wrapper(*args, **kwargs):

        '''
        Wrapper function to monitor CPU usage during the execution of the original function.

        Args:
            *args (Any): Positional arguments for the original function.
            **kwargs (Any): Keyword arguments for the original function.

        Returns:
            Any: The result of the original function.
        '''

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
        plt.savefig('../plots/cpu_usage_3.png')

        return result

    return wrapper
