#code to get consecutive numbers

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