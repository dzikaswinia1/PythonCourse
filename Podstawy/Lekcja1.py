##LISTY
# Deklarowanie Listy []
array = ["Movies", "Games", "Python"]
print(array[0])
print(array[1])
print(array[2])

#DICTIONARIES - slowniki
#Deklarowanie slownika {}
dictionaries = {"name": "Nick", "age": 16, "hobby": "code maker"}
print(dictionaries["name"])
print(dictionaries["age"])

#Variables - zmienne
#Deklaracja zmiennych   // zmienne nazywamy w nastepujacySposob
string = "This is a string" + " Hello!"
print(string)
greetingWorld = "Hello World!"
print(greetingWorld)
greetingWorld = greetingWorld.split(" ")[0] #SPLIT dzieli tekst na czesci, uzywajac 0 otrzymamy "Hello" uzywajac 1 otrzymamy "World"
print(greetingWorld)
print(greetingWorld + " Nick") #laczymy zmienna z tekstem
number = 2
secondNumber = 3
print(number * secondNumber + secondNumber * number) #Operacje na zmiennych
check = True
print(check)
# KONWERTOWANIE NA INNE TYPY
#str()- konwersja na String
#int() - konwersja na Integer
#float() - konwersja na float...
#bool() - Boolean

#Inne funkcje
#len() - sprawdza dlugosc

lengthWord = "Hello!"
print(len(lengthWord))

#sorted([]) - sortuje tablice
sortMe = [4, 2, 6, 23, 63, 765, 3142]
print(sorted(sortMe))

sortWord = ["A", "C", "G", "H", "Z", "W", "b"] # Mala litera na koniec!
print(sorted(sortWord))

mixSort = ["5", "7", "5.2", "A", "C", "B", "F", "a", "o", "p"]
print(sorted(mixSort))
# Liczby - int i float rosnąco, pierw duże litery, potem małe :)

#Tworzenie wlasnych funkcji
# definiowanie fukcji - def // funckje definiujemy w ten_sposob

def my_function ():
    print("This is my function")
    print("A second string")

my_function()









