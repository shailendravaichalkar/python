class User:                   # This is same as class User(object)
    def sign_in(self):
        print("logged in")

class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f"I am {self.name} and I have {self.power} power")

class Archer(User):
    def __init__(self,name,archer):
        self.name = name
        self.archer = archer
    
    def check_arrows(self):
        print(f"I am {self.name} and I have {self.archer} arrows left")    

    def run(self):
        print("I can run fast")

class Fighter(Wizard, Archer):
    pass

f1 = Fighter("SMART", 100)  #We arw not passing archer here
f1.run()
f1.attack()
# f1.check_arrows()  This will not work