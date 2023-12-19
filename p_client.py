#!/usr/bin/env python3

from prometheus_client import start_wsgi_server, Gauge, Counter
import psutil
import time

# CPU metrics
userTime = Gauge('cpu_user_time', 'CPU Time in User space')
systemTime = Gauge('cpu_system_time', 'CPU Time in System space')
idleTime = Gauge('cpu_idle_time', 'CPU Time in idle')
cpuUtilization = Gauge('cpu_utilization', 'CPU Utilization')

# Memory metrics
totalMemory = Gauge('system_total_memory', 'System total memory')
availMemory = Gauge('system_available_memory', 'System available memory')

# Disk metrics
freeDisk = Gauge('system_free_disk', 'System free disk space')
readCount = Counter('system_disk_read_count', 'System disk read count')
writeCount = Counter('system_disk_write_count', 'System disk write count')

# Network metrics
netSent = Counter('system_network_bytes_sent', 'System network bytes sent')
netReceived = Counter('system_network_bytes_received', 'System network bytes received')
netConnections = Gauge('system_network_connections', 'System network connections')

# Process metrics
numProcs = Gauge('system_process_count', 'Number of processes running on the system')

if __name__ == '__main__':
	# discard the first result of cpu_percent
	psutil.cpu_percent(interval=None)

	start_wsgi_server(8000)
	while True:
		times = psutil.cpu_times()
		memory = psutil.virtual_memory()
		diskIO = psutil.disk_io_counters(nowrap=True)
		netIO = psutil.net_io_counters(nowrap=True)
		connections = psutil.net_connections(kind='all')
		pids = psutil.pids()
		
		userTime.set(times[0])
		systemTime.set(times[2])
		idleTime.set(times[3])
		cpuUtilization.set(psutil.cpu_percent(interval=None))
		totalMemory.set(memory[0])
		availMemory.set(memory[1])
		readCount.inc(diskIO[0])
		writeCount.inc(diskIO[1])
		netSent.inc(netIO[0])
		netReceived.inc(netIO[1])
		netConnections.set(len(connections))
		numProcs.set(len(pids))
		time.sleep(1)
