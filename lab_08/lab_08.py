from array import array
import csv
from datetime import datetime
import random
from timeit import timeit
from collections import deque, namedtuple, Counter
import time

# #Zad 1
# # In Python 3.x, use int instead of long.
# setup = """
# from array import array
# import random
# """
# stmt1 = """
# tab_of_ints = array('I', [random.randint(0,255) for _ in range(1_000_000)])
# """
# stmt2 = """
# list_of_ints = [random.randint(0,255) for _ in range(1_000_000)]
# """

# print(timeit(stmt1, setup, number=100))
# print(timeit(stmt2, setup, number=100))

# stmt3 = """
# tab_of_ints = array('B', [random.randint(0,255) for _ in range(1_000_000)])
# """
# stmt4 = """
# list_of_ints = [random.randint(0,255) for _ in range(1_000_000)]
# """

# print(timeit(stmt3, setup, number=100))
# print(timeit(stmt4, setup, number=100))

# #Zad 2
# print("=======Array=======")
# print("=======Write=======")
# start = datetime.now()
# tab_of_floats = array('f', [random.random() for _ in range(1_000_000)])
# with open('lab_08/floats_array.bin', 'wb') as file_arr:
#     tab_of_floats.tofile(file_arr)
# end = datetime.now()
# print(end-start)
# print("=======Read=======")
# start = datetime.now()
# list_of_floats = [random.random() for _ in range(1_000_000)]
# with open('lab_08/floats_list.txt', 'w') as file_arr:
#     file_arr.writelines('\n'.join([str(x) for x in list_of_floats]))
# end = datetime.now()
# print(end-start)
# print("=======List=======")
# print("=======Write=======")
# start = datetime.now()
# tab_of_floats_loaded = array('f')
# file_arr  = open('lab_08/floats_array.bin', 'rb')
# tab_of_floats_loaded.fromfile(file_arr, 1_000_000)
# file_arr.close()
# end = datetime.now()
# print(end-start)
# print("=======Read=======")
# start = datetime.now()
# with open('lab_08/floats_list.txt', 'r') as file_list:
#     list_of_floats_loaded = file_list.readlines()
# list_of_floats_loaded = [float(x.strip()) for x in list_of_floats_loaded]
# end = datetime.now()
# print(end-start)
# print("==================")

# #Zad 3
# setup = """
# from collections import deque
# kolejka = deque('Ala ma kota'.split())
# """
# stmt1="""
# for x in range(100_000):
#     kolejka.append('?')
# """
# stmt2="""
# for x in range(100_000):
#     kolejka.appendleft('Czy')
# """
# print(timeit(stmt1, setup, number=1))
# print(timeit(stmt2, setup, number=1))

# setup = """
# lista = 'Ala ma kota'.split()
# """
# stmt1="""
# for x in range(100_000):
#     lista.append('?')
# """
# stmt2="""
# for x in range(100_000):
#     lista.insert(0,'Czy')
# """
# print(timeit(stmt1, setup, number=1))
# print(timeit(stmt2, setup, number=1))

# #Zad 4
# with open('lab_06/zamowienia.csv', newline='', encoding="utf8",errors="ignore") as f:
#     reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
#     Line = namedtuple('Line', [x.replace(" ","_") for x in next(reader, None)])
#     list_of_lines = list()
#     for _ in range(15):
#         list_of_lines.append(Line._make(next(reader, None)))
#     for x in list_of_lines:
#         print(x)

# #Zad 5
# tab_of_ints = sorted(array('I', [random.randint(0,1000000) for _ in range(1000)]))
# print(tab_of_ints[len(tab_of_ints):len(tab_of_ints)-int(len(tab_of_ints)/10)-1:-1])

# #Zad 6
def create_kolo_fortuny(*args) -> deque:
    return deque(Counter(args).elements())


# print(create_kolo_fortuny(4,5,6,7,4,6,2,7,4,5,6,6,5,3,5,5,3,4,5,1))

#Zad 7
def spinit(fortune: deque, wygrana: int):
    fortune.rotate(random.randint(0, len(fortune)))

    print(f"Aktualny stan koła: {fortune}")
    if fortune[0] != wygrana:
        time.sleep(1)
        spinit(fortune, wygrana)
       
fortune = create_kolo_fortuny(9,2,3,4,5,6,7,8,1)
wygrana = fortune[0] #albo random.choice(fortune)

fortune.rotate(1)
spinit(fortune, wygrana)
print("Wygrałeś")
    