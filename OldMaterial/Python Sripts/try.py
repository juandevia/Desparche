#example of try and except

while(True):
    # In this example i need a number no a string
    # Im asking for a number, 
    # Without the try and except, if the user type something differet than a number, the program will crash
    try :
        #see the int(), it will turn the string into a integer
        userInput=int(input('Plase enter a number: '))
        #in case the user type 0 the program will stop 
        if userInput == 0:
            #this breaks the while
            break
        print('good job, you entered number', userInput, 'type 0 to quit')
    #In case the user type something that can not be turned into an integer (example: 'j', 'juan') 
    except :
    #example: the user typed jsjkldsaklf, it will do this action but the program will still running
        print('are you stupid i asked for a number, type 0 to quit' )
