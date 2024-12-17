r_speed = [48,47,54,50,42,68,39,46]

result = list(filter(lambda x:x>50, r_speed ))

print("Recorded values: ", r_speed)
print("Speed too high: ",result)