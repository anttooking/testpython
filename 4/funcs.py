

def getANumber(prompt : str, retryAttempts : int = 4) -> int:
    """ Gets a number from the user with the given number of attempts"""
    while True:
        
        #Decrement retryAttempts
        if (retryAttempts <= 0):
            print('Exiting getANumber prompt')
            return "Failed"
        

        retryAttempts -= 1
        print('Attempts left =', retryAttempts +1, ' : ', end='')

        val = input(prompt)
        if (val.isnumeric()):
            return int(val)
        else:
            pass


#getANumber("gimme a number! ", retryAttempts=10)

# Lambda functions
t = lambda c: (c,-c,c)
print (t(3)) #turn into tupple (3,-3,3)


## PEP 8 https://www.python.org/dev/peps/pep-0008/
