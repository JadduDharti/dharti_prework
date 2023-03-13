#code to get odd_number



def odd_number1():
    for i in range(1,101,2):
        print(i)

def odd_number():
    num = list(range(1,101))
    for no in num:
        if no % 2 != 0:
            print(no)

odd_number()