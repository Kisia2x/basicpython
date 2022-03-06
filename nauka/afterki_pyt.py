
a = 10
b = 20
e = 2,5
c = "trencz"
lista03 = ["trencz", "Adam", "Anna", 77]
print(a)
print(b)
print(e)
print(c)
print(lista03)

lista03.append("Dominika")
print(lista03)

g = len(lista03)
print(g)

dd = a + b
d = a - b
ddd = a/a
print(dd)
print(d)
print(ddd)

T = True
F = False
print(T)

###########
#zmienna przypisana do 0 
a = 0
print(a)
###
#zmienna przypisana do innej wartosci liczbowej np 55
a = 55
print(a)




if T == True:
    a = 1
print(a)
if F == True:
    a = 2   #gdy to jest źle podane to on podaje ponownie pierwsza poprawną liczbę 
print(a)

if F == False:
    a = 7
print(a)
if T == False:
    a = 4 # czemu wybrał 4 jako poprawną ?
print(a)

b = 1
if b > 0.2000:
    print("BIG")
if b < 2000:
    print("SMALL")

##########################

v = input( "podaj wartość: " )
print(v)
print(type(v))
    
z = int(v)  
print(z)
print(type(z))


if z > 500 and z <1000 : 
      print("warunrk mamy spełniony")

elif z > 10 and z < 499:      
   print("warunek całkiem ciekawy")
   
else:
   print("warunek jest niespełniony")

dictionary0 = {"Daniel": 32,
               "Damian": 27}

print(dictionary0)

dictionary2 = {"Daria": 28,
               "Dariusz": 27}
print(dictionary2)

G=11
print(G)
G = dictionary2["Dariusz" ] 
print(G)

dictionary11 = {"Mac": 2021,
                "IMac": 2022}
print(dictionary11)


def pole_powierzchni_ściany(a, b):
    pole = a*b*2 
    print("Wartość mojego pola to: ")
    print(pole)


a = int(input( "podaj szerokość: " ))


b = float(input( "podaj długość: " ))

pole_powierzchni_ściany(a,b)



def pole_powierzchni_ściany_z_wartością_2_75(a):
    pole = a*2.75*2 
    print("Wartość mojego pola to: ")
    print(pole)

liczba = int(input( "podaj szerokość: " ))

pole_powierzchni_ściany_z_wartością_2_75(liczba)

a = "Hej witajcie!"
print(a.upper())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("Hello", "Jestemmm"))


















    
