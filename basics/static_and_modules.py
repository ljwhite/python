# static - utility functions independent of classes

class Sum:
    @staticmethod
    def get_sum(*args):
        sum_1 = 0
        for i in args:
            sum_1 += i
        return sum_1

# def main():
#     print("Sum :", Sum.get_sum(1,2,3,4,5))
#
# main()
# static method --> class method. But can also call on an instance???
# static variable --> class variable

class Dog:
    num_of_dogs = 0
    def __init__(self, name="unknown"):
        self.name = name
        Dog.num_of_dogs += 1

    @staticmethod
    def get_num_of_dogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))

def main():
    spot = Dog("Spot")
    doug = Dog("Doug")
    Dog.get_num_of_dogs()

main()