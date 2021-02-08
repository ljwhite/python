import re

rand_str = "F.B.I I.R.S CIA"
print("Matches :",len(re.findall(".\..\..", rand_str)))

rand_str = """This is a long
string that goes
on for many lines"""
print(rand_str)

regex = re.compile("\n")
str_search = regex.search(rand_str)
print(str_search)
one_line = regex.sub(" ", rand_str)
print(one_line)

nums = "12345"
print("Matches :", len(re.findall("\d",nums)))
if re.search("\d{5}", nums):
    print("it is a zip code")

# \d [0-9] digit
# \w [a-zA-z0-9] anything alphanumeric
# \W Anything that isn't a letter or number
# {} add quantity \w{3} three consecutive alphanumeric characters
phone = "333-333-3333"
if re.search("\w{3}-\w{3}-\w{4}",phone):
    print('{} is a phone number'.format(phone))

if re.search("\w{2,10}", "sarah white"):
    print("It is a valid name")
print(re.findall("\w{2,20}", "sarah white"))

# match for white space
# \s [\f\n\r\t\v]

if re.search("\w{2,20}\s\w{2,20}", "sarah white"):
    print("{} is a valid first and last name".format("sarah white"))

print("Matches :",len(re.findall("a+", "a as apa bua")))

# problem
# valid email address
# Part 1: 1-20 alphanumeric symbols, plus, ._%+-
# Part 2: @
# Part 3, 2-20 alphanumeric symbols, plus .-
# Part 4 2-3 lower/upper case letters

crit = "[\w._%+-]{1,20}@[\w.-]{2,20}.[a-zA-Z]{2,3}"

criteria = "[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}"
emai_list = "@gmail.com db@aol.com m@.com @apple.com db@.com lito@gmail.com"

print("Correct Email Matches :", re.findall(criteria, emai_list))

rand_str = "doctor doctors doctor's"
regex = re.compile("[doctor]+['s]{0,2}")
matches = re.findall(regex, rand_str)
print("doctor matches :", len(matches))

criteria = "[doctor]+['s]{0,2}"
matches2 = re.findall(criteria,rand_str)
print("doctor matches :",matches2)

# Problem
# \r\n
long_str = '''Just some words
and some more\r
and more
'''

criteria = re.compile("[\r\n]{1,2}")
one_line = criteria.sub(" ", long_str)
print(one_line)

criteria2 = "[\w\s]+[\r\n]{1,2}"

matches = re.findall(criteria2,long_str)
print(matches)

for i in matches:
    print(i)

# word matching
rand_str = 'ape at the apex'
regex = re.compile(r"ape")
regex_2 = re.compile(r"\bape\b")
print(re.findall(regex,rand_str))
print(re.findall(regex_2,rand_str))

# word matching
# "\bword\b"