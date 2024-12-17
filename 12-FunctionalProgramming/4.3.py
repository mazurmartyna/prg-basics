f_grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

positive_grades = list(filter(lambda x: x>2,f_grades))

result = round(sum(positive_grades) / len(positive_grades),2)

print("Arithmetic mean for grades <> 2.0 is", result)

