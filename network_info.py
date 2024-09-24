import psutil

net_info = psutil.net_if_addrs()
for interface, addrs in net_info.items():
    print(f"Interface: {interface}")
    for addr in addrs:
        print(f"  Address: {addr.address}")
        print(f"  Netmask: {addr.netmask}")
        print(f"  Broadcast: {addr.broadcast}")
