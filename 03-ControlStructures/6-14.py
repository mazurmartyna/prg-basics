facebook = False
twitter = True
instagram = False

if facebook == True:
    if twitter or instagram:
        print('You are a good influencer!')
    print('You are not a good influencer :/ ')
elif twitter == True:
    if instagram:
        print('You are a good influencer!')
    print('You are not a good influencer :/ ')
else:
    print('You are not a good influencer :/ ')