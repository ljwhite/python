import re

if re.search("ape", "The ape was at the apex"):
    print("there is an ape")

all_apes = re.findall("ape", "the ape was at the apex")
for i in all_apes:
    print(i)

the_str = "The ape was at the apex"
for i in re.finditer("ape.", the_str):
    loc_tuple = i.span()
    # span generates a tuple with starting and ending index position
    print(loc_tuple)
    print(the_str[loc_tuple[0]:loc_tuple[1]])

print("--------")
all_ape = re.search("ape.", the_str)
all_ape.span()
print("--------")

animal_str = "Cat rat mat fat pat"
all_animals = re.findall("[c-mC-M]at",animal_str)
for i in all_animals:
    print(i)

owl_food = "rat cat mat pat"
regex = re.compile("[cr]at")
owl_food = regex.sub("owl", owl_food)
print(owl_food)

rand_str = "Here is \\stuff"
print("Find \\stuff :", re.search(r"\\stuff",rand_str))

