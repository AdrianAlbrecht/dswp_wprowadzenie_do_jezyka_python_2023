import json
import random

# lista
lista = [[random.randint(1, 100) for n in range(10)] for k in range(10)]

with open('test/dane_lista.json', 'w') as plik:
    json.dump(lista, plik)

with open('test/dane_lista.json', 'r') as plik:
    x = json.load(plik)

print(x)
print(type(x))

# słownik
slownik = {f'student_{x}': x**2 for x in range(1,11)}

with open('test/dane_slownik.json', 'w') as plik:
    json.dump(slownik, plik)

with open('test/dane_slownik.json', 'r') as plik:
    x = json.load(plik)

print(x)
print(type(x))

# typy inne niż list i dict nie działają out of the box
# ale można poszukać metod, które pozwalają zapisać inne struktury w
# postaci list lub słowników

class Pracownik:
    pass

p = Pracownik()
p.imie = 'Adam'
p.nazwisko = 'Malinowski'

# print(json.dumps(p)) # nie

# tak !
print(json.dumps(p.__dict__))