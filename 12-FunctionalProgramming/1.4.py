ms = int(input("Enter the speed in ms: "))

ms_to_kmh = lambda ms: ms*3.6

print(f"{ms} m/s = {ms_to_kmh(ms)} km/h")