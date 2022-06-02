from collections import Counter,defaultdict,OrderedDict
import collections

# List Counter
print("LIST Counter")
li = [1,2,3,4,5,6,7,7]
print(Counter(li))

# String Counter
print("String Counter")
sentence = " Hi All I am shailendra and trying to explore Python"

print(Counter(sentence))

# Defaultdict
print("Default Dictionary with default value")

my_dictionary = defaultdict(lambda : 5 , {'a': 1, 'b':2})
print(my_dictionary['c'])

my_dictionary = defaultdict(lambda : "Does Not exist" , {'a': 1, 'b':2})
print(my_dictionary['c'])

# Ordered dictionary
print("ordered dictionary")

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d1 == d2)