# leap year function
def is_leap(year):
    if (year % 400 == 0) and (year % 100 == 0):
        print("{0} is a leap year".format(year))

    elif (year % 4 ==0) and (year % 100 != 0):
        print("{0} is a leap year".format(year))

    
    else:
        print("{0} is not a leap year".format(year))
year=int(input("Insert Year :"))
is_leap(year)        