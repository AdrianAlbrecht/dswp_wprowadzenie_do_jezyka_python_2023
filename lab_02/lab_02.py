#Zad 1
sentence = input('Wpisz dowolne zdanie z jednolitym separatorem (spacja, średnik, itd.):\n')
source_separator = input('Podaj separator z powyższego zdania:\n')
destination_separator = input('Podaj separator docelowy:\n')

split_sentence = sentence.split(source_separator)
sentence = destination_separator.join(split_sentence)
print('Twoje nowe zdanie:\n'+sentence+'\n')

#Czy można szybciej/lepiej?
sentence = input('Wpisz dowolne zdanie z jednolitym separatorem (spacja, średnik, itd.):\n')
separators = input('Podaj separatory (źródłowy i docelowy) rozdzielone literą "r":\n')
source, destination = separators.split('r')
sentence= sentence.replace(source, destination)
print('Twoje nowe zdanie:\n'+sentence+'\n')
#Czy lepiej? Nie wiem...

#Zad 2
lorem_ipsum = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'

#Zad 3
#U mnie litera1 === litera2, więc wziąłem pierwszą literę z imienia, aby pobawić się w wielkie/małe litery
litera_1 = 'Adrian'[0]
litera_2 = 'Albrecht'[3] 
liczba_liter1 = lorem_ipsum.lower().count(litera_1.lower())
liczba_liter2 = lorem_ipsum.lower().count(litera_2.lower())
print(f'W tekście jest {liczba_liter1} liter {litera_1.lower()} oraz {liczba_liter2} liter {litera_2.lower()}')