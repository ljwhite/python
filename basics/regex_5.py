import re

rand_str = "1. Dog 2. Cat 3. Turtle"
regex = re.compile(r"\d\.\s(Dog|Cat)")
print(re.findall(regex,rand_str))

rand_str = "1. Dog 2. Cat 3. Turtle"
regex = re.compile(r"\d\.\s(Dog|Cat)")
print(re.findall(regex,rand_str))

# problem
# match for 5 digits 55555, or 5 digits - 4 digits 55555-4444

rand_str ="12345 12345-1234 1234 123456-333"
regex = re.compile(r"(\d{5}-\d{4}|\d{5}\s)")
print(re.findall(regex, rand_str))

# group
# regex return subexpressions regex_results.group() arg is for which group number
# bd = input("Enter your birthday (mm-dd-yyyy): ")
# bd_regex = re.search(r"(\d{1,2})-(\d{1,2})-(\d{4})", bd)
# print("you were born on : ",bd_regex.group())
# print("Month: ",bd_regex.group(1))
# print("Day: ",bd_regex.group(2))
# print("Year: ",bd_regex.group(3))

# match
match = re.search(r"\d{2}", "the chicken weighed 13 lbs")
print("Match :",match.group())
print("Span :",match.span())
print("Match :",match.start())
print("Match :",match.end())

# assign name to matches
rand_str = "December 21 1974"
regex = r"^(?P<month>\w+)\s(?P<day>\d+)\s(?P<year>\d+)"
matches = re.search(regex, rand_str)
print("month :", matches.group('month'))
print("day :", matches.group('day'))
print("year :", matches.group('year'))

# problem
# email address, match for each one

rand_str = 'd+b@aol.com a_1@yahoo.co.uk A-100@mm-b.INTERNATIONAL'
regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
print(re.findall(regex,rand_str))

# problem
#  match all telephone numbers
rand_str = "14125551212 4125551212 (412)5551212 412 555 1212 412-555-1212 1-412-555-1212"
# regex = re.compile(r"((1?)(-| ?)(\()?(\d{3})(\)|-| |\))?(\d{3})(-| )?(\d{4}|\d{4}))")
regex = re.compile(r"((1?)(-| ?)(\()?(\d{3})(\)|-| |\))?(\d{3})(-| )?(\d{4}|\d{4})")
matches = re.findall(regex, randStr)

print(len(matches))

for i in matches:
    print(i[0].lstrip())