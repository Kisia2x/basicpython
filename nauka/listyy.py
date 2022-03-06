mylist = ["orange", "babana", "potato"]
print(mylist[2])

mylist.append("libra") # dodaje na końcu
print(mylist)

mylist.insert(2, "orangii") #insert dodaje na początku np gdy jest {[0,1]}
print(mylist)

mylist[1] = "blackcurrant" # zamienianie 1 wyrazu
print(mylist)
mylist.remove("potato")  #usuwanie konkretnego elementu
print(mylist)
mylist.sort() # sortowanie układanie od a do z
print(mylist)
newlist = ["ada", "ola", "mania"]
freshlist = mylist + newlist
print(freshlist)
freshlist.sort()
print(freshlist)
x = len(freshlist)  #funkcja len liczy ilość/długość listy 
print(x)       #ta długość jest wyliczona= x
print(len(freshlist)) # w1 linijce jest wyświetlanie i liczenie 
