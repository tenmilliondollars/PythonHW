def decpalindrom(x):
    if x == int(str(x)[::-1]):
        return True
    else:
        return False
 
def binpalindrom(x):
    if "{0:b}".format(x) == ("{0:b}".format(x)[::-1]):
        return True
    else:
        return False
c = 0
for i in range(0,1000000):
    if decpalindrom(i) and  binpalindrom(i):
        c += i
print(c)