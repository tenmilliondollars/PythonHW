a=input("Введите строку\n")
a=a.lower()
a = a.split(" ")
b = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i]=1
 
maxi = 0
 
for key,value in b.items():
    if value > maxi:
        maxi= value
 
 
for key,value in b.items():
    if value == maxi:
        print(value , '-' , key)