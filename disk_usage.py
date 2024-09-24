import psutil

disk_usage = psutil.disk_usage('/')
print(f"Total Disk Space: {disk_usage.total}")
print(f"Used Disk Space: {disk_usage.used}")
print(f"Free Disk Space: {disk_usage.free}")
print(f"Percentage: {disk_usage.percent}%")
