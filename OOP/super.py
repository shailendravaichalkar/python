class User: 
    def sign_in(self):
        print("logged in")
    
    def attack(self):
        print("Do Nothing")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f' Hello I am {self.name} and I can attack with {self.power} power' )

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f' Hello I am {self.name} and I have {self.arrows} arrows left' )

wizard1 = Wizard("SHA", 100)
archer1 = Archer("Rhea", 50)
print(dir(wizard1))
print("Dunder Method")
print(wizard1.__dir__)