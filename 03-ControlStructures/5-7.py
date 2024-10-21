###
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of
# the counter
# are displayed in words, i.e. five, four, three, two, one.
#
import time

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 5:
    print(countdown)
    countdown -= 1
    time.sleep(1)  # Wait for 1 second

print('five')
time.sleep(1)  # Wait for 1 second

print('four')
time.sleep(1)  # Wait for 1 second
print('three')
time.sleep(1)  # Wait for 1 second
print('two')
time.sleep(1)  # Wait for 1 second
print('one')
time.sleep(1)  # Wait for 1 second

print("Time's up!")