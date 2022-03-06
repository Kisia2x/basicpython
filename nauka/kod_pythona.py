# liczby ab to całkowite
####a to jest zmienna(wariable) przechowuje 10
#Variabl type int, valiu 10 
a = 10
b = 20

#zmiennan zmiennoprzecinkowa
#Variabl type flloat valiu 2,5 
d = 2.5

#typ danych napis czyli string, łańcuch znaków
#zmienna o nazwie c typ string wartość "trend"
# wariable name c type string valiu have "trend" 
c = "trend"


# to jest moja lista
#wariale name list01 type list valiu have trend a 76
lista01 = ["trend",a,76]

#funkcja print dzięki której wszystko mi się wyświetli
#piszac w edytorze ukrywam co się dzieje w czaie żeczywistym a program wie co ma robić




print(a)


#print(lista01)

lista02 = ["Agata", "Andżela", "Anna"]
#tworzymy kolejną zmienną i wyjmujemy 1 osobę 2 z 3 
osoba1 = lista02[0]
# pierwsza osoba wpisana na litre A jest jako nr 0 kolejna to 1 a następna to 3
#zawsze zaczyna się wszystko od 0


print(osoba1)
#dodaliśmy 1 kolejną osobę do całej listy pisząc .append("Dominika")
lista02.append("Dominika")
#prontem zawsze sprawdzam czy to co napisałam jest dobre w IDLE Shell

print(lista02)
#len to funkcja liczaca dlugość typu danych czyli liczy 4 imiona jako 4 oddzielne znaki

e = len(lista02)
#print sprawdza nam kod 
print(e)

# tworze kolejną zmienna o nazwie x która ma wynik a+b

x = a + b
print(x)

# tworzenie zmiennej mnożenia i odejmowania
y = b*b - a
print(y)

#tworzenie zmiennej operacji dzielenia
z = a/a
print(z)
#gdy
lista03 = [1,2,3]
liczbazlisty03 = lista03[1] + 1    #######################
print(liczbazlisty03)

#Typ bool, wyświetlanie prawda fałsz 

T = True
F = False
print(T)


#Instrukcja warunkowa słowo if

if T == True:
    a = 1

if F == True:
    a = 2
print(a)

if F == False:
    a = 2

b = 1
##### b jest wieksze 
if b > 0.2000:
    print("BIG")

    #### jest mniejsze 
if b < 2000:
    print("SMALL")
                   ##### tutaj mam 2 instrukcje z 2ma ifami niezaleznymi
###
# on pyta o liczbę podaję wartość 2 i on ją zapamiętje w zmiennej o nazwie v
#wiem ze wartosc kolejna po sprawdzeniu to jest liczba a program widzi to jako napis
v = input( "podaj liczę: " )
print(v)
print(type(v))   # on ten tym rozpoznaje jako string 

#konwertujemy v na liczbę czyli napis na liczbę 
w = int(v)    #zamieniamy v na w 
print(w)
print(type(w))


     #### tu mam 1 cały blok if 
if w > 500 and w <1000 :     #zawsze po ifie print jest na boku 
   print("warunrk jrst sprlniony") 
elif w > 105 and w < 499:         #tu mogę podać dodatkowy warunek do zapytania 
   print("warunrk jrst ciekawy")
else:
   print("warunrk jrst niesprlniony")
##         a=3 to jest zmienna a i ona ma liczbę 3, jest typu int
##       a= "3" to jest zmienna a lecz ma napis 3, i teraz jest typ string




#klucz to agata a wiek to 27 
dictionary0 = {"Agata": 27,
               "Anna": 28}
print(dictionary0)


#
## słownik to klucz i wartoś czyli trzeba podac
##pary informacji 
## lub podać nazwę i wskaźnik wpisujemy co chcemy ale ma być para wartości 
dictionary1 = {"Monika": 27,
               "Blazej": 28}
print(dictionary1)

###wyjmujemy wartość wieku Moniki czyli 2 daną
f = 11
print(f)
f = dictionary1["Monika"]
print(f)


dictionary11 = {"MAC": 227,
               "BWW": 25558}
print(dictionary11)

###############################################



 # FUNKCJA a pole to nazwa tej funkcji


 #i argumenty funkcji sa mieszczone w nawiasie czyli a i b czyli długość i szerokość 
            #Robimy funkcje własną

def pole_powierzchni_ściany(a, b):
    pole = a*b*2 
    print("Wartosc nojrgo pola to: ")
    print(pole)
    
a = int(input( "podaj szerokość: " ))
#input pobiera od uzytkownika daną w cyfrze
b = float(input( "podaj długość: " ))
#floar pobiera daną z zmienno przecinkową z kropką 

pole_powierzchni_ściany(a,b)




def pole_powierzchni_ściany_z_automatyczną_2_75(a):
    pole = a*2.75*2 
    print("Wartosc nojrgo pola to: ")
    print(pole)
    
liczba = int(input( "podaj szerokość: " ))
#input pobiera od uzytkownika daną w cyfrze
pole_powierzchni_ściany_z_automatyczną_2_75(liczba)

#Use the format() method to insert numbers into strings:

age = 34
txt = "My name is {}, and i have {} years and I have {} dogs"
name = "daniel"
liczbaPsow = 2 
print(txt.format(name,age,liczbaPsow))



#kodowanie jest zaskakujące 
