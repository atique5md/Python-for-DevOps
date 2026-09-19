import psutil

def get_system_stats():
    disk = psutil.disk_usage("C:\\")
    memory = psutil.virtual_memory()
    
    return {
        "cpu_percent": psutil.cpu_percent(interval=1) ,
        " memory_percent": memory.percent,
        "memory_used_gb": round(memory.used / (1024 ** 3), 2),
        "memory_total_gb": round(memory.total / (1024 ** 3), 2),
        "disk_percent": disk.percent,
        "disk_free_gb": round(disk.free / (1024 ** 3), 2),
        "disk_total_gb": round(disk.total / (1024 ** 3), 2)
    }

# if __name__ == "__main__":
#     print(get_system_stats())

print(get_system_stats())