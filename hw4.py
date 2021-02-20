import re
a=input('Введените целые неотрицательные числа:\n')
sum=0
c=re.findall(r'[+-]?\d+', a)
for i in range(len(c)):
    c[i]=int(c[i])
for i in range(len(c)):
    sum=sum+c[i]
print(sum)


