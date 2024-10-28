
def time_string(hours, minutes, time_format):
    if time_format == '12':
        if hours == 0:
            hours=12
            midnight='AM'
        elif hours < 12:
            midnight = 'AM'
        elif hours == 12:
            midnight = 'PM'
        else:
            midnight = 'PM'
            hours = hours-12
    
        if minutes < 10:
            result = (f'{hours}:0{minutes}{midnight}')
        else:
            result = (f'{hours}:{minutes}{midnight}') 
    else:
        if hours < 10:
            if minutes < 10:
                result = (f'0{hours}:0{minutes}')
            else:
                result = (f'0{hours}:{minutes}')
        else:
            if minutes < 10:
                result = (f'{hours}:0{minutes}')
            else:
                result = (f'{hours}:{minutes}')

    return result

hours = int(input('Enter hours: '))
minutes = int(input('Enter mintues: '))
time_format = input('Enter time format (12 or 24): ')

time = time_string(hours, minutes, time_format)

print('The time is: ', time)



        

        
        