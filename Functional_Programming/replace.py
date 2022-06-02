import re

var1 = "Hello"
var2 = "I am Shailendra hello HeLLo HELLO is my greet"
var3 = "bye"

pattern = re.compile(var1, re.IGNORECASE)
print(pattern.sub(var3, var2))

# O/P : I am Shailendra bye bye bye is my greet