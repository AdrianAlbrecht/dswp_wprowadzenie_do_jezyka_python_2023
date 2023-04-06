import csv
import datetime
from random import randint
import unicodedata
import re

#Zad 1
poland = []
germany = []
kolumny = []

with open('lab_06/zamowienia.csv', newline='', encoding="utf8",errors="ignore") as f:
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    kolumny = next(reader, None)
    for wiersz in reader:
        wiersz[4] = wiersz[4][:-2].replace(",",".").replace(" ","")
        date = wiersz[2].split(".")
        wiersz[2] = datetime.datetime(int(date[2]), int(date[1]), int(date[0])).strftime("%Y-%m-%d")
        if wiersz[0]=="Polska" :
            poland.append(wiersz)
        else:
            germany.append(wiersz)
          
with open('lab_06/zamowienia_polska.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile,delimiter=";")
    writer.writerow(kolumny)
    for wiersz in poland:
        writer.writerow(wiersz)
        
with open('lab_06/zamowienia_niemcy.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile,delimiter=";")
    writer.writerow(kolumny)
    for wiersz in germany:
        writer.writerow(wiersz)
        
#Zad 2
def file_splitter(files: list, newfile: str) -> None:
    with open('lab_06/'+newfile, 'w', newline='') as f:
        for file in files:
            with open('lab_06/'+file, 'r', newline='') as fi:
                for row in fi:
                    f.write(row)
                    
file_splitter(['zamowienia_niemcy.csv','zamowienia_polska.csv'],'new.csv')

#Zad3
def n_min_max(numbers: list[float|int], n: int, min_max: bool=False) -> list:
    if type(all(numbers)) != str:
        sort_numbers = numbers.copy()
        sort_numbers.sort(reverse=min_max)
        return sort_numbers[:n]
    else:
        return ["This list hasn't only numbers!"]
    
num = [1,8,-4,5.6,123,3.6]
print(n_min_max(num,4,True))
print(n_min_max(num,4))

#Zad 4
mieszana = [1, 2.3, 'Zbyszek', 5, 'Marian', 3.0]
dictionary = dict()
for x in mieszana:
    if type(x).__name__ not in dictionary.keys():
        dictionary[type(x).__name__] = [x]
    else:
        dictionary[type(x).__name__].append(x)
print(dictionary)

#Zad 5
names = ['Wyżlic',"Sapkowski","Malinowski","Hohenzolern","Albrecht", "Brunow","Gruszczyński","Żuchwa"]


def names_file(names: list[str]): #77 to M
    with open('lab_06/A-M_nazwiska.txt', 'w', encoding="utf-8", newline='') as am:
        with open('lab_06/N-Ż_nazwiska.txt', 'w',encoding="utf-8", newline='') as nz:
            for name in names:
                if ord(name[0].upper()) <= 77:
                    am.write(name+'\n')
                else:
                    nz.write(name+'\n')

names_file(names)

#Zad6
def word_reverse(sentence: str) -> str:
    new_sentence = ""
    for word in sentence.split(' '):
        new_sentence+=word[::-1]+" "
    return new_sentence

print(word_reverse("Ala ma kota"))

#Zad7
def play_cards() -> list:
    colors = ["Pik", "Karo", "Czerwo", "Trefl"]
    figure = ["As", "Król", "Dama", "Jopek"] + [str(x) for x in range(10,1,-1)]
    cards = [ y+' '+x for x in colors for y in figure]
    players = []
    for i in range(4):
        hand = []
        for j in range(5):
            card = cards[randint(0, len(cards)-1)]
            hand.append(card)
            cards.remove(card)
        players.append(hand)
    return f'Adrian: {players[0]}\nJanek: {players[1]}\nKacper: {players[2]}\nBartek: {players[3]}\n'
            
    
print(play_cards())

#Zad8
def generate_mails(filename: str, domain: str) -> None:
    with open('lab_06/mails.txt', 'w', newline='') as f:
        with open('lab_06/'+filename, 'r', newline='') as fi:
            for row in fi:
                name = unicodedata.normalize('NFD', row.replace("\r","").replace("\n","")).encode('utf-8','ignore').decode('ascii','ignore')
                f.write(name.lower().replace(" ",".")+f"@{domain}\n")
                
generate_mails("names.txt","student.uwm.edu.pl")

#Zad9
def fortune_wheel() -> None:
    sentences = []
    with open('lab_06/fortune.txt', 'r', encoding="utf-8", newline='') as f:
        for sentence in f:
            sentences.append(sentence.replace("\r","").replace("\n",""))
    to_guess = sentences[randint(0, len(sentences)-1)]
    covered = re.sub("[^., ]","_",to_guess)
    print(to_guess)
    while True:
        print(covered)
        if "_" in covered:
            answer = input("Czy chcesz odgadywać hasło? (Y/N)")
            if answer == "Y":
                sentence = input("Hasło to: ")
                if sentence == to_guess:
                    print("Hasło poprawne! :D")
                    break
                else:
                    print("Hasło błędne! :(((")
            else:
                character = input("Podaję literę: ")
                if len(character) == 1:
                    if character in to_guess:
                        if character in covered:
                            print("Litera powtórzona!")
                        else:
                            for x in range(len(to_guess)):
                                if to_guess[x] == character:
                                    covered = covered[:x]+character+covered[x+1:]
                    else:
                        print(f"Brak litery {character} w haśle! :(((") 
                else:
                    print("Podaj JEDNĄ literę!!!")
        else:
            print("Brak liter do odgadnięcia :(")
            break

fortune_wheel()