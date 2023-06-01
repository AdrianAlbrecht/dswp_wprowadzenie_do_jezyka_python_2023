#Zad 4
from collections import defaultdict


mieszana = [1, 2.3, 'Zbyszek', 5, 'Marian', 3.0]
dictionary = defaultdict(list)
for x in mieszana:
    dictionary[type(x).__name__].append(x)
print(dict(dictionary))