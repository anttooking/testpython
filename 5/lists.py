fruits = ['orange', 'apple',  'reallylonglongfruit', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'reallylonglongfruit']


fruits.append('tinyfruit')
fruits.extend(['blueorange','blueapple'])

fruits.remove('apple')

##Standard
fruits.sort()


##Using Lambda to sort on fruit string length
newFruit = sorted(fruits, key = lambda fruit: len(fruit))
newFruit.reverse()

##print the fruit
print (newFruit)


