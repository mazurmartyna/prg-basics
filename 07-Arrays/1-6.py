def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n]

if __name__ == "__main__":
    day = int(input('Number for the day of the week: '))
    print(weekday(day-1))