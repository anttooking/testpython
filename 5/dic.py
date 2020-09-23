

def squared(x):
    return x*x

def sumSquarted(n):
    summer = 0
    for i in range(0,n):
        summer += i*i
    return summer


sumsTo10 = {str(x) + "^2": sumSquarted(x) for x in range(0,10)} 
print(sumsTo10["3^2"])


##Seperating the tupples
for a,b in sumsTo10.items():
    print(a, " ==== ", b)

