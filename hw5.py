a=input('Введите целые неотрицательные числа:\n')
a=a.split(" ")
for i in range(len(a)):
    a[i]=int(a[i])
a=sorted(a)
b=1
for i in range(len(a)):
    if b not in a:
        break
    else:
        b=b+1
print(b)