ms = int(input("Enter the speed: "))

def ms_to_kmh(ms):
    result = ms * 3.6
    return result

km = ms_to_kmh(ms)

print(f"{ms} m/s = {km} km/h")