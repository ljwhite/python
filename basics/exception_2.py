import os

# finally / else
# handle errors or expected events
# execute code when something happens (close a file previously opened)
# exceptions can be triggered 1) with an error 2) when you want them to
# execute different code when we reach an error
# try: <code> ... except <error_type>: <code>

# try:
#     a_list = [1,2,3]
#     print(a_list[3])
#
# except IndexError:
#     print("Sorry - that index doesn't exist")
# except:
#     print("an unknown error occurred")
#
# class DogNameError(Exception):
#     def __init__(self, *args, **kwargs):
#         Exception.__init__(self, *args, **kwargs)
#
# try:
#     dog_name = input("What is your dogs name : ")
#     if any(char.isdigit() for char in dog_name):
#         raise DogNameError
# except DogNameError:
#     print("your dogs name can't contain a number")
#

# problem

# with open("mydata3.txt", mode="w", encoding="utf-8") as my_file:
#     my_file.write("Some random text\nAnd some more text\nAnd finally a bit more")



try:
    my_file = open("mydata2.txt", encoding="utf-8")
    # with open("mydata3.txt", mode="w", encoding="utf-8") as my_file:
    #     print(my_file.read())
except FileNotFoundError as ex:
    print("file does not exist")
    print(ex.args)
else:
    print("File:\n",my_file.read())
    my_file.close()
finally:
    print("Finished Working with File")
