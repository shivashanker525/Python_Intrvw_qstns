
def leap_year(year):
    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if year % 400 == 0 and year % 100 == 0:
        return 'Leap year'
    
    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif year % 4 == 0 and year % 100 != 0:
        return 'Leap year'
    else:
        return 'Not a leap year'
    
print(leap_year(1992))
print(leap_year(2016))
print(leap_year(2222))