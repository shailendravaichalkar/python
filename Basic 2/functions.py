def showHello():
    print("Hello")

showHello()

def sayHello(name, emoji):
    print(f'Hello {name} {emoji}')

#Positional Arguments
sayHello('Sha', ':)')
sayHello('Rhea', ':P')

#keyword Arguments
sayHello(emoji=":)", name='SMART')

#Default Arguments
def greet(name="Shailendra", emoji=":-)"):
    print(f'Hello {name} {emoji} from Greet')

greet()
greet(name="Rhea")
greet(emoji=";-)")    
greet("SMART")