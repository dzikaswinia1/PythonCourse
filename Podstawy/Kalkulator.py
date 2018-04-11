print("Kalkulator ver. 1.0")

def dodaj(x, y):
    return int(x) + int(y)

def odejmij(x, y):
    return int(x) - int(y)

def pomnoz(x, y):
    return int(x) * int(y)

def podziel(x, y):
    return int(x) / int(y)

print("Wybierz opcje:")
print("1 - dodawanie")
print("2 - odejmowanie")
print("3 - mnozenie")
print("4 - dzielenie")

choose = input("Twoj wybor to: ")
num1 = input("Podaj pierwsza liczbe")
num2 = input("Podaj druga liczbe")

if choose == "1":
    print(num1, "+", num2, "=", dodaj(num1, num2))

elif choose == "2":
    print(num1, "-", num2, "=", odejmij(num1, num2))
elif choose == "3":
    print(num1, "*", num2, "=", pomnoz(num1, num2))
elif choose == "4":
    print(num1, "/", num2, "=", podziel(num1, num2))
else:
    print("Wybrałeś złą liczbę")