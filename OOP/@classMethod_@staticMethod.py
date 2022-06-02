class  PlayerCharecter:
    membership = True  # Class object attribute

    def __init__(self, name, age):  #class object Method    
        if(self.membership): 
            if (PlayerCharecter.membership): # PlayerCharecter is same as self
                self.name = name
                self.age = age

    @classmethod
    def addinngNumbers (cls, num1, num2):
        return num1 + num2
    
    @classmethod                       # Object created using class Moethod
    def add_num (cls, num1, num2):
        return cls("RHEA", num1 + num2)

    
    @staticmethod                     # Same as class Method but dont have access to cls or class 
    def sumNum (num1, num2):
        return num1 + num2


print(PlayerCharecter.addinngNumbers(3,4)) # No need to create object to call Class Method
player3 = PlayerCharecter.add_num(10,4)
print(player3.age)

print(PlayerCharecter.sumNum(9,4))
