# function 3!

def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num-1)
        return result

print(factorial(5))

def factorial_iter(num):
    for i in range(1,num+1):
        if i <= 1:
            result = 1
        else:
            result = result * i
    return result

print(factorial_iter(5))

# problem
# fibonacci numbers
# sum previous two values to get the next
# (5) ==> 1,1,2,3,5
def fib(n):
    if n <= 1:
        return n
    else:
        result = fib(n-1) + fib(n-2)
        return result

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
# [0,1,1,2,3,5,8,13,21]
# num_fib_values = int(input("how many fib values should be found : "))
# i = 0
# while i < num_fib_values:
#     fib_value = fib(i)
#     print(fib_value)
#     i += 1
