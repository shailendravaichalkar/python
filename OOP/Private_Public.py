# There is NO provision is python to make variable private
class  PlayerCharecter():
    def __init__(self, name, age):  #class object Method    
        self._name = name   # This undersocre _name just to tell programmer this is private variable
        self._age = age
    def speak(self):
        print(f'My name is {self._name} and I am {self._age} years old')


player1 = PlayerCharecter("Sha", 35)
player1.speak()

print(player1._age)
