import csv
import datetime
from typing import Any, Callable


# #Zad 1
# def extract_numbers(vals: list[Any]) -> list[int | float]:
#     return list(filter(lambda x: isinstance(x,(int,float)) , vals))


# print(extract_numbers(["andrzej", 1, 1.34,-3,4,"Mateusz",6.43,7.9]))

# #Zad 2
# print(sorted(input("Podaj listę słów oddzielnoych spacją:\n").split(" "), key = lambda x: len(x), reverse = True))

# #Zad 3
# def double_list_sort(vals: list[int | str], reversed: bool = False) -> list[int | str]:
#     return sorted(filter(lambda x: isinstance(x,str) , vals)) + sorted(filter(lambda x: isinstance(x,int) , vals)) \
#             if reversed else sorted(filter(lambda x: isinstance(x,int) , vals)) + sorted(filter(lambda x: isinstance(x,str) , vals))


# print(double_list_sort(["andrzej", 1,-3,4,"Mateusz"], True))
# print(double_list_sort(["andrzej", 1,-3,4,"Mateusz"], False))

# #Zad 4
# nation = []
# sorted_nation = dict()
# kolumny = []

# def add_to_dict(dictionary : dict , new_value: list[Any]) -> None:
#     if new_value[0] in dictionary.keys():
#         dictionary[new_value[0]].append(new_value)
#     else:
#         dictionary[new_value[0]] = [new_value]
#     return dictionary

# with open('lab_06/zamowienia.csv', newline='', encoding="utf8",errors="ignore") as f:
#     reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
#     kolumny = next(reader, None)
#     for wiersz in reader:
#         nation.append(wiersz)
# nation = list(map(lambda wiersz: wiersz[:2] + [datetime.datetime(int(wiersz[2].split(".")[2]), int(wiersz[2].split(".")[1]),\
#                                                                 int(wiersz[2].split(".")[0])).strftime("%Y-%m-%d")] \
#                                                 + [wiersz[3]]+[wiersz[4][:-2].replace(",",".").replace(" ","")],nation))
# sorted_nation = list(map(lambda x: add_to_dict(sorted_nation,x),nation))[0]
          
# with open('lab_07/zamowienia_polska.csv', 'w', newline='') as csvfile:
#     with open('lab_07/zamowienia_niemcy.csv', 'w', newline='') as csvfile2:
#         writer = csv.writer(csvfile,delimiter=";")
#         writer2 = csv.writer(csvfile2,delimiter=";")
#         writer.writerow(kolumny)
#         writer2.writerow(kolumny)
#         list(map(lambda x: writer.writerow(x),sorted_nation['Polska']))
#         list(map(lambda x: writer2.writerow(x),sorted_nation['Niemcy']))
    
#Zad 5
def sort_dict(dictionary: dict, arg: Callable) -> dict:
    return dict(sorted(dictionary.items(), key = lambda x: arg(list(x)[1:][0])))


ex = {'Jan': [1, 4, 7 , 9, 12, 20, 80], 'Andrzej': [2,3,4,5,6,7,8,9], 'Ewa': [99]}
print(sort_dict(ex, min))
print(sort_dict(ex, max))
print(sort_dict(ex, sum))
#print(sort_dict(ex, abs)) #not working with abs and don't know how it was supossed to work