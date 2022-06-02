my_file = open("FileIO\Sample.txt")

print(my_file.read())
my_file.seek(100) # Seek index
print("-------Trying Seek Function-----------")
print(my_file.read())
my_file.seek(0) 
print(my_file.readlines())
my_file.close()

