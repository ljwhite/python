import os

with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Some random text\nMoore random text\nAnd more random text")

with open("mydata.txt", encoding="utf-8") as my_file:
    print(my_file.read())

print(my_file.closed)
print(my_file.name)
print(my_file.mode)
os.rename("mydata.txt","mydata2.txt")
# os.remove("mydata2.txt")
# os.mkdir("mydir")
# os.chdir("mydir")
# print("current directory :", os.getcwd())

# read line
with open("mydata2.txt", encoding="utf-8") as my_file:
    line_num = 1
    while True:
        line = my_file.readline()
        if not line:
            break
        print("Line : ",line_num, " : ",line, end=(""))
        line_num += 1
        print()

def average_length(array):
    accumulator = 0
    for i in array:
        accumulator += len(i)
    average = (accumulator / len(array))
    return average
# problem
with open("mydata2.txt", encoding="utf-8") as my_file:
    line_num = 1
    while True:
        line = my_file.readline()
        if not line:
            break
        list = line.split()
        print("Line",line_num)
        print("Number of words :",len(list))
        print("Avg Word Length :",average_length(list))
        line_num += 1