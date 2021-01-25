import math

def add_numbers(num_1, num_2):
    return num_1 + num_2

print("5 + 4 =", add_numbers(5,4))

def is_float(str_value):
    try:
        float(str_value)
        return True
    except ValueError:
        return False

pi = "a"
print("Is Pi a Float:", is_float(pi))

def solve_eq(equation):
    x, add, num_1, equal, num_2 = equation.split()
    x = int(num_2) - int(num_1)
    print(x)

print(solve_eq("x + 5 = 9"))


def mult_divide(num1, num2):
    return (num1 * num2), (num1 / num2)

mult, divide = mult_divide(5, 4)

print("5 * 4 =", mult)
print("5 / 4 =", divide)

def is_prime(x):
    x = int(x)
    for i in range(2, x):
        if (x % i) == 0:
            return False
    return True

print(is_prime(7))

def get_primes(x):
    list_primes = []

    for i in range(2,x):
        if is_prime(i):
            list_primes.append(i)
    return list_primes

print(get_primes(12))

# max_number = int(input("Search for primes up to : "))
# print(get_primes(max_number))

def sum_all(*args):
    sum_1 = 0
    for i in args:
        sum_1 += i
    return sum_1

print(sum_all(4,5,6,7,8))

def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("please enter rectangle or circle")

def rectangle_area():
    length = float(input("Enter the length : "))
    width = float(input("Enter the width :"))
    area = length * width
    print("The area of a rectangle is {:.2f}".format(area))

def circle_area():
    diameter = float(input("Enter the diameter : "))
    area = math.pow(diameter,2) * math.pi / 4
    print("The area of a circle is {:.2f}".format(area))

def main():
    shape_type = input("Get area for what shape (rectangle or circle): ")
    get_area(shape_type)

main()

