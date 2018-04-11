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

#Dodawanie argumentow do fukcji

def second_function(str1, str2):
    print(str1)
    print(str2)

second_function("\nThis is argument one", "This is the second argument")

#Argumenty podstawowe

def print_something(name, age):
    print("\nMy name is ", name, "my age is ", age)

print_something("Nick", 29)

def new_argument(name = "Someone", age = "Unknow"):
    print("\n My name is ", name, "my age is ", age)

new_argument()
new_argument("Patryk", 16)

#Slowa kluczowe argumentow

new_argument(age = 27, name = "Nick")

#Nieskoczone argumenty
#Za pomoca * mozemy dodawac niezliczona ilosc argumentow
#Petla "for person in people" iteruje nasze podane argumenty.

def print_people(*people):
    for person in people:
        print("This person is", person)

print_people("Nick", "Dan", "Jack", "King", "Smiley")

#Zwraacanie wartosci z funkcji
# Używamy funkcji RETURN (return)

def do_math(num1, num2):
    return num1 + num2

math1 = do_math(2, 7)
math2 = do_math(11, 34)

print("First sum is", math1, "and the second sum is", math2)

#Petla IF ELIF ELSE

check = "Hamburger"

if check == False:
    print("It is false!")
elif check == "Hamburger":
    print("Yummm, hamburgers")
elif check == "Yo":
    print("Hello!")
else:
    print("It is actually equal to true")

#Petla For WHILE
numbers = [1, 2, 3, 4, 5]

for item in numbers: #Iterujemy i wypisujemy kazdy element tablicy
    print(item)

names = ["Nick", "Someone", "Patryk"]

for items in names:
    print("This person name is", items)

#Petla WHILE
run = True
current = 1

while run:
    if current == 10:
        run = False
    else:
        print(current)
        current +=1












