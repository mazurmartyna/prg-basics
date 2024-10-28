time = input('Enter time (24-hour format): ')

hour = int(time[0:2])

if hour < 12:
    print(f'Time in 12-hour format: {hour}:{time[3:5]}AM')
elif hour == 12:
    print(f'Time in 12-hour format: {hour}:{time[3:5]}PM')
else:
    print(f'Time in 12-hour format: {hour-12}:{time[3:5]}PM')
