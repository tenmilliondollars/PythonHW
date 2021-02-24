n=int(input('Введите количество шагов:\n'))
def f(n):  
    if n == 0:
        return 0  
    if n == 1 or n==2:
        return 1  
    else:
        return (f(n-1) + f(n-2))
for i in range (n+1):
    print(f(i))

