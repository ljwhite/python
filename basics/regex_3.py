import re

# matches the beginning of string ^
# matches the end of string $

rand_str = "Match everything up to @"
regex = re.compile(r"^.*[^@]")
# first ^ - start at beginning of string
# .* any number of characters
# [^@] anything but the @ symbol
matches = re.findall(regex,rand_str)
print("Matches :",matches)

rand_str = "@ Get this string"
regex = re.compile(r"[^@\s].*$")
# Match anything at the end of the string that isn't @ followed by a space

matches = re.findall(regex,rand_str)
print("Matches :",matches)

rand_str = '''Ape is big
Turtle is slow
Cheetah is fast
'''

# first word of each line after a line break
# (?m) multiline. Signifies that ^ will operate newline boundary
regex = re.compile(r"(?m)^.*?\s")
matches = re.findall(regex, rand_str)
print(matches)

# subexpression
rand_str = "My number is 412-555-1212"
regex = re.compile(r"412-(.*)")
print(re.findall(regex,rand_str))

# problem
rand_str = "412-555-1212 412-555-1213 412-555-12214"
regex = re.compile(r"412-(.{8})")
print(re.findall(regex,rand_str))