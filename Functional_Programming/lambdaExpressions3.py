line = "Hi all I am Shailendra AND willing to work on Python"
opCode = ["AND", "OR", "WHEN"]

print(list(map(lambda item: item in line, opCode)))

# [True, False, False]