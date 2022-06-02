with open("fileIO\Sample.txt") as my_file:
    print(my_file.readlines())

with open("fileIO\\newFile.txt", mode="a") as your_file:
    your_file.write("Hello")

#mode="w" for writing
#mode="a" for appending to a file