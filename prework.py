#question- 1 code to get hello_username

def get_user(username):
 print("Hello, " + username.title() + "!")

get_user("Dharti")


#question- 2 code to get odd_number

def odd_number1():
    for i in range(1,101,2):
        print(i)

def odd_number():
    num = list(range(1,101))
    for no in num:
        if no % 2 != 0:
            print(no)

odd_number()


#question- 3 code to get maxmimum number among list

def max_number_in_list(a_list):
    max_number = max(a_list)
    return max_number

test = max_number_in_list([4,5,20,8,10])
print(test)



#question- 4 code to get leap year

def is_leap_year(a_year):
    if a_year % 4 == 0 and (a_year % 400 ==0 or a_year % 100 != 0):
        print(str(a_year) + " is a leap year")
    else:
        print(str(a_year) + " is not leap year")

is_leap_year(2020)
is_leap_year(2019)


#question- 5 code to get consecutive numbers

def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else:
            status = False
            break
    print(status)

is_consecutive([1,2,3,4,5,6,7,8,9])
is_consecutive([1, 2, 1, 2, 1, 2])