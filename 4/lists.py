
squares = [1,2,3,4,5,6]
print(squares)

for q in squares:
    print(q*q)

for a in range(20,30):
    print(a)



def fib(n):
    t = [0,1]
    while len(t) < n:
        t.append(t[-1]+t[-2])
    return t


myList = fib(300)


print(fib(50))