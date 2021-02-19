a=input('Введените целые неотрицательные числа:\n')
a=a.split(" ")
a=sorted(a)
for i in range(len(a)):
    a[i]=int(a[i])
b=1
for i in range(len(a)):
    if b not in a:
        print(b)
        break
    else:
        b=b+1