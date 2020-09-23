

def getANumber(prompt, retryAttempts = 4):
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


getANumber("gimme a number! ", retryAttempts=10)