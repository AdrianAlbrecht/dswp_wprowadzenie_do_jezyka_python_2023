import csv
from datetime import datetime
from zoneinfo import ZoneInfo
from dateutil import relativedelta
import os
import string

#Zad 1
def check_paths(paths: list) -> None:
    for path in paths:
        if os.path.exists(path):
            print(f'Folder {path} istnieje')
        else:
            print(f'Folder {path} nie istnieje. Trwa tworzenie...')
            path_parts = path.split('/')
            walk = path_parts.pop(0)
            for part in path_parts:
                walk+="/"+part
                if os.path.exists(walk)==False:
                    try:
                        os.mkdir(walk)
                        print(f'Utworzono folder: {walk}')
                    except OSError as e:
                        print(e)
            
check_paths(["lab_10","lab_10/test/test_in_test","C:/tmp/tmp2/tmp3"])

#Zad2
def join_files_from(path: string) -> None:
    with open('lab_10/zad2.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile,delimiter=";")
        kolumny = ""
        for root, _, files in os.walk(path):
            # print(root)
            # print('    ', files)
            for file in files:
                with open(root+"/"+file , 'r') as f:
                    if kolumny == "":
                        kolumny = f.readline().removesuffix("\n").split(",")
                        writer.writerow(kolumny)
                    else:
                        f.readline()
                    for line in f:
                        writer.writerow(line.removesuffix("\n").split(","))
                        
        
join_files_from("lab_10/data_for_lab_10")

#Zad3
def time_zones_check(time: string) -> None:
    time_parts = time.split(":")
    dt = datetime.now(ZoneInfo('Europe/Warsaw')).replace(hour=int(time_parts[0]), minute=int(time_parts[1]), second=int(time_parts[2]), microsecond=0)
    print(f"Tokyo: {dt.astimezone(tz=ZoneInfo('Asia/Tokyo')).strftime('%H:%M:%S')}")
    print(f"Londyn: {dt.astimezone(tz=ZoneInfo('Europe/London')).strftime('%H:%M:%S')}")
    print(f"Sydney: {dt.astimezone(tz=ZoneInfo('Australia/Sydney')).strftime('%H:%M:%S')}")
    print(f"Waszyngton: {dt.astimezone(tz=ZoneInfo('Etc/GMT+4')).strftime('%H:%M:%S')}") #Waszyngton jest w GMT-4, ale nie ma go w ZoneInfo (nie wiedzieć czemu w ZoneInfo GMT+4 to GMT-4)
    
time_zones_check(input("Podaj godzinę w formacie HH:MM:SS: "))

#Zad4
def time_to_birth(birthsday: datetime) -> None:
    now = datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
    diff = relativedelta.relativedelta(now, birthsday)
    new_birth = datetime(datetime.now().year, birthsday.month, birthsday.day)
    if now > new_birth:
        new_birth = new_birth.replace(year=new_birth.year+1)
    diff_new = new_birth - now
    print(f'Dzisiaj masz {diff.years} lat, {diff.months} miesięcy i {diff.days} dni. Do twoich kolejnych urodzin pozostało {diff_new.days} dni')
    
time_to_birth(datetime(1999,2,8))

#Zad5
def z5(filename: string, indx:int, src_format: string, dst_format: string) -> None:
    with open('lab_10/zad2.csv', newline='', encoding="utf8",errors="ignore") as f:
        with open(f'lab_10/{filename}.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile,delimiter=";")
            reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
            kolumny = next(reader, None)
            writer.writerow(kolumny)
            for wiersz in reader:
                data = datetime.strptime(wiersz[indx], src_format)
                wiersz[indx] = data.strftime(dst_format)
                writer.writerow(wiersz)

z5("zad5",2,"%Y%m%d","%Y-%m-%d")