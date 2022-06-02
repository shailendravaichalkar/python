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
    def __init__(self,name,arrows):
        self.name = name
        self.arrows = arrows
    
    def check_arrows(self):
        print(f"I am {self.name} and I have {self.arrows} arrows left")    

    def run(self):
        print("I can run fast")

class Fighter(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self,name, arrows)

f1 = Fighter("SMART", 100, 50)  
f1.run()
f1.attack()
f1.check_arrows()