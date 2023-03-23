from random import random, randint
import math
from typing import Union, Tuple, List


#Zad1
a = [ 1/x for x in range(1,11) ]
b = [ pow(2,x) for x in range(11) ]
c = [ x for x in b if x%4 == 0] 
print(a,b,c,sep='\n')

#Zad2
matrix = [ [random() for y in range(4)] for x in range(4)]
diagonal = [ matrix[i][i] for i in range(4)]
print(matrix, diagonal, sep='\n')

#Zad3
text = 'Ala ma kota.'
generator = ( (x,[ord(y) for y in x]) for x in text.split(" "))
for x in generator:
    print(x)

#Zad4
# -> float | tuple(float, float) nie działa "TypeError: tuple expected at most 1 argument, got 2"
def row_kwadratowe(a: int, b: int , c: int) -> float:
    delta = b**2 - 4 * a * c
    if (delta < 0):
        # brak pierwiastków
        return -1
    elif (delta == 0):
        # jeden pierwiastek
        x = (-b) / (2 * a)
        return x
    else:
        # równanie ma dwa pierwiastki
        x1 = (- b - math.sqrt(delta)) / (2 * a)
        x2 = (- b + math.sqrt(delta)) / (2 * a)
        return x1, x2

print(row_kwadratowe(6,1,3))
print(row_kwadratowe(1,2,1))
print(row_kwadratowe(1,4,1))

#Zad5
def dice_throw(n: int) -> list():
    dice = dict.fromkeys([x for x in range(1,7)],0)
    for x in range(n):
        throw = randint(1,6)
        dice[throw]+=1
    return [(f'oczka: {x}', f'rzutów: {dice[x]}') for x in range(6, 0, -1)]
    
    
try:
    n = int(input('Podaj liczbę całkowitą: '))
    print(dice_throw(n))
except:
    print('Błędny format liczby!!!!!')

#Zad6
def alphabetic(* text: str) -> list():
    if len(text) == 0:
        return list()
    else:
        return sorted([ x for x in text ])
    
print(alphabetic('alfa', 'beta', 'a', 'ba', 'bz'))

#Zad7
def points(** teams: dict()) -> int:
    return sum([teams[x] for x in teams])

print(points(red_bulls = 4, blue_cats = 2, green_panteras = 7))     