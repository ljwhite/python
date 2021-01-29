# iterables
# iterables - list. Object with an __iter__ method that returns an iterator
# Iterator - object with a __next__ method that retrieves the next value
# generators - produces one object at a time

samp_str = iter("Sample")

print("Char :", next(samp_str))
print("Char :", next(samp_str)) #same method, next character

class Alphabet:
    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.letters):
            raise StopIteration
        self.index += 1
        return self.letters[self.index - 1]

alpha = Alphabet()
for letter in alpha:
    print(letter)
#
# str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for i in str:
#     print(i)

derek = {'f_name': 'derek', 'l_name': "banas"}

for key in derek:
    print(key, derek[key])

# problem
# fibonacci sequence - print next num when next is called

class Fib_Generator:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib_num = self.first + self.second
        self.first = self.second
        self.second = fib_num
        return fib_num

fib_seq = Fib_Generator()

for i in range(10):
    print("Fib :", next(fib_seq))

class Fib_Gen2:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib_number = self.first + self.second
        self.first = self.second
        self.second = fib_number
        return fib_number

fib_object = Fib_Gen2() #constructor method for FibGen object

for i in range(10):
    print("Fib number :", next(fib_object))
