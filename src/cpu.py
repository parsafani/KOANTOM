
import cpuinfo
import psutil


def get_cpu_info():
    cpu = cpuinfo.get_cpu_info()
    freq = psutil.cpu_freq()

    return {
        "name": cpu["brand_raw"],
        "cores": psutil.cpu_count(logical=False),
        "threads": psutil.cpu_count(logical=True),
        "current_mhz": round(freq.current),
        "max_mhz": round(freq.max),
    }


if __name__ == "__main__":
    info = get_cpu_info()

    print("=" * 40)
    print("KOANTOM CPU Scanner")
    print("=" * 40)
    print(f"CPU      : {info['name']}")
    print(f"Cores    : {info['cores']}")
    print(f"Threads  : {info['threads']}")
    print(f"Current  : {info['current_mhz']} MHz")
    print(f"Maximum  : {info['max_mhz']} MHz")