rand_string = "      this is an important string     "

rand_string1 = rand_string.lstrip()
rand_string2 = rand_string.rstrip()
rand_string3 = rand_string.strip()

print(rand_string)
print(rand_string1)
print(rand_string2)
print(rand_string3)

print(rand_string.upper())

list = ["Bunch", "of", "random", "words"]
print(type(list))
print(list)
print(" ".join(list))

list_2 = rand_string.split()
print(list_2)

for i in list_2:
    print(i)

print("how many is:",rand_string.count("is"))
print("where is:",rand_string3.find("string"))
print("replace is:",rand_string1.replace(" an", " a type of"))

# problem
# create acronym generator
# take first letter and create an acronym out of it ("Random Access Memory" --> "RAM")
str = "Random access Memory"

list = str.split()
acronym = ""
for i in list:
    acronym += i[0].upper()
    print(i[0].upper(), end="")
print("", end='\n')
print(acronym)

letter_z = "z"
print("is z alphanumeric :", letter_z.isalnum())
print("is z a letter :", letter_z.isalpha())
print("is z a digit :", letter_z.isdigit())
print("is z a number :", letter_z.isnumeric())
print("is z a lowercase :", letter_z.islower())
print("is z a uppercase :", letter_z.isupper())

# problem
# caesar cipher - move message by characters x amount to the right
# a - z 97-122
# A - Z 65-90

message = "StR iNg"
key = 17
secret_list = []
for char in message:
    if char.islower():
        char_ord = ord(char)
        secret_ord = char_ord + (key % 26)
        if secret_ord > 122:
            new_ord = secret_ord - 26
            secret_list.append(new_ord)
        else:
            secret_list.append(secret_ord)
    elif char.isupper():
        char_ord = ord(char)
        secret_ord = char_ord + (key % 26)
        if secret_ord > 90:
            new_ord = secret_ord - 26
            secret_list.append(new_ord)
        else:
            secret_list.append(secret_ord)
    else:
        char_ord = ord(char)
        secret_list.append(char_ord)

secret_message = ""
for i in secret_list:
    secret_message += chr(i)
print(secret_message)

str1 = "  This is a very important string  "
str1 = str1.strip()
print("Uppercase :", str1.upper())
print("Lowercase :", str1.lower())
str_list = str1.split()
print("Words")
for i in str_list:
    print(i)

print("How many ts?",str1.count("t"))