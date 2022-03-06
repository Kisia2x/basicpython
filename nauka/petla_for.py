# PĘTLA FOR PRZECHODZI PO LISTACH



lista07 = ["Kwiatek", "Listek", "Doniczka"]
for i in lista07:
    print(i)
lista08 = ["pen","page","iphon11","bad","glass","warsaw","tr"]
for element in lista08:
    dlugość_elementu = len(element)
    if dlugość_elementu > 4:
        print("warunrk jrst spelniony")
    print(element)
    print(dlugość_elementu)   # printuję zmienną czyli liczymy litery
    # print("dlugość_elementu")  # printuję napis "dlugośc elementu" tu jest od razu podany napis
    #moj_napis = "jakis napis"   # zmienna powielająca napis czyli sting
    #print(moj_napis)
    print("---------")

print("PRZYKLAD 2")
lista08 = ["pen","page","iphon11","bad","glass","warsaw","tr"]
for element in lista08:
    dlugość_elementu = len(element)
    if dlugość_elementu < 4:
        print(element)

print("PRZYKLAD 3") #wszystkie pierwsze litery wypisujemy
lista08 = ["pen","page","iphon11","palec","glass","warsaw","tr"]
for element in lista08:
    pierwsza_litera = element[0]
    print(pierwsza_litera)

print("PRZYKLAD 4") #wszystkie elementy zaczynąjące się na p
lista08 = ["pen","page","iphon11","palec","glass","warsaw","tr"]
for element in lista08:
    pierwsza_litera = element[0]
    if pierwsza_litera == "p":
        print(element)  




