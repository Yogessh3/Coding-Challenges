def isLeapYear(year):
    if(year%400==0 or (year%100!=0 and year%4==0)):
        return True
    else:
        return False
year=int(input())
print(isLeapYear(year))