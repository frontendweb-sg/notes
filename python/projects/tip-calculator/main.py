def leapYear(year):
    return (year % 4 == 0 and year % 100 == 0 and year % 400 == 0)


print("Leap year")
print(leapYear(2000))
