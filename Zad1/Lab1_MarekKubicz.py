import random
print('\n Zad 2')
uczelnia = "Studiuję na WSIIZ"
print(uczelnia)


print('\n Zad 3')
imie = "Jan"
wiek = 20
wzrost = 178
print(f"Nazywam się {imie} i mam {wiek} lat.")
print(f"Mój wzrost to 178 cm")


print('\n Zad 4')
cena = "39.99 PLN"
rabat = 20                                           #Przyjmujemy że to są procenty 
cena = float(cena[:-3])                          #Wycinamy 3 ostatnie symbole i zmieniam na float, każdy skrót walutowy zapinasy w ISO code ma 3 symbole
cena = cena - (cena*rabat)/100
cena = '{0:.2f}'.format(cena)
print(cena)


print('\n Zad 5')
a = int(input("Podaj bok a: "))
h = int(input("Podaj bok b: "))
print(f"Pole: {a*h}, Obwód: {(a+h)*2}")


print('\n Zad 6')
d = input("Podaj drogę (zostaw puste jeśli chcesz losowe): ")
spalenie = float(input("Podaj ile pali samochód na 100km: "))/100
cena_paliwa = 6.5 #zł/l
if d == '':
    d = random.randint(10,1000)
    cena_paliwa = float(input("podaj cene paliwa zł/l (samą liczbę)"))
else:
    d=int(d)
print(f'Droga: {d}, Spalanie: {spalenie*100}, Cena paliwa: {cena_paliwa}, Spalone Paliwo: {spalenie*d} Wydane pieniądze na paliwo: {spalenie*d*cena_paliwa}')


print('\n Zad 7')
a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
print('Rozwiązanie: ', b/a*-1)


print('\n Zad 8')
a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))

delta = b**2-4*(a*c)
if delta < 0: print("Brak rozwiązania")
elif delta == 0: print(f'Jest jedno rozwiązanie: {b/a*-1}')
else:
    delta = delta**(1/2)
    odp1 = (-b+delta)/(2*a)
    odp2 = (-b-delta)/(2*a)
    print(f'x1: {odp1} x2: {odp2}')
