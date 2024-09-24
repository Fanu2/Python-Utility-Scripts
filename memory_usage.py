import psutil

memory_info = psutil.virtual_memory()
print(f"Total Memory: {memory_info.total}")
print(f"Available Memory: {memory_info.available}")
print(f"Used Memory: {memory_info.used}")
print(f"Percentage: {memory_info.percent}%")
