from random import randint
import this
import os

os.system('cls')

#Zad1
try:
    number = int(input('Wpisz dowolną liczbę całkowitą: '))

    print(f'Liczba całkowita: {str(number)}\nLiczba w preprezentacji binarnej: {str(bin(number))}')
    print(f'Liczba w preprezentacji ósemkowej: {str(oct(number))}\nLiczba w preprezentacji szesnastkowej: {str(hex(number))}\n')
except:
    print('Błędny format liczby!')

#Zad2
i = input('Napisz cokolwiek :)\n')
try:
    int(i)
    print(f'Zmienna jest rzutowalna na typ całkowity.')
except:
    print(f'Zmienna NIE jest rzutowalna na typ całkowity.')

try:
    float(i)
    print(f'Zmienna jest rzutowalna na typ zmiennoprzecinkowy.')
except:
    print(f'Zmienna NIE jest rzutowalna na typ zmiennoprzecinkowy.')

#Zad3
import sys

print('Wpisz dowolną liczbę całkowitą: ', end="")
try:
    number = int(sys.stdin.readline())
    multiplier = pow(10,(len(str(number))-1))
    ratio = f"Podaną liczbę można zapisać jako: "
    print(number, multiplier)
    while number > 0:
        temp = int(number//multiplier)
        ratio+=f'{multiplier} * {temp}'
        if(multiplier > 1):
            ratio+=f' + '
        number = number - (temp*multiplier)
        multiplier= int(multiplier/10)
    sys.stdout.write(ratio)
except:
    print('Błędny format liczby!')

#Zad4

some_text = input('Wpisz dowolny tekst: ')
encode_text = ""
for x in some_text:
    try:
        encode_text += this.d[x]
    except:
        encode_text += x
print(encode_text)

#Zad5
some_text = input('Wpisz dowolne zdanie: ')
split_text = some_text.split(" ")
print(sorted(split_text, key=len))

#Zad6
universal = []
universal.append(['Koleżanki i koledzy ','Z drugiej strony ','Podobnie ', 'Nie zapominajmy jednak, że ', 'W ten oto sposób ', 'Praktyka dnia codziennego dowodzi, że ', 'Wagi i znaczenia tych problemów nie trzeba szerzej uzasadniać, ponieważ ', 'Różnorakie i bogate doświadczenia ', 'Troska organizacji, a szczególnie ', 'Wyższe założenia ideowe, a także '])
universal.append(['realizacja nakreślonych zadań programowych ', 'zakres i miejsce szkolenia kadr ', 'stały wzrost ilości i zakres naszej aktywności ', 'aktualna struktura organizacji ', 'nowy model działalności organizacyjnej ', 'dalszy rozwój różnych form działalności ', 'stałe zabezpieczenie informacyjno programowe naszej działalności ', 'wzmacnianie i rozwijanie struktur ', 'konsultacja z szerokim aktywem ', 'rozpoczęcie powszechnej akcji kształtowania postaw '])
universal.append(['zmusza nas do przeanalizowania ', 'spełnia istotną rolę w kształtowaniu ', 'wymaga sprecyzowania i określenia ', 'pomaga w przygotowaniu i realizacji ', 'zabezpiecza udział szerokiej grupie w kształtowaniu ', 'spełnia ważne zadania w wypracowaniu ', 'umożliwia w większym stopniu tworzenie ', 'powoduje docenianie wagi ', 'przedstawia intersującą próbę sprawdzenia ', 'pociąga za sobą proces wdrażania i unowocześniania '])
universal.append(['istniejących warunków administracyjno- finansowych. ', 'dalszych kierunków rozwoju. ', 'systemu powszechnego uczestnictwa. ', 'postaw uczestników wobec zadań stawianych przez organizację. ', 'nowych propozycji. ', 'kierunków postępowego wychowania. ', 'systemu szkolenia kadry odpowiadającego potrzebom. ', 'odpowiednich waruknków aktywizacji. ', 'modelu rozwoju. ', 'form oddziaływania. '])
try:
    number = int(input('Podaj liczbę zdań do wygenerowania: '))
    text = ""
    for i in range(number):
        for x in range(4):
            random = randint(0, 9)
            text += universal[x][random]
    print(text)
except:
    print('Błędny format liczby!')