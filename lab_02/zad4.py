from datetime import datetime


#1 Cięcie stringa
print(f'{"Xylophone":.5}')
#2 Formatowanie floata
print(f'{3.141592653589793:f}')
#3 Dystans pomiędzy znakiem aliczbą dziesiętną
print(f'{23:=+7d}')
#4 Datetime
print(f'{datetime(2001, 2, 3, 4, 5):%Y-%m-%d %H:%M}')
#5 Wyrównanie i długość stringa
print(f'{"tekst":{"^"}{20}}')