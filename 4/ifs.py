

x = int(input("please enter an integer:"))

#if, elif, else

if (x < 0):
    print('too low')
elif x == 0:
    print('too zero')
elif x == 1:
    print ('too one')
else:
    print('something else')

myWords = ['hello','world']

for word in myWords:
    print(word) 

for i in range(10):
    print(i)

anExample = [True, True, False, False, True, False]

def whereTrue (arr):
    for a in arr:
        if a == True:
            yield a

n = list(whereTrue(anExample))

print(n)