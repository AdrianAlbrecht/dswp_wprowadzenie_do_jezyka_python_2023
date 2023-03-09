#Zad 1
print("=========================Zad 1=========================")
list_1 = [ x for x in range(1,11)]
print(list_1)
list_1_1 = list_1[:5]
list_1_2 = list_1[5:]
print(list_1_1,list_1_2, sep=", ")

#Zad 2
print("=========================Zad 2=========================")
list_2 = [0]+ list_1_1 + list_1_2
print(list_2)
list_3 = list_2.copy()
list_3.sort(reverse=True)
print(list_2, list_3, sep="\n")

#Zad 3
print("=========================Zad 3=========================")
import numpy as np

text = input("Input here some text:\n").lower()
letters = np.array([*text])
letters = list(np.unique(letters)) 
letters.sort()
print(letters)

# lub bez numpy
letters = np.array([*text])
unique = list()
for x in letters:
    if x not in unique:
        unique.append(x)
unique.sort()
#print(unique)

#Zad 4
print("=========================Zad 4=========================")
import babel.dates

months = dict(babel.dates.get_month_names(context='stand-alone'))
print(months)

# można też ręcznie xD (ale po co?)

months = dict()
polish = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]
for x in range(1,13):
    months[x]=polish[x-1]
#print(months)

#Zad 5
print("=========================Zad 5=========================")
months_pl = months.copy()
print(months_pl)
months_en = dict(babel.dates.get_month_names(context='stand-alone', locale="en_US"))
print(months_en)

months = dict()
months['pl'] = months_pl
months['en'] = months_en

print(months['pl'][4], months['en'][4])

#Zad 6
print("=========================Zad 6=========================")
name = 'Marianna'
name_dict = dict.fromkeys(name, 1)
print(name_dict)

#Zad 7
print("=========================Zad 7=========================")
import string 


text = input("Input here some text without special characters but with digits:\n").lower()
unique = list()
for x in text:
    try:
        x = int(x)
    except:
        None
    if x not in unique:
        unique.append(x)
letters = [x for x in unique if type(x) == str if x in [*string.ascii_lowercase]]
digits = [x for x in unique if type(x) == int]

print(f'This text has {len(letters)} unique characters and it\'s {len(letters)/len(string.ascii_lowercase)*100:.2f}% of all characters')
print(f'This text has {len(digits)} unique digits and it\'s {len(digits)/len(string.digits)*100:.2f}% of all digits')