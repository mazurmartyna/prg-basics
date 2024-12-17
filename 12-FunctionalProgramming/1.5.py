distance = int(input("Enter the distance in km: "))
hours = int(input("Enter the number of travel hours: "))
minutes = int(input("Enter the number of travel minutes: "))

def avg_speed(distance, hours, minutes):
    time = hours + minutes/60
    result = round(distance/time, 2)
    return result

print("Average speed: ", avg_speed(distance, hours, minutes), "km/h")