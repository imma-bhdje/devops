import os
import random
import time
import unittest
import subprocess
import psutil
from prometheus_client import start_http_server, Summary, Gauge
from test_calculator import TestCalculator

# Create metrics to track time spent, CPU usage, and memory usage.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
CPU_USAGE = Gauge('cpu_usage_percent', 'CPU usage in percent')
MEMORY_USAGE = Gauge('memory_usage_percent', 'Memory usage in percent')

def get_memory_usage():
    # Get the current memory usage in percent
    return psutil.virtual_memory().percent

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)

    # Generate some requests.
    while True:
        # Decorate the process_request function with metric.
        # Get the current CPU usage of the hello_world.py process and update the metric.
        processes = [p for p in psutil.process_iter(['name', 'pid']) if p.info['name'] == 'python' and p.info['pid'] != os.getpid()]
        if len(processes) > 0:
            cpu_percent = processes[0].cpu_percent()
            CPU_USAGE.set(cpu_percent)
        else:
            # Set CPU usage to 0 if the hello_world.py process is not found
            CPU_USAGE.set(0)
        # Get the current memory usage and update the metric.
        memory_usage_percent = get_memory_usage()
        MEMORY_USAGE.set(memory_usage_percent)

        # Execute the wrapped process_request function.

        # Execute a Python script
        subprocess.run(['python', 'test_calculator.py'])

