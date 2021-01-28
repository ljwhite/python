def mult_by_2(num):
    return num * 2

times_two = mult_by_2
print("4 * 2 =",times_two(4))

def do_math(func,num):
    return func(num)

print("8 * 2 =",do_math(mult_by_2, 8))

def get_func_mult_by_num(num):
    def mult_by(value):
        return num * value

    return mult_by

generated_func = get_func_mult_by_num(5)
print("5 * 9 =",generated_func(9))

list_of_funcs = [times_two,generated_func]
# variable accepts an argument!
print("5 * 9 =",list_of_funcs[1](9))

# problem
# create a function that receives a list and a function
# function will pass T/F if list value is odd
# surrounding function will return a list of odd numbers

def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def change_list(list,func):
    odd_list = []
    for i in list:
        if func(i) is True:
          odd_list.append(i)
    return odd_list

a_list = range(1,20)
print(change_list(a_list, is_it_odd))
# is_it_odd doesn't require an argument when it is itself an argument

# function annotation. Define the data types of attributes. Annotate the expected return value
# annotated for clarity, not for functionality. Code will execute regardless of actual data type in args
def random_func(name: str, age: int, weight: float) -> str:
        print("Name :", name)
        print("Age :", age)
        print("Weight :", weight)
        return "{} is {} years old and weighs {}".format(name, age, weight)

print(random_func('Lito',37,192))
print(random_func.__annotations__)