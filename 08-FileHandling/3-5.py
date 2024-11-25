##
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input('Type in your username: ')
password = input('Type in your password: ')

# pattern (criteria) for username and password
username_pattern = '[a-z]{6}'
password_pattern = '^[\w]+[\w]{7}$'

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern, password)

# print results
if username_match and password_match:
   print('Correct username and password')
else:
   print('Incorrect username or password!!!')