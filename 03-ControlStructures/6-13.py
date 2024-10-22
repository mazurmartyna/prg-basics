car_speed = int(input('Enter car speed: '))
speed_limit_min = 41
speed_limit_max = 141

if car_speed < speed_limit_min and car_speed > speed_limit_max:
    print('Warning: invalid car speed!!')
