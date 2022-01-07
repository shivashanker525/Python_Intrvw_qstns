def Leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0  and (year % 400) == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Not a leap year")

#print leap years from range of two numbers
Leap_year(2005)