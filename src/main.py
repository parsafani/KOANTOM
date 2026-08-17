
from cpu import get_cpu_info

print("=" * 45)
print("        KOANTOM v0.2")
print("=" * 45)

info = get_cpu_info()

print(f"CPU      : {info['name']}")
print(f"Cores    : {info['cores']}")
print(f"Threads  : {info['threads']}")
print(f"Current  : {info['current_mhz']} MHz")
print(f"Maximum  : {info['max_mhz']} MHz")