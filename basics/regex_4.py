import re
#back reference

rand_str = "The cat cat fell out the window"
regex = re.compile(r"(\b\w+)\s+\1")
matches = re.findall(regex,rand_str)
print(matches)

# back reference substitutions
rand_str = "<a href='#><b>The Link</b></a>"
regex = re.compile(r"<b>(.*?)</b>")
rand_str = re.sub(regex, r"\1", rand_str)
print(rand_str)

# look ahead
# (?=expressions)

rand_str = "one two three four"
regex = re.compile(r"\w+(?=\b)")
# returns the word that is followed by a word boundary
print(re.findall(regex, rand_str))

# look behind
# (?<=expression)
rand_str = "1. bread 2. apples 3. lettuce"
regex = re.compile(r"(?<=\d.\s)\w+")
# returns the word that follows the digit, the dot, and the space
print(re.findall(regex,rand_str))

# combine look ahead and look behind
rand_str = "<h1>I'm Important</h1> <h1>So am I</h1>"
regex = re.compile(r"(?<=<h1>)\w+")
regex2 = re.compile(r"\w+(?=</h1>)")
combined = re.compile(r"(?<=<h1>).+?(?=</h1>)")
print(re.findall(combined, rand_str))
