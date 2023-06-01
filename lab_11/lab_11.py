import csv
from datetime import datetime
import re
import pickle

#Zad1
numbers = re.compile(r'\d+')
numbers_w_3_d = re.compile(r'\d{3,}')
ip4s = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
word_w_fg = re.compile(r'[A-Z][a-z]+')
lines_w_4d = re.compile(r'.+\s.+\s.+\s.+\n')
urls = re.compile(r'[https://|http://].+[/]')
def find_regex(filename, regex):
    finds = []
    with open(f'lab_11/{filename}', newline='', encoding="utf8",errors="ignore") as f:
        for line in f:
            finds+= re.findall(regex, line)
    return finds
            
print(find_regex("strings.txt",numbers))
print(find_regex("strings.txt",numbers_w_3_d))
print(find_regex("strings.txt",ip4s))
print(find_regex("strings.txt",word_w_fg))
print(find_regex("strings.txt",lines_w_4d))
print(find_regex("strings.txt",urls))

Zad2
date = re.compile(r'[A-Z][a-z]{2}\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}')
dates = find_regex("auth.log",date)
dates= [datetime.strptime(x,'%b %d %H:%M:%S').replace(year=2023).strftime('%Y-%m-%d %H:%M:%S') for x in dates]                                                    #TODO
ip = re.compile(r'\d\sip-\d{1,3}-\d{1,3}-\d{1,3}-\d{1,3}')
ips = find_regex("auth.log",ip)
ips = [x[5:].replace("-",".") for x in ips]
user = re.compile(r'-\d{1,3}\s\w+-?\w+\[?\d*\]?:\s')
users = find_regex("auth.log",user)
users = [x[5:] for x in users]
pid = re.compile(r'\[\d+\]')
users = [x.split("[")[0].replace(":","") for x in users]
comm = re.compile(r'-\d{1,3}\s\w+-?\w+\[?\d*\]?:\s.+\n')
comms = find_regex("auth.log",comm)
comms = [x[x.find(": ")+2:] for x in comms]
comms = ["\""+x[:-1]+"\"" for x in comms]
with open('lab_11/zad2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile,delimiter=";")
    for x in zip(dates, ips, users, comms):
        writer.writerow(x)
    
#Zad3
class Zad3:
    a: int
    b: int
    
    def __init__(self,x,y):
        self.a = x
        self.b = y
    
    def result(self):
        return self.a*self.b
    
    def __repr__(self) -> str:
        return f'({self.a}, {self.b})'
    
square = Zad3(3,5)
    
with open('lab_11/picled_inst', 'wb') as file:
    pickle.dump(square, file)

with open('lab_11/picled_inst', 'rb') as file:
    square_un = pickle.load(file)
  
print(square_un.result())

#test
with open('lab_11/picled_class', 'wb') as file:
    pickle.dump(Zad3, file)

with open('lab_11/picled_class', 'rb') as file:
    Zad3_un = pickle.load(file)

square2 = Zad3_un(5,5)
print(square2.result())
#działa :)

#Zad4
packed = [Zad3(x,x*3+1) for x in range(1,10)]
with open('lab_11/picled_list', 'wb') as file:
    pickle.dump(packed, file)

with open('lab_11/picled_list', 'rb') as file:
    unpacked = pickle.load(file)
    
print(unpacked)