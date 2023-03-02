from datetime import datetime


#1 Cięcie stringa z określoną długością
print(f'{"Xylophone":10.5}!')
#2 Formatowanie floata
print(f'{3.141592653589793:f}')
#3 Dystans pomiędzy znakiem aliczbą dziesiętną
print(f'{23:=+7d}')
#4 Datetime
print(f'{datetime.now():%Y-%m-%d %H:%M}')
#5 Wyrównanie i długość stringa
print(f'{"tekst":{"^"}{20}}')