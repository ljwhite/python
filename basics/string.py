print(type(3))
print(type("3"))

samp = "This is a very important string"
print("length: ", len(samp))

print(samp[0])
print(samp[-1])
print(samp[0:4])
print(samp[8:])
print("Every other character: ", samp[0:-1:2])
print("Reverse: ", samp[::-1])
print("Green" + "Eggs")
print("hello " * 5)

num = str(4)
print(num)

for char in samp:
    print(char)

for i in range(0, len(samp)-1,2):
    print(samp[i] + samp[i+1])

print("A =", ord("A"))
print("space =", ord(" "))
print("65 =", chr(65))

str_1 = "a"
str_2 = "b"
print(ord(str_1))
print(ord(str_2))
print(ord(str_1) + ord(str_2))
print(chr(ord(str_1) + ord(str_2)))

# Problem: Receive uppercase string. Hide in unicode, then translate back.
input_str = "CaT"
secret = ""
for char in input_str:
    secret += str(ord(char) - 23)
print(secret)

message = ""
for i in range(0, len(secret)-1,2):
    num_str = secret[i]+ secret[i+1]
    message += chr(int(num_str) + 23)
print(message)

# problem