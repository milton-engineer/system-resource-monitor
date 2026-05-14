import os
import shutil
import time


def get_uptime():
    with open("/proc/uptime", "r") as file:
        uptime_seconds = float(file.readline().split()[0])

    uptime_hours = uptime_seconds // 3600
    uptime_minutes = (uptime_seconds % 3600) // 60

    return f"{int(uptime_hours)}h {int(uptime_minutes)}m"


def get_memory_usage():
    with open("/proc/meminfo", "r") as file:
        lines = file.readlines()

    total_memory = int(lines[0].split()[1])
    free_memory = int(lines[1].split()[1])

    used_memory = total_memory - free_memory

    return used_memory // 1024, total_memory // 1024


def display_system_info():
    os.system("clear")

    print("System Resource Monitor")
    print("-" * 40)

    uptime = get_uptime()
    used_memory, total_memory = get_memory_usage()

    print(f"System Uptime : {uptime}")
    print(f"Memory Usage  : {used_memory} MB / {total_memory} MB")

    cpu_load = os.getloadavg()
    print(f"CPU Load      : {cpu_load}")


if __name__ == "__main__":
    display_system_info()
