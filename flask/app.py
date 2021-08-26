#!/usr/bin/env python
from flask import Flask
from flask_cors import CORS
import random
import psutil
import json
# from subprocess import PIPE, Popen

app = Flask(__name__)
CORS(app)

@app.route("/rpi_storage")
def get_rpi_storage():
    disk = psutil.disk_usage('/')
    disk_total = disk.total / 2**30     # GiB.
    disk_used = disk.used / 2**30
    disk_free = disk.free / 2**30
    disk_percent_used = disk.percent

    rpi_disk = {
        "disk": {
            "disk_total": disk_total,
            "disk_used": disk_used,
            "disk_free": disk_free,
            "disk_percent_used": disk_percent_used
        }
    }

    return rpi_disk

@app.route("/rpi_status")
def get_rpi_status():

    # cpu_temperature = get_cpu_temperature()
    # print(psutil.sensors_temperatures())
    # cpu_usage = psutil.cpu_percent()

    cpu_usage = psutil.cpu_percent()
    cpu_usage_per_core = psutil.cpu_percent(percpu=True)
    
    disk = psutil.disk_usage('/')
    disk_total = disk.total / 2**30     # GiB.
    disk_used = disk.used / 2**30
    disk_free = disk.free / 2**30
    disk_percent_used = disk.percent

    ram = psutil.virtual_memory()
    ram_total = ram.total / 2**20       # MiB.
    ram_used = ram.used / 2**20
    ram_free = ram.free / 2**20
    ram_percent_used = ram.percent

    swap_ram = psutil.swap_memory()
    swap_ram_total = swap_ram.total / 2**20       # MiB.
    swap_ram_used = swap_ram.used / 2**20
    swap_ram_free = swap_ram.free / 2**20
    swap_ram_percent_used = swap_ram.percent

    cpufreq = psutil.cpu_freq()
    max_cpufreq=cpufreq.max
    min_cpufreq=cpufreq.min
    current_cpufreq = cpufreq.current

    # uname = platform.uname()
    # sys_name = uname.system
    # sys_release = uname.release
    # sys_version = uname.version
    # sys_processor = uname.processor

    rpi_obj = {
        "temperatures": {
                "cpu": random.randint(1, 100)
            },
        "cpu_usage": {
            "total_cpu_usage": cpu_usage,
            "cpu_usage_per_core": cpu_usage_per_core
        },
        "disk": {
            "disk_total": disk_total,
            "disk_used": disk_used,
            "disk_free": disk_free,
            "disk_percent_used": disk_percent_used
        },
        "ram": {
            "ram_total": ram_total,
            "ram_used": ram_used,
            "ram_free": ram_free,
            "ram_percent_used": ram_percent_used
        },
        "swap_ram": {
            "swap_ram_total": swap_ram_total,
            "swap_ram_used": swap_ram_used,
            "swap_ram_free": swap_ram_free,
            "swap_ram_percent_used": swap_ram_percent_used
        }
    }

    rpi_obj_string = json.dumps(rpi_obj)

    return rpi_obj



# def get_cpu_temperature():
#     process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
#     output, _error = process.communicate()
#     return float(output[output.index('=') + 1:output.rindex("'")])


# def main():
    # cpu_temperature = get_cpu_temperature()
    # cpu_usage = psutil.cpu_percent()
    
    # ram = psutil.phymem_usage()
    # ram_total = ram.total / 2**20       # MiB.
    # ram_used = ram.used / 2**20
    # ram_free = ram.free / 2**20
    # ram_percent_used = ram.percent
    
    # disk = psutil.disk_usage('/')
    # disk_total = disk.total / 2**30     # GiB.
    # disk_used = disk.used / 2**30
    # disk_free = disk.free / 2**30
    # disk_percent_used = disk.percent
    # # 
    # # Print top five processes in terms of virtual memory usage.
    # # 
    # processes = sorted(
    #     ((p.get_memory_info().vms, p) for p in psutil.process_iter()),
    #     reverse=True
    # )
    # for virtual_memory, process in processes[:5]:
    #     print virtual_memory // 2**20, process.pid, process.name


# if __name__ == '__main__':
#     main()
