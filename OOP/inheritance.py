class User:                   # This is same as class User(object)
    def sign_in(self):
        print("logged in")

class Wizard(User):
    pass

class Archer(User):
    pass

wizard1 = Wizard()
wizard1.sign_in()

print(isinstance(wizard1,Wizard))
print(isinstance(wizard1,Archer))
print(isinstance(wizard1,User))
print(isinstance(wizard1,object))  # Inherits the properties from 'object' base class that python comes with