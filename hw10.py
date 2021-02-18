n=int(input('Введите строку\n'))
k=0
while n > 1:
    if n % 2 == 0:
        n = n / 2
        k = k + 1 
    elif n % 2 > 0: 
        n = 3 * n + 1
        k = k + 1
print('Количество шагов:' , k)