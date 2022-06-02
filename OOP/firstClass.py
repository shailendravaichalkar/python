class  PlayerCharecter:
    membership = True  # Class object attribute

    def __init__(self, name, age):  #class object Method    
        if(self.membership): 
            if (PlayerCharecter.membership): # PlayerCharecter is same as self
                self.name = name
                self.age = age

    def run(self):
        print("Run")

    def shout(self): 
        print(f"My name is {self.name}")


player1 = PlayerCharecter('Chuk',30)

player1.attack = 100

print(player1.name)
print(player1.age)
print(player1.attack)
player1.shout()

player1.run()