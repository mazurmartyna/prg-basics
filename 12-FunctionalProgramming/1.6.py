distance = int(input("Enter the distance in km: "))
hours = int(input("Enter the number of travel hours: "))
minutes = int(input("Enter the number of travel minutes: "))

avg_speed = lambda distance, hours, minutes: round(distance/(hours+ minutes/60),2)

print(f"Average speed: {avg_speed(distance, hours, minutes)} km/h")