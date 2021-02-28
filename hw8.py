def check(a):
       while True:
            a=input('Введите текст: ')
            if a == 'cancel':
                return ('Bye!')
                break
            else:
                counting(a)

def counting(a):
    try:
        a=(int(a))
        if a % 2 == 0: 
            print (int(a/2))
        elif a % 2 > 0:
            print (int(3*a+1))
    except ValueError:
        print('Не удалось преобразовать введенный текст в число.')


print (check(1))



