 #FUNKCJA a pole to nazwa tej funkcji


 #i argumenty funkcji sa mieszczone w nawiasie czyli a i b czyli długość i szerokość 
            #Robimy funkcje własną

def pole_powierzchni_ściany(a, b):
    pole = a*b*2 
    print("Wartosc mojego pola to: ")
    print(pole)
    
a = int(input( "podaj szerokość: " ))
#input pobiera od uzytkownika daną w cyfrze
b = float(input( "podaj długość: " ))
#floar pobiera daną z zmienno przecinkową z kropką 

pole_powierzchni_ściany(a,b)
print(a)




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

#funkcja ma oddać mi większa liczbę
def zwroc_wieksze(a, b):
    if a > b:               #warunek sprawdza a większe od b           
        return a          # pokaż mi a jeśli jest prawdziwe 
    else:
        return b          # daj mi b 

                                      
x = zwroc_wieksze(10, 35)   #poniewaz a nie jest większe od b to pokazuje mi a i b 
print(x)


2


