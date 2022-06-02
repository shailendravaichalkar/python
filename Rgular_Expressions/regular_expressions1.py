import re
from typing import Pattern

string = " This is string to practice reg ex in python. And this is pattern, This is"

a = re.search("is", string)
print(a.span())

pattern = re.compile("This")

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.match(string)
d = pattern.fullmatch(string)

print(a)
print(b)
print(c)
print(d)