def fact(x):
    if (x == 0):
        return 1
    return(x * fact(x-1))

def fact_1(x):
    fact_value = 1;
    for i in range(fact_value,x+1):
        fact_value = i * fact_value
    print(f"fact({x}) = {fact_value}")
        


input_num=0
input_num = int(input("Give Number to calculate Factorial :"))

print("Method 1 ")
print (fact(input_num))

print("Method 2 ")
fact_1(input_num)


