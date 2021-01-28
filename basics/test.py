def is_it_odd(num):
    if num % 2 != 0:
        return True
    else:
        return False

rg = range(1,20)

def change_list(list,function):
    accumulator = []
    for i in list:
        if is_it_odd(i):
            accumulator.append(i)
    return accumulator

print(change_list(rg,is_it_odd))