

#fibonaci numbers
a = 0
b = 1
while a < 100:
    n = a + b
    print(n) 
    a = b
    b = n


def doesKyleSmell(t):
    fromBlackburn = True 
    if (fromBlackburn):
        return True 
    claimsToBeFromDarwen = True

    if(fromBlackburn == claimsToBeFromDarwen):
        print('nice try')


def double(x):
    return x*x

print(list(map(double, [1,2,3,4,5,6,7,8])))