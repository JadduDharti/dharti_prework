#code to get leap year

def is_leap_year(a_year):
    if a_year % 4 == 0 and (a_year % 400 ==0 or a_year % 100 != 0):
        print(str(a_year) + " is a leap year")
    else:
        print(str(a_year) + " is not leap year")

is_leap_year(2020)
is_leap_year(2019)

