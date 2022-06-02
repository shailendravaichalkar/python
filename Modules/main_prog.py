import utility
import shopping.more_shopping.shopping_cart
# or better way
from utility import multiply, devide
#or
# from utility import *
from shopping.more_shopping.shopping_cart import buy

print(utility.multiply(10, 11))
print(shopping.more_shopping.shopping_cart.buy("apple")) 

if __name__ == '__main__' :
    print(multiply(2,3))
    print(devide(2,3))
    print(buy("orrange"))

print(__name__)

